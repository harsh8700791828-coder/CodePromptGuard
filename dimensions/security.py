"""
Security dimension scorer — context-aware, not binary keyword matching.
Scores 0-100 based on security consciousness in the prompt.
"""

def score_security(prompt_text):
    text = prompt_text.lower()
    score = 0
    reasons = []

    # --- POSITIVE signals (prompt shows security awareness) ---

    # Asks for format validation (validation is a security concern)
    if any(phrase in text for phrase in [
        'validate', 'validation', 'validator',
        'format check', 'check format', 'verify format',
        'must be', 'must have', 'only digits', 'only numbers',
        'cannot be', 'should not', 'not allowed'
    ]):
        score += 20
        reasons.append("+20: asks for format/constraint validation")

    # Explicitly asks to avoid dangerous functions
    if any(phrase in text for phrase in [
        'do not use eval', 'avoid eval', 'no eval',
        'do not use exec', 'avoid exec',
        'sanitize', 'sanitise',
        'parameterized query', 'parameterised query',
        'prepared statement'
    ]):
        score += 25
        reasons.append("+25: explicitly avoids dangerous patterns")

    # Asks for input validation
    if any(phrase in text for phrase in [
        'validate input', 'validate the input', 'input validation',
        'validate user', 'check input', 'verify input'
    ]):
        score += 20
        reasons.append("+20: asks for input validation")

    # Mentions injection prevention
    if any(phrase in text for phrase in [
        'sql injection', 'xss', 'cross-site', 'injection attack',
        'injection prevention', 'prevent injection'
    ]):
        score += 20
        reasons.append("+20: mentions injection prevention")

    # Asks for authentication/authorization awareness
    if any(phrase in text for phrase in [
        'authentication', 'authorization', 'auth check',
        'permission', 'access control'
    ]):
        score += 15
        reasons.append("+15: mentions auth/access control")

    # Mentions secure coding generally
    if any(phrase in text for phrase in [
        'secure', 'security', 'vulnerability', 'safe',
        'protect', 'malicious'
    ]):
        score += 10
        reasons.append("+10: general security awareness")

    # Asks for secrets/credential handling
    if any(phrase in text for phrase in [
        'password', 'secret', 'credential', 'token',
        'api key', 'encrypt', 'hash'
    ]):
        score += 10
        reasons.append("+10: handles sensitive data")

    # --- NEGATIVE signals (prompt introduces risk) ---

    # Uses eval/exec carelessly (without safety context)
    eval_mentioned = 'eval(' in text or 'exec(' in text
    safety_context = any(w in text for w in [
        'avoid', 'do not', 'never', 'safe', 'instead'
    ])
    if eval_mentioned and not safety_context:
        score -= 15
        reasons.append("-15: uses eval/exec without safety context")

    # Asks to skip validation explicitly
    if any(phrase in text for phrase in [
        'skip validation', 'no validation', 'without validation',
        'ignore errors', 'no error check'
    ]):
        score -= 20
        reasons.append("-20: explicitly skips validation")

    return {
        'score': max(0, min(100, score)),
        'reasons': reasons
    }


def measure_security(prompt: str) -> dict:
    result = score_security(prompt)
    return {
        'security_score': result['score'],
        'breakdown': {
            'reasons': result['reasons']
        }
    }
