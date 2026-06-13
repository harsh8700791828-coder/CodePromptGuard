"""
Testability dimension — checks if prompt makes output verifiable.
"""

def score_testability(prompt_text):
    text = prompt_text.lower()
    score = 0
    reasons = []

    # Provides concrete examples
    if any(phrase in text for phrase in [
        'example', 'for example', 'e.g.', 'such as',
        'sample', 'instance', 'demonstration'
    ]):
        score += 25
        reasons.append("+25: provides examples")

    # Return type specification counts as testable output
    if any(phrase in text for phrase in [
        'return {', 'return true', 'return false',
        'valid:', 'bool', 'errors:', '{valid',
        'standardized format', 'standardized',
        'validation result'
    ]):
        score += 25
        reasons.append("+25: specifies structured return type")

    # Specifies expected output format
    if any(phrase in text for phrase in [
        'return true', 'return false', 'return -1',
        'return none', 'returns a list', 'returns a dict',
        'output should be', 'result should'
    ]):
        score += 25
        reasons.append("+25: specifies exact output")

    # Mentions test cases or assertions
    if any(phrase in text for phrase in [
        'test', 'assert', 'verify', 'unit test',
        'should pass', 'must pass'
    ]):
        score += 25
        reasons.append("+25: mentions testing")

    # Has input-output pair (>>> style or explicit)
    if '>>>' in text or '->' in text or '=>' in text:
        score += 25
        reasons.append("+25: has input-output example")

    return {
        'score': max(0, min(100, score)),
        'reasons': reasons
    }


def measure_testability(prompt: str) -> dict:
    result = score_testability(prompt)
    return {
        'testability_score': result['score'],
        'breakdown': {
            'reasons': result['reasons']
        }
    }
