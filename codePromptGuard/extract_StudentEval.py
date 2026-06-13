# extract_studenteval.py
from datasets import load_dataset
from datasets.exceptions import DatasetNotFoundError
import json
import os
import sys

print("Downloading StudentEval...")

try:
    ds = load_dataset(
        "wellesley-easel/StudentEval",
        split="test",
        token=os.getenv("HF_TOKEN") or None,
    )
except DatasetNotFoundError:
    print(
        "\nStudentEval is a gated Hugging Face dataset.\n"
        "Fix:\n"
        "1. Request access at https://huggingface.co/datasets/wellesley-easel/StudentEval\n"
        "2. After access is approved, either run `huggingface-cli login` or set HF_TOKEN.\n"
        "   PowerShell example: $env:HF_TOKEN='hf_your_token_here'\n"
    )
    sys.exit(1)
except FileNotFoundError as exc:
    message = str(exc)
    if "403 Forbidden" in message or "public gated repositories" in message:
        print(
            "\nYour Hugging Face token does not allow public gated repositories.\n"
            "Fix your token settings:\n"
            "1. Go to https://huggingface.co/settings/tokens\n"
            "2. Edit or create a token with read access.\n"
            "3. For a fine-grained token, enable access to public gated repositories.\n"
            "4. Make sure the same account has been approved for StudentEval access.\n"
            "5. Run again with: $env:HF_TOKEN='hf_your_token_here'\n"
        )
        sys.exit(1)
    raise

extracted = []
seen_problems = set()

for item in ds:
    problem = item.get("problem_name", "")
    if problem not in seen_problems and len(extracted) < 10:
        seen_problems.add(problem)
        extracted.append({
            "id": f"student-{len(extracted)+1:03d}",
            "source": "studenteval",
            "title": problem,
            "text": item.get("prompt", ""),
            "passed": item.get("passed", False)
        })

os.makedirs("prompts", exist_ok=True)

with open("prompts/studenteval_prompts.json", "w") as f:
    json.dump({"prompts": extracted}, f, indent=2)

print(f"Saved {len(extracted)} StudentEval prompts")
