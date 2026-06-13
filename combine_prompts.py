# combine_prompts.py
import json

all_prompts = []

# Load LiveCodeBench (40)
with open('prompts/livecodebench_prompts.json', 'r') as f:
    lcb = json.load(f)
all_prompts.extend(lcb['prompts'])
print(f"✅ LiveCodeBench: {len(lcb['prompts'])} prompts")

# Load StudentEval (downloaded)
with open('prompts/studenteval_prompts.json', 'r') as f:
    se = json.load(f)
all_prompts.extend(se['prompts'])
print(f"✅ StudentEval downloaded: {len(se['prompts'])} prompts")

# Custom Indian prompts (5)
custom = [
    {"id": "custom-001", "source": "custom", "title": "GST Calculator", "text": "Write function to calculate GST. Input: price, rate (5/12/18/28). Output: {subtotal, gst, total}. Handle: negative price raises error, proper rounding to 2 decimal places."},
    {"id": "custom-002", "source": "custom", "title": "Aadhaar Validator", "text": "Validate Aadhaar number (12 digits). Check: format, not all zeros, Verhoeff algorithm for check digit. Return: {valid: bool, normalized: str, errors: list}."},
    {"id": "custom-003", "source": "custom", "title": "PAN Validator", "text": "Validate Indian PAN format (AAAAA9999A). Return validation result with detailed error message if invalid."},
    {"id": "custom-004", "source": "custom", "title": "Phone Validator", "text": "Validate Indian mobile number (10 digits, starts with 6-9). Handle +91 prefix. Return standardized format or error."},
    {"id": "custom-005", "source": "custom", "title": "Pincode Validator", "text": "Validate Indian pincode (exactly 6 digits, no special characters). Return {valid: bool, error: str}."}
]
all_prompts.extend(custom)
print(f"✅ Custom Indian: {len(custom)} prompts")

# StudentEval-style manual prompts (4) - novice prompts from paper examples
studenteval_manual = [
    {"id": "student-manual-001", "source": "studenteval", "title": "Reverse Words", "text": "reverse the words in a sentence"},
    {"id": "student-manual-002", "source": "studenteval", "title": "Count Words", "text": "count how many words are in the string"},
    {"id": "student-manual-003", "source": "studenteval", "title": "Find Duplicates", "text": "find all duplicate numbers in a list"},
    {"id": "student-manual-004", "source": "studenteval", "title": "Check Sorted", "text": "check if a list is sorted"},
]
all_prompts.extend(studenteval_manual)
print(f"✅ StudentEval manual: {len(studenteval_manual)} prompts")

# Save combined
with open('prompts/combined_prompts.json', 'w') as f:
    json.dump({"prompts": all_prompts}, f, indent=2)

print(f"\n✅ TOTAL: {len(all_prompts)} prompts saved to prompts/combined_prompts.json")

# Show breakdown by source
sources = {}
for p in all_prompts:
    s = p['source']
    sources[s] = sources.get(s, 0) + 1
for s, c in sources.items():
    print(f"   {s}: {c}")