"""
repair.py — Diagnosis-Driven Prompt Repair (DDPR)
Targeted repair respects prompt type — doesn't add irrelevant dimensions.
"""
import os

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    def load_dotenv(path=".env"):
        if not os.path.exists(path):
            return False

        with open(path, "r", encoding="utf-8") as env_file:
            for line in env_file:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue

                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip().strip("'\""))
        return True

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
from groq import Groq
from dimensions.health_score import compute_overall_health_score, detect_prompt_type


client = Groq(api_key=GROQ_API_KEY)

REPAIR_THRESHOLD = 40

# Dimensions relevant per prompt type
RELEVANT_DIMENSIONS = {
    'algorithm': ['clarity', 'edge_cases', 'context', 'testability'],
    'software':  ['clarity', 'error_handling', 'security', 'context', 'testability', 'edge_cases'],
    'general':   ['clarity', 'error_handling', 'context', 'edge_cases']
}

REPAIR_INSTRUCTIONS = {
    'error_handling': "specify what should happen on invalid input or errors (e.g., raise ValueError, return -1)",
    'edge_cases':     "mention edge cases to handle such as empty input, zero, negative numbers, single element, boundary conditions",
    'security':       "add input validation or safe handling requirements",
    'context':        "specify the programming language, expected data types, and input/output format",
    'testability':    "provide one concrete input-output example showing expected behavior",
    'clarity':        "restate the task precisely with clear input format and expected output format"
}

def diagnose(prompt_text):
    result = compute_overall_health_score(prompt_text)
    prompt_type = detect_prompt_type(prompt_text)
    breakdown = result['breakdown']
    relevant = RELEVANT_DIMENSIONS.get(prompt_type, RELEVANT_DIMENSIONS['general'])

    # Only flag dimensions that are BOTH weak AND relevant to this prompt type
    weak_relevant = {
        dim: score
        for dim, score in breakdown.items()
        if score < REPAIR_THRESHOLD and dim in relevant
    }

    return weak_relevant, result['overall_health_score'], prompt_type

def repair(prompt_text):
    weak_dims, original_score, prompt_type = diagnose(prompt_text)

    if not weak_dims:
        repaired_score = compute_overall_health_score(prompt_text)['overall_health_score']
        return {
            'original': prompt_text,
            'repaired': prompt_text,
            'original_score': original_score,
            'repaired_score': repaired_score,
            'prompt_type': prompt_type,
            'weak_dimensions': {},
            'repairs_applied': [],
            'improvement': 0
        }

    repair_targets = [
        f"- {dim}: {REPAIR_INSTRUCTIONS[dim]}"
        for dim in weak_dims
        if dim in REPAIR_INSTRUCTIONS
    ]

    repair_prompt_text = f"""You are improving a code generation prompt by adding missing details.

ORIGINAL PROMPT: "{prompt_text}"

This prompt is weak in these specific areas. Add ONLY what is missing:
{chr(10).join(repair_targets)}

Rules:
- Keep the original intent completely intact
- Only ADD the missing information, do not rewrite the whole prompt
- Keep it concise — add 1-2 sentences maximum
- Do not add unrelated requirements

Return ONLY the improved prompt, nothing else."""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": repair_prompt_text}],
            max_tokens=300,
            temperature=0.2
        )
        repaired_text = response.choices[0].message.content.strip()
        repaired_score = compute_overall_health_score(repaired_text)['overall_health_score']

        return {
            'original': prompt_text,
            'repaired': repaired_text,
            'original_score': original_score,
            'repaired_score': repaired_score,
            'prompt_type': prompt_type,
            'weak_dimensions': weak_dims,
            'repairs_applied': list(weak_dims.keys()),
            'improvement': round(repaired_score - original_score, 1)
        }

    except Exception as e:
        print(f"Repair error: {e}")
        return None
