iimport csv

data = []
with open('results/metrics.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# 1. Calculate Baseline (using Motion AND Variability)
baselines = {}
for row in data:
    p = row['participant']
    if p not in baselines:
        baselines[p] = {'motions': [], 'vars': []}
    if "Experiment_1" in row['video']:
        baselines[p]['motions'].append(float(row['avg_motion']))
        baselines[p]['vars'].append(float(row['variability']))

for p in baselines:
    baselines[p]['base_mot'] = sum(baselines[p]['motions']) / len(baselines[p]['motions'])
    baselines[p]['base_var'] = sum(baselines[p]['vars']) / len(baselines[p]['vars'])

# 2. Test with Improved Logic
correct = 0
total = len(data)

print(f"{'Video Run':<15} | {'Actual':<15} | {'Predicted':<15} | {'Match'}")
print("-" * 60)

for row in data:
    p = row['participant']
    actual = "Normal" if "Experiment_1" in row['video'] else "Simulated"
    mot = float(row['avg_motion'])
    var = float(row['variability'])
    
    # IMPROVED LOGIC: 
    # Calculate how far off the current walk is from their normal baseline (percentages)
    mot_diff = abs(mot - baselines[p]['base_mot']) / baselines[p]['base_mot']
    var_diff = (var - baselines[p]['base_var']) / baselines[p]['base_var']
    
    # If variability jumps by more than 15% OR overall motion changes by more than 25%, it's abnormal.
    if mot_diff > 0.25 or var_diff > 0.15:
        predicted = "Simulated"
    else:
        predicted = "Normal"
        
    match = "✅" if actual == predicted else "❌"
    if actual == predicted: correct += 1
        
    vid_short = row['video'].split('\\')[-1][:12]
    print(f"{vid_short:<15} | {actual:<15} | {predicted:<15} | {match}")

print("-" * 60)
print(f"IMPROVED Accuracy: {correct}/{total} ({(correct/total)*100:.1f}%)")
