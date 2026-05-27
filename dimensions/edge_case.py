"""
Dimension 6: Edge Case Coverage
Measures how well the prompt covers edge cases
"""

import re


def measure_edge_case_coverage(prompt: str) -> dict:
    """
    Score edge case coverage in a prompt (0-100)
    
    Checks for:
    - Empty/null cases?
    - Boundary values?
    - Large inputs?
    - Special values?
    """
    
    score = 0
    details = {}
    
    # Check 1: Empty/null cases mentioned?
    empty_keywords = [
        'empty',
        'null',
        'none',
        'zero length',
        'blank',
        'no elements'
    ]
    
    empty_mentioned = any(kw in prompt.lower() for kw in empty_keywords)
    
    if empty_mentioned:
        score += 16
        details['empty_null_cases'] = 'YES'
    else:
        details['empty_null_cases'] = 'NO'
    
    # Check 2: Single/small inputs mentioned?
    small_keywords = [
        'single',
        'one element',
        'size 1',
        'single item'
    ]
    
    small_mentioned = any(kw in prompt.lower() for kw in small_keywords)
    
    if small_mentioned:
        score += 16
        details['single_element_case'] = 'YES'
    else:
        details['single_element_case'] = 'NO'
    
    # Check 3: Large inputs mentioned?
    large_keywords = [
        'large',
        'million',
        'billion',
        '10^6',
        '10^9',
        'massive'
    ]
    
    large_mentioned = any(kw in prompt.lower() for kw in large_keywords)
    
    if large_mentioned:
        score += 17
        details['large_input_case'] = 'YES'
    else:
        details['large_input_case'] = 'NO'
    
    # Check 4: Boundary values mentioned?
    boundary_keywords = [
        'boundary',
        'maximum',
        'minimum',
        'limit',
        'extreme',
        'negative',
        'zero',
        'float'
    ]
    
    boundary_mentions = sum(1 for kw in boundary_keywords if kw in prompt.lower())
    
    if boundary_mentions >= 2:
        score += 17
        details['boundary_values'] = f'{boundary_mentions} found'
    else:
        details['boundary_values'] = 'NO'
    
    # Check 5: Special cases mentioned?
    special_keywords = [
        'duplicate',
        'special',
        'unicode',
        'emoji',
        'whitespace',
        'repeated'
    ]
    
    special_mentioned = any(kw in prompt.lower() for kw in special_keywords)
    
    if special_mentioned:
        score += 18
        details['special_cases'] = 'YES'
    else:
        details['special_cases'] = 'NO'
    
    return {
        'edge_case_score': min(100, score),
        'breakdown': details
    }


# Test it
if __name__ == "__main__":
    
    # Test prompt 1: No edge case handling
    bad_prompt = "Write a function to find max element"
    
    print("Testing WEAK edge case coverage:")
    print(f"'{bad_prompt}'")
    result1 = measure_edge_case_coverage(bad_prompt)
    print(f"Score: {result1['edge_case_score']}/100")
    print(f"Breakdown: {result1['breakdown']}")
    print()
    
    # Test prompt 2: Good edge case handling
    good_prompt = """
    Write a function to find max element in array.
    
    Handle edge cases:
    - Empty array: raise ValueError
    - Single element: return that element
    - Negative numbers: should work fine
    - Large arrays (1 million elements): must be efficient
    - Duplicate maximum values: return first occurrence
    - Floating point numbers: compare properly
    """
    
    print("Testing STRONG edge case coverage:")
    print(f"'{good_prompt}'")
    result2 = measure_edge_case_coverage(good_prompt)
    print(f"Score: {result2['edge_case_score']}/100")
    print(f"Breakdown: {result2['breakdown']}")