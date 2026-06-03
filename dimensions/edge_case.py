"""
Edge cases dimension — checks if prompt asks to handle boundary conditions.
"""

def score_edge_cases(prompt_text):
    text = prompt_text.lower()
    score = 0
    reasons = []

    # Mentions specific edge cases
    specific_edges = {

        'exactly': 15,
        'special character': 15,
        'no special': 15,
        '+91': 10,
        'international': 10,
        'prefix': 10,
        'negative price': 20,
        'rounding': 10,
        'decimal': 10,
        'all zeros': 15,
        'not all': 10,  
        'empty': 15, 'null': 15, 'none': 10,
        'zero': 15, 'negative': 15, 'overflow': 15,
        'single element': 15, 'one element': 15,
        'duplicate': 10, 'boundary': 15,
        'maximum': 10, 'minimum': 10,
        'large input': 10, 'very large': 10
    }
    for phrase, points in specific_edges.items():
        if phrase in text:
            score += points
            reasons.append(f"+{points}: mentions '{phrase}' edge case")

    # Uses the phrase "edge case" explicitly
    if 'edge case' in text:
        score += 20
        reasons.append("+20: explicitly mentions edge cases")

    # Asks to handle multiple scenarios
    if any(phrase in text for phrase in [
        'all cases', 'any case', 'various', 'different scenarios',
        'handle all', 'consider all'
    ]):
        score += 15
        reasons.append("+15: asks for comprehensive coverage")

    return {
        'score': max(0, min(100, score)),
        'reasons': reasons
    }


def measure_edge_case_coverage(prompt: str) -> dict:
    result = score_edge_cases(prompt)
    return {
        'edge_case_score': result['score'],
        'breakdown': {
            'reasons': result['reasons']
        }
    }
