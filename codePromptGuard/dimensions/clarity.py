"""
Clarity dimension scorer — checks structural completeness, not just word presence.
"""

def score_clarity(prompt_text):
    text = prompt_text.lower()
    score = 0
    reasons = []

    # Has a clear action verb at start
    action_verbs = [
        'implement', 'write', 'create', 'build', 'design',
        'develop', 'calculate', 'find', 'detect', 'generate',
        'parse', 'convert', 'validate', 'check', 'return'
    ]
    if any(text.strip().startswith(v) for v in action_verbs):
        score += 20
        reasons.append("+20: starts with clear action verb")
    elif any(v in text for v in action_verbs):
        score += 10
        reasons.append("+10: contains action verb")

    # Specifies what to return
    if any(phrase in text for phrase in [
        'return', 'output', 'result', 'print', 'yield'
    ]):
        score += 15
        reasons.append("+15: specifies expected output")

    # Specifies input format
    if any(phrase in text for phrase in [
        'input', 'given', 'takes', 'accepts', 'parameter',
        'argument', 'array', 'string', 'integer', 'list', 'dict'
    ]):
        score += 15
        reasons.append("+15: describes input")

    # Has constraints or requirements
    if any(phrase in text for phrase in [
        'must', 'should', 'cannot', 'only', 'always',
        'never', 'exactly', 'at least', 'at most'
    ]):
        score += 15
        reasons.append("+15: has explicit constraints")

    # Reasonable length (too short = vague, too long = cluttered)
    word_count = len(prompt_text.split())
    if 10 <= word_count <= 80:
        score += 20
        reasons.append(f"+20: good length ({word_count} words)")
    elif word_count < 5:
        score -= 20
        reasons.append(f"-20: too short ({word_count} words), likely vague")
    elif word_count > 150:
        score -= 5
        reasons.append(f"-5: very long ({word_count} words), may be cluttered")

    # Has multiple sentences = more structured
    sentence_count = text.count('.') + text.count('?') + text.count('\n')
    if sentence_count >= 2:
        score += 15
        reasons.append("+15: multi-sentence, structured")

    return {
        'score': max(0, min(100, score)),
        'reasons': reasons
    }


def measure_clarity(prompt: str) -> dict:
    result = score_clarity(prompt)
    return {
        'clarity_score': result['score'],
        'breakdown': {
            'reasons': result['reasons']
        }
    }
