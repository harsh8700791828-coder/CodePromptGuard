from dimensions.health_score import detect_prompt_type, compute_overall_health_score

prompts = {
    'Phone Validator': 'Validate Indian mobile number (10 digits, starts with 6-9). Handle +91 prefix. Return standardized format or error.',
    'Pincode Validator': 'Validate Indian pincode (exactly 6 digits, no special characters). Return {valid: bool, error: str}.',
    'GST Calculator': 'Write function to calculate GST. Input: price, rate (5/12/18/28). Output: {subtotal, gst, total}. Handle: negative price raises error, proper rounding to 2 decimal places.'
}

for name, text in prompts.items():
    ptype = detect_prompt_type(text)
    result = compute_overall_health_score(text)
    print(f"{name}:")
    print(f"  Type detected: {ptype}")
    print(f"  Score: {result['overall_health_score']}")
    print(f"  Breakdown: {result['breakdown']}")
    print(f"  Weights: {result['weights_used']}")
    print()