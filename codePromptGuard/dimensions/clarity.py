"""
Dimension 1: Clarity & Specificity
Measures how clearly the prompt specifies what to build
"""

import re


def measure_clarity(prompt: str) -> dict:
    """
    Score clarity of a prompt (0-100)
    
    Checks for:
    - Input/output format specified?
    - Constraints mentioned?
    - Examples provided?
    - Error conditions addressed?
    """
    
    score = 0
    details = {}
    
    # Check 1: Is input/output format mentioned?
    has_io_format = bool(re.search(
        r'(input|output|format|returns?|accept)',
        prompt,
        re.IGNORECASE
    ))
    
    if has_io_format:
        score += 25  # Important
        details['input_output_format'] = 'YES'
    else:
        details['input_output_format'] = 'NO'
    
    # Check 2: Are constraints mentioned?
    has_constraints = bool(re.search(
        r'(constraint|limit|time|space|complexity|efficient)',
        prompt,
        re.IGNORECASE
    ))
    
    if has_constraints:
        score += 25  # Important
        details['constraints_specified'] = 'YES'
    else:
        details['constraints_specified'] = 'NO'
    
    # Check 3: Are examples provided?
    has_examples = bool(re.search(
        r'(example|e\.g|test case|instance|for instance)',
        prompt,
        re.IGNORECASE
    ))
    
    if has_examples:
        score += 25  # Very important
        details['examples_provided'] = 'YES'
    else:
        details['examples_provided'] = 'NO'
    
    # Check 4: Is error handling mentioned?
    has_error_handling = bool(re.search(
        r'(error|exception|invalid|invalid input|edge case)',
        prompt,
        re.IGNORECASE
    ))
    
    if has_error_handling:
        score += 25  # Important
        details['error_handling_mentioned'] = 'YES'
    else:
        details['error_handling_mentioned'] = 'NO'
    
    return {
        'clarity_score': score,  # 0-100
        'breakdown': details
    }


# Test it
if __name__ == "__main__":
    
    # Test prompt 1: Poor clarity
    bad_prompt = "Write a function to sort things"
    
    print("Testing BAD prompt:")
    print(f"'{bad_prompt}'")
    result1 = measure_clarity(bad_prompt)
    print(f"Score: {result1['clarity_score']}/100")
    print(f"Breakdown: {result1['breakdown']}")
    print()
    
    # Test prompt 2: Good clarity
    good_prompt = """
    Write a function to sort an array of integers in ascending order.
    
    Input: list of integers
    Output: same list, sorted
    
    Constraints:
    - Must be O(n log n) or better
    - In-place sorting preferred
    
    Examples:
    sort([3, 1, 4, 1, 5]) -> [1, 1, 3, 4, 5]
    sort([]) -> []
    sort([1]) -> [1]
    
    Handle edge cases: empty list, duplicate elements, negative numbers
    """
    
    print("Testing GOOD prompt:")
    print(f"'{good_prompt}'")
    result2 = measure_clarity(good_prompt)
    print(f"Score: {result2['clarity_score']}/100")
    print(f"Breakdown: {result2['breakdown']}")