"""
Dimension 5: Testability & Verification
Measures how well the prompt specifies testing and verification
"""

import re


def measure_testability(prompt: str) -> dict:
    """
    Score testability in a prompt (0-100)
    
    Checks for:
    - Test cases provided?
    - Expected outputs specified?
    - Verification method clear?
    - Performance requirements?
    """
    
    score = 0
    details = {}
    
    # Check 1: Test cases/examples provided?
    test_keywords = [
        'test',
        'example',
        'case',
        'input',
        'output',
        '->',  # Arrow notation like: [1,2] -> [2,1]
        'expected'
    ]
    
    test_mentions = sum(1 for kw in test_keywords if kw in prompt.lower())
    
    if test_mentions >= 2:  # Need at least 2 mentions
        score += 25
        details['test_cases'] = f'{test_mentions} mentions'
    else:
        details['test_cases'] = 'NO'
    
    # Check 2: Expected output format specified?
    output_keywords = [
        'return',
        'output',
        'result',
        'should return',
        'yields'
    ]
    
    output_mentioned = any(kw in prompt.lower() for kw in output_keywords)
    
    if output_mentioned:
        score += 25
        details['output_format'] = 'YES'
    else:
        details['output_format'] = 'NO'
    
    # Check 3: Pass/fail criteria clear?
    criteria_keywords = [
        'pass',
        'fail',
        'correct',
        'valid',
        'success',
        'should work'
    ]
    
    criteria_mentioned = any(kw in prompt.lower() for kw in criteria_keywords)
    
    if criteria_mentioned:
        score += 25
        details['success_criteria'] = 'YES'
    else:
        details['success_criteria'] = 'NO'
    
    # Check 4: Performance requirements?
    perf_keywords = [
        'time',
        'space',
        'complexity',
        'o(',
        'efficient',
        'fast',
        'second',
        'millisecond'
    ]
    
    perf_mentioned = any(kw in prompt.lower() for kw in perf_keywords)
    
    if perf_mentioned:
        score += 25
        details['performance_specified'] = 'YES'
    else:
        details['performance_specified'] = 'NO'
    
    return {
        'testability_score': min(100, score),
        'breakdown': details
    }


# Test it
if __name__ == "__main__":
    
    # Test prompt 1: No testability info
    bad_prompt = "Write a sorting function"
    
    print("Testing WEAK testability:")
    print(f"'{bad_prompt}'")
    result1 = measure_testability(bad_prompt)
    print(f"Score: {result1['testability_score']}/100")
    print(f"Breakdown: {result1['breakdown']}")
    print()
    
    # Test prompt 2: Good testability
    good_prompt = """
    Write a function to reverse a list.
    
    Expected output: reversed list
    
    Test cases:
    - [1, 2, 3] -> [3, 2, 1]
    - [] -> []
    - [1] -> [1]
    
    Success criteria: function returns reversed list correctly
    
    Performance: must be O(n) time, O(1) space
    """
    
    print("Testing STRONG testability:")
    print(f"'{good_prompt}'")
    result2 = measure_testability(good_prompt)
    print(f"Score: {result2['testability_score']}/100")
    print(f"Breakdown: {result2['breakdown']}")