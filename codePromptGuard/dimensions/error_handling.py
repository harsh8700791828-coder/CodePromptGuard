"""
Error handling dimension — checks if prompt explicitly requires robust error handling.
"""

def score_error_handling(prompt_text):
    text = prompt_text.lower()
    score = 0
    reasons = []

    # Explicitly asks for exception handling
    if any(phrase in text for phrase in [
        'raise', 'exception', 'try', 'catch', 'except',
        'throw', 'handle error', 'error handling'
    ]):
        score += 30
        reasons.append("+30: asks for exception handling")

    # Mentions specific error cases
    if any(phrase in text for phrase in [
        'if invalid', 'if not found', 'if empty',
        'when error', 'on failure', 'gracefully',
        'return error', 'return none', 'return -1'
    ]):
        score += 25
        reasons.append("+25: specifies error return behavior")

    # Mentions what to do with bad input
    if any(phrase in text for phrase in [
        'invalid input', 'bad input', 'malformed',
        'unexpected input', 'wrong type', 'negative number'
    ]):
        score += 25
        reasons.append("+25: handles bad input explicitly")

    # General error awareness
    if any(phrase in text for phrase in [
        'error', 'fail', 'wrong', 'invalid', 'missing'
    ]):
        score += 10
        reasons.append("+10: general error awareness")

    # Explicitly ignores errors (bad)
    if any(phrase in text for phrase in [
        'ignore error', 'skip error', 'no need to handle',
        'assume valid', 'assume correct'
    ]):
        score -= 25
        reasons.append("-25: explicitly ignores errors")

    return {
        'score': max(0, min(100, score)),
        'reasons': reasons
    }


def measure_error_handling(prompt: str) -> dict:
    result = score_error_handling(prompt)
    return {
        'error_handling_score': result['score'],
        'breakdown': {
            'reasons': result['reasons']
        }
    }
