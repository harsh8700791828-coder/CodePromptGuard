"""
Dimension 2: Error Handling & Robustness
Measures how well the prompt specifies error conditions and edge cases
"""

import re


def measure_error_handling(prompt: str) -> dict:
    """
    Score error handling in a prompt (0-100)
    
    Checks for:
    - Edge cases mentioned?
    - Error conditions addressed?
    - Invalid input handling?
    - Boundary conditions?
    - Fallback strategies?
    """
    
    score = 0
    details = {}
    
    # Check 1: Are edge cases mentioned?
    edge_case_keywords = [
        'edge case',
        'corner case',
        'boundary',
        'empty',
        'null',
        'single element',
        'extreme'
    ]
    
    has_edge_cases = any(kw in prompt.lower() for kw in edge_case_keywords)
    
    if has_edge_cases:
        score += 20
        details['edge_cases_mentioned'] = 'YES'
    else:
        details['edge_cases_mentioned'] = 'NO'
    
    # Check 2: Are error/exception conditions mentioned?
    error_keywords = [
        'error',
        'exception',
        'invalid',
        'invalid input',
        'raise',
        'throw',
        'error handling'
    ]
    
    has_error_handling = any(kw in prompt.lower() for kw in error_keywords)
    
    if has_error_handling:
        score += 20
        details['error_conditions_mentioned'] = 'YES'
    else:
        details['error_conditions_mentioned'] = 'NO'
    
    # Check 3: Are negative/zero values mentioned?
    has_negative_handling = bool(re.search(
        r'(negative|zero|below|minimum)',
        prompt,
        re.IGNORECASE
    ))
    
    if has_negative_handling:
        score += 15
        details['negative_zero_handling'] = 'YES'
    else:
        details['negative_zero_handling'] = 'NO'
    
    # Check 4: Are duplicates/special cases mentioned?
    has_special_cases = bool(re.search(
        r'(duplicate|special|unique|repeated|distinct)',
        prompt,
        re.IGNORECASE
    ))
    
    if has_special_cases:
        score += 15
        details['special_cases_mentioned'] = 'YES'
    else:
        details['special_cases_mentioned'] = 'NO'
    
    # Check 5: Are large inputs mentioned?
    has_large_input = bool(re.search(
        r'(large|million|billion|10\^|very large|huge)',
        prompt,
        re.IGNORECASE
    ))
    
    if has_large_input:
        score += 15
        details['large_input_mentioned'] = 'YES'
    else:
        details['large_input_mentioned'] = 'NO'
    
    # Check 6: Are constraints on invalid behavior mentioned?
    has_constraints = bool(re.search(
        r'(must not|should not|cannot|do not|don\'t)',
        prompt,
        re.IGNORECASE
    ))
    
    if has_constraints:
        score += 15
        details['constraint_specified'] = 'YES'
    else:
        details['constraint_specified'] = 'NO'
    
    return {
        'error_handling_score': score,  # 0-100
        'breakdown': details
    }


# Test it
if __name__ == "__main__":
    
    # Test prompt 1: No error handling
    bad_prompt = "Write a sorting function"
    
    print("Testing WEAK error handling:")
    print(f"'{bad_prompt}'")
    result1 = measure_error_handling(bad_prompt)
    print(f"Score: {result1['error_handling_score']}/100")
    print(f"Breakdown: {result1['breakdown']}")
    print()
    
    # Test prompt 2: Good error handling
    good_prompt = """
    Write a function to find maximum element in a list.
    
    Handle edge cases:
    - Empty list: raise ValueError
    - Single element: return that element
    - Negative numbers: should work fine
    - Duplicates: return first occurrence
    
    Do NOT assume list has elements.
    Must work with lists up to 1 million elements.
    """
    
    print("Testing STRONG error handling:")
    print(f"'{good_prompt}'")
    result2 = measure_error_handling(good_prompt)
    print(f"Score: {result2['error_handling_score']}/100")
    print(f"Breakdown: {result2['breakdown']}")