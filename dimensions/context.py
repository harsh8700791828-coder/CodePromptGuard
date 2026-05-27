"""
Dimension 4: Context & Dependency Management
Measures if prompt specifies dependencies, imports, and context clearly
"""

import re


def measure_context(prompt: str) -> dict:
    """
    Score context clarity in a prompt (0-100)
    
    Checks for:
    - Libraries/imports mentioned?
    - Language version specified?
    - Data structures explained?
    - Assumptions stated?
    - Pre/post conditions?
    """
    
    score = 0
    details = {}
    
    # Check 1: Libraries/imports mentioned?
    import_keywords = [
        'import',
        'library',
        'module',
        'package',
        'require',
        'use this',
        'numpy',
        'pandas',
        'requests'
    ]
    
    import_mentions = sum(1 for kw in import_keywords if kw in prompt.lower())
    
    if import_mentions >= 1:
        score += 20
        details['dependencies_mentioned'] = f'{import_mentions} found'
    else:
        details['dependencies_mentioned'] = 'NO'
    
    # Check 2: Language/version specified?
    version_keywords = [
        'python',
        'version',
        '3.8',
        '3.9',
        '3.10',
        '3.11',
        'java',
        'javascript'
    ]
    
    version_mentioned = any(kw in prompt.lower() for kw in version_keywords)
    
    if version_mentioned:
        score += 20
        details['language_version'] = 'YES'
    else:
        details['language_version'] = 'NO'
    
    # Check 3: Data structures explained?
    datastructure_keywords = [
        'list',
        'dict',
        'set',
        'array',
        'matrix',
        'graph',
        'tree',
        'tuple',
        'queue',
        'stack'
    ]
    
    datastructure_mentions = sum(1 for ds in datastructure_keywords if ds in prompt.lower())
    
    if datastructure_mentions >= 1:
        score += 20
        details['datastructures_mentioned'] = f'{datastructure_mentions} found'
    else:
        details['datastructures_mentioned'] = 'NO'
    
    # Check 4: Assumptions/preconditions stated?
    assumption_keywords = [
        'assume',
        'given',
        'suppose',
        'precondition',
        'prerequisite',
        'requires'
    ]
    
    assumption_mentioned = any(kw in prompt.lower() for kw in assumption_keywords)
    
    if assumption_mentioned:
        score += 20
        details['assumptions_stated'] = 'YES'
    else:
        details['assumptions_stated'] = 'NO'
    
    # Check 5: Environment or setup mentioned?
    setup_keywords = [
        'setup',
        'install',
        'environment',
        'python path',
        'working directory'
    ]
    
    setup_mentioned = any(kw in prompt.lower() for kw in setup_keywords)
    
    if setup_mentioned:
        score += 20
        details['setup_instructions'] = 'YES'
    else:
        details['setup_instructions'] = 'NO'
    
    return {
        'context_score': min(100, score),  # Clamp to 100
        'breakdown': details
    }


# Test it
if __name__ == "__main__":
    
    # Test prompt 1: No context
    bad_prompt = "Write a web scraper"
    
    print("Testing WEAK context:")
    print(f"'{bad_prompt}'")
    result1 = measure_context(bad_prompt)
    print(f"Score: {result1['context_score']}/100")
    print(f"Breakdown: {result1['breakdown']}")
    print()
    
    # Test prompt 2: Good context
    good_prompt = """
    Write a web scraper in Python 3.10.
    
    Dependencies:
    - requests library (for HTTP)
    - BeautifulSoup4 (for HTML parsing)
    
    Input: URL (string)
    Output: dict with {title, paragraphs[], links[]}
    
    Assume:
    - URL is valid
    - Page is valid HTML
    - No authentication required
    
    Data structures used:
    - list for paragraphs
    - list for links
    - dict for output
    """
    
    print("Testing STRONG context:")
    print(f"'{good_prompt}'")
    result2 = measure_context(good_prompt)
    print(f"Score: {result2['context_score']}/100")
    print(f"Breakdown: {result2['breakdown']}")