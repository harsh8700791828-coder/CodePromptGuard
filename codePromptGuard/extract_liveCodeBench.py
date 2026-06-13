# extract_livecodebench.py
from datasets import load_dataset
from itertools import islice
import json
import os

print("Downloading LiveCodeBench 2024...")

ds = load_dataset(
    "livecodebench/code_generation_lite",
    split="test",
    trust_remote_code=True,
)

extracted = []
for i, item in enumerate(islice(ds, 40)):   # take 40 problems
    extracted.append({
        "id": f"lcb-{i+1:03d}",
        "source": "livecodebench",
        "title": item.get("question_title", f"Problem {i+1}"),
        "text": item.get("question_content", ""),
        "difficulty": item.get("difficulty", "unknown")
    })

os.makedirs("prompts", exist_ok=True)

with open("prompts/livecodebench_prompts.json", "w") as f:
    json.dump({"prompts": extracted}, f, indent=2)

print(f"Saved {len(extracted)} LiveCodeBench prompts")
