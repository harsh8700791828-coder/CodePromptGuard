"""
Dimension 3: Security & Vulnerability Awareness
Measures if prompt specifies secure coding practices
"""

import re


def measure_security(prompt: str) -> dict:
    """
    Score security awareness in a prompt (0-100)
    
    Checks for:
    - Security keywords mentioned?
    - Unsafe operations forbidden?
    - Input validation mentioned?
    - Safe practices mentioned?
    """
    
    score = 0
    details = {}
    
    # Check 1: Security keywords present?
    security_keywords = [
        'secure',
        'safety',
        'validate',
        'sanitize',
        'protect',
        'safe',
        'security'
    ]
    
    security_mentions = sum(1 for kw in security_keywords if kw in prompt.lower())
    
    if security_mentions >= 1:
        score += 25
        details['security_keywords'] = f'{security_mentions} found'
    else:
        details['security_keywords'] = 'NO'
    
    # Check 2: Forbidden operations NOT mentioned (good!)
    forbidden_operations = [
        'eval',
        'exec',
        'pickle',
        'shell=true',
        'os.system',
        '__import__'
    ]
    
    forbidden_found = sum(1 for fo in forbidden_operations if fo in prompt.lower())
    
    if forbidden_found == 0:
        score += 25  # Good: doesn't mention dangerous stuff
        details['unsafe_operations'] = 'NONE (good!)'
    else:
        score -= forbidden_found * 10  # Penalty for mentioning them
        details['unsafe_operations'] = f'{forbidden_found} mentioned (bad!)'
    
    # Check 3: Input validation mentioned?
    has_validation = bool(re.search(
        r'(validate|check|verify|input validation|sanitize|clean)',
        prompt,
        re.IGNORECASE
    ))
    
    if has_validation:
        score += 25
        details['input_validation'] = 'YES'
    else:
        details['input_validation'] = 'NO'
    
    # Check 4: Safe libraries or methods mentioned?
    safe_practices = [
        'hashlib',
        'secrets',
        'jwt',
        'encryption',
        'hashing',
        'https',
        'ssl',
        'parameterized'
    ]
    
    safe_mentions = sum(1 for sp in safe_practices if sp in prompt.lower())
    
    if safe_mentions >= 1:
        score += 25
        details['safe_practices'] = f'{safe_mentions} found'
    else:
        details['safe_practices'] = 'NO'
    
    return {
        'security_score': max(0, min(100, score)),  # Clamp 0-100
        'breakdown': details
    }


# Test it
if __name__ == "__main__":
    
    # Test prompt 1: No security awareness
    bad_prompt = "Write a function that executes user input as code"
    
    print("Testing WEAK security:")
    print(f"'{bad_prompt}'")
    result1 = measure_security(bad_prompt)
    print(f"Score: {result1['security_score']}/100")
    print(f"Breakdown: {result1['breakdown']}")
    print()
    
    # Test prompt 2: Good security awareness
    good_prompt = """
    Write a function to hash a password.
    
    Security requirements:
    - Use hashlib, NOT plain text
    - Validate input (string, non-empty)
    - Add salt for security
    - Use bcrypt or PBKDF2 for password hashing
    
    Do NOT use eval() or pickle
    Do NOT store plain text passwords
    Sanitize all user input
    """
    
    print("Testing STRONG security:")
    print(f"'{good_prompt}'")
    result2 = measure_security(good_prompt)
    print(f"Score: {result2['security_score']}/100")
    print(f"Breakdown: {result2['breakdown']}")