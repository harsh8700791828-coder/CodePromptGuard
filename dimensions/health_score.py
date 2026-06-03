"""
health_score.py — Weighted multi-dimension prompt health scorer.
Weights adjust based on detected prompt type.
"""

from dimensions.clarity import score_clarity
from dimensions.error_handling import score_error_handling
from dimensions.security import score_security
from dimensions.context import score_context
from dimensions.testability import score_testability
from dimensions.edge_case import score_edge_cases


def detect_prompt_type(text):
    """
    Detect whether prompt is algorithm-focused or software-engineering focused.
    This matters because dimensions like security are irrelevant for pure algorithms.
    """
    text_lower = text.lower()

    algorithm_signals = [
        'array', 'sort', 'search', 'tree', 'graph', 'matrix',
        'palindrome', 'substring', 'subarray', 'permutation',
        'traversal', 'bfs', 'dfs', 'dynamic programming', 'dp',
        'binary search', 'linked list', 'stack', 'queue',
        'gcd', 'fibonacci', 'factorial', 'prime',
        'minimum', 'maximum', 'optimal', 'count', 'find the'
    ]

    software_signals = [
    'api', 'endpoint', 'database', 'authentication', 'sql',
    'file', 'http', 'request', 'response', 'user input',
    'web', 'server', 'client', 'password', 'token',
    'validate', 'sanitize', 'injection', 'session',
    'validator', 'validation', 'format', 'phone', 'pincode',
    'aadhaar', 'pan', 'gst', 'mobile', 'standardized',
    'return {', 'valid:', 'errors:', 'normalized'
]

    algo_score = sum(1 for s in algorithm_signals if s in text_lower)
    soft_score = sum(1 for s in software_signals if s in text_lower)

    if algo_score > soft_score:
        return 'algorithm'
    elif soft_score > algo_score:
        return 'software'
    else:
        return 'general'


def get_weights(prompt_type):
    """
    Return dimension weights based on prompt type.
    Weights sum to 1.0.
    """
    if prompt_type == 'algorithm':
        # For algorithm problems: clarity and edge cases matter most
        # Security is mostly irrelevant — don't punish for it
        return {
            'clarity':        0.30,
            'error_handling': 0.15,
            'security':       0.05,  # low weight — not relevant
            'context':        0.20,
            'testability':    0.20,
            'edge_cases':     0.10
        }
    elif prompt_type == 'software':
        # For software/API problems: security and error handling matter a lot
        return {
            'clarity':        0.20,
            'error_handling': 0.20,
            'security':       0.25,  # high weight
            'context':        0.15,
            'testability':    0.10,
            'edge_cases':     0.10
        }
    else:
        # General: balanced weights
        return {
            'clarity':        0.25,
            'error_handling': 0.20,
            'security':       0.10,
            'context':        0.20,
            'testability':    0.15,
            'edge_cases':     0.10
        }


def compute_overall_health_score(prompt_text):
    """
    Main scoring function. Returns overall score + full breakdown.
    """

    # Detect type
    prompt_type = detect_prompt_type(prompt_text)

    # Get dimension scores
    clarity        = score_clarity(prompt_text)['score']
    error_handling = score_error_handling(prompt_text)['score']
    security       = score_security(prompt_text)['score']
    context        = score_context(prompt_text)['score']
    testability    = score_testability(prompt_text)['score']
    edge_cases     = score_edge_cases(prompt_text)['score']

    # Get weights
    weights = get_weights(prompt_type)

    # Weighted average
    overall = (
        clarity        * weights['clarity']        +
        error_handling * weights['error_handling'] +
        security       * weights['security']       +
        context        * weights['context']        +
        testability    * weights['testability']    +
        edge_cases     * weights['edge_cases']
    )

    return {
        'overall_health_score': round(overall, 1),
        'prompt_type': prompt_type,
        'breakdown': {
            'clarity':        clarity,
            'error_handling': error_handling,
            'security':       security,
            'context':        context,
            'testability':    testability,
            'edge_cases':     edge_cases
        },
        'weights_used': weights
    }