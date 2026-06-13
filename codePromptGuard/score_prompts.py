import json
from dimensions.health_score import compute_overall_health_score

# Load combined prompts
with open('prompts/combined_prompts.json', 'r') as f:
    prompts_data = json.load(f)

prompts = prompts_data['prompts']

print("=" * 80)
print(f"SCORING {len(prompts)} COMBINED PROMPTS")
print("(LiveCodeBench + StudentEval + Custom Indian)")
print("=" * 80)

results = []

for prompt in prompts:
    prompt_id = prompt['id']
    prompt_text = prompt['text']
    source = prompt['source']
    title = prompt['title']

    score_result = compute_overall_health_score(prompt_text)
    overall_score = score_result['overall_health_score']

    result = {
        'id': prompt_id,
        'title': title,
        'source': source,
        'prompt': prompt_text,
        'overall_health': overall_score,
        'breakdown': score_result['breakdown']
    }
    results.append(result)

    print(f"{prompt_id}: {title} | Source: {source} | Score: {overall_score}/100")

# Save results
import os
os.makedirs('results', exist_ok=True)
with open('results/combined_prompt_scores.json', 'w') as f:
    json.dump(results, f, indent=2)

print("\n" + "=" * 80)
scores = [r['overall_health'] for r in results]
print(f"STATISTICS:")
print(f"  Total: {len(scores)} prompts")
print(f"  Average: {sum(scores)/len(scores):.1f}/100")
print(f"  Min: {min(scores)}/100")
print(f"  Max: {max(scores)}/100")

print(f"\nBY SOURCE:")
sources = {}
for r in results:
    s = r['source']
    if s not in sources:
        sources[s] = []
    sources[s].append(r['overall_health'])
for s, sc in sources.items():
    # add this temporarily to score_prompts.py, inside the loop
    if prompt_id.startswith('custom'):
     print(f"  >> {prompt_id} | Type: {score_result['prompt_type']} | Breakdown: {score_result['breakdown']}")
    print(f"  {s}: {len(sc)} prompts, avg {sum(sc)/len(sc):.1f}/100")

print("=" * 80)
print(f"{prompt_id}: {title} | Type: {score_result['prompt_type']} | Score: {overall_score}/100")
print("Saved to: results/combined_prompt_scores.json")