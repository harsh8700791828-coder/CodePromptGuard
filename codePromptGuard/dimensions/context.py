"""
Context dimension — checks if prompt provides enough background for accurate generation.
"""

def score_context(prompt_text):
    text = prompt_text.lower()
    score = 0
    reasons = []

    # Specifies programming language
    languages = [
        'python', 'java', 'javascript', 'c++', 'typescript',
        'go', 'rust', 'kotlin', 'swift', 'ruby'
    ]
    if any(lang in text for lang in languages):
        score += 25
        reasons.append("+25: specifies programming language")

    # Specifies data structure or type
    if any(phrase in text for phrase in [
        'array', 'list', 'string', 'integer', 'float',
        'dictionary', 'dict', 'set', 'tree', 'graph',
        'linked list', 'stack', 'queue', 'tuple'
    ]):
        score += 20
        reasons.append("+20: specifies data types")

    # Mentions performance requirements
    if any(phrase in text for phrase in [
        'o(n)', 'o(log n)', 'o(1)', 'time complexity',
        'space complexity', 'efficient', 'optimize',
        'in-place', 'constant space'
    ]):
        score += 20
        reasons.append("+20: mentions complexity/performance")

    # Mentions constraints on input
    if any(phrase in text for phrase in [
        'sorted', 'unsorted', 'positive', 'non-negative',
        'distinct', 'unique', 'size', 'length', 'range'
    ]):
        score += 20
        reasons.append("+20: specifies input constraints")

    # Validation context signals
    if any(phrase in text for phrase in [
        'digits', 'characters', 'format', 'length',
        'starts with', 'prefix', 'suffix',
        '10 digits', '6 digits', '12 digits',
        'alphanumeric', 'numeric', 'letters'
    ]):
        score += 20
        reasons.append("+20: specifies format/length constraints")

    # Indian domain context
    if any(phrase in text for phrase in [
        'indian', 'india', '+91', 'aadhaar', 'pan',
        'gst', 'pincode', 'mobile number'
    ]):
        score += 15
        reasons.append("+15: domain context specified")

    # General domain context
    if any(phrase in text for phrase in [
        'api', 'database', 'file', 'network', 'web',
        'class', 'object', 'module', 'library'
    ]):
        score += 15
        reasons.append("+15: provides domain context")

    return {
        'score': max(0, min(100, score)),
        'reasons': reasons
    }


def measure_context(prompt: str) -> dict:
    result = score_context(prompt)
    return {
        'context_score': result['score'],
        'breakdown': {
            'reasons': result['reasons']
        }
    }
