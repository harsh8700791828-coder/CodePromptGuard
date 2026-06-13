"""
Test our clarity scorer on 5 sample prompts
"""

from clarity import measure_clarity


# Real prompts we'll use in our research
test_prompts = {
    'prompt_1': """
    Write a function to find if a number is prime.
    """,
    
    'prompt_2': """
    Write a function to check if a number is prime.
    
    Input: positive integer n
    Output: True if n is prime, False otherwise
    """,
    
    'prompt_3': """
    Write a function is_prime(n) that returns True if n is prime, False otherwise.
    
    Input: positive integer n (1 <= n <= 10^9)
    Output: boolean
    
    Constraints:
    - Must be O(sqrt(n)) or better
    - Handle edge cases: n=1, n=2
    
    Examples:
    is_prime(2) -> True
    is_prime(3) -> True
    is_prime(4) -> False
    is_prime(17) -> True
    """,
    
    'prompt_4': """
    Implement binary search on a sorted array.
    """,
    
    'prompt_5': """
    Implement binary search function.
    
    Input: sorted list of integers, target value
    Output: index of target (-1 if not found)
    
    Time complexity: O(log n)
    Space complexity: O(1)
    
    Examples:
    binary_search([1,3,5,7], 5) -> 2
    binary_search([1,3,5], 4) -> -1
    
    Handle: empty list, list with one element, duplicates
    """
}

# Test each prompt
print("=" * 60)
print("CLARITY SCORING TEST")
print("=" * 60)

for prompt_name, prompt_text in test_prompts.items():
    result = measure_clarity(prompt_text)
    score = result['clarity_score']
    
    print(f"\n{prompt_name}:")
    print(f"  Prompt: {prompt_text[:50]}...")
    print(f"  CLARITY SCORE: {score}/100")
    print(f"  Details: {result['breakdown']}")

print("\n" + "=" * 60)