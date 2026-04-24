import csv

data = []
with open('results/metrics.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# 1. Calculate the "Normal" baseline for each participant
baselines = {}
for row in data:
    p = row['participant']
    if p not in baselines:
        baselines[p] = {'norm_motions': [], 'norm_freqs': []}
    
    # We use Experiment 1 as their true normal baseline
    if "Experiment_1" in row['video']:
        baselines[p]['norm_motions'].append(float(row['avg_motion']))
        baselines[p]['norm_freqs'].append(float(row['frequency']))

for p in baselines:
    baselines[p]['base_mot'] = sum(baselines[p]['norm_motions']) / len(baselines[p]['norm_motions'])
    baselines[p]['base_freq'] = sum(baselines[p]['norm_freqs']) / len(baselines[p]['norm_freqs'])

# 2. Test every video and make a prediction
correct = 0
total = len(data)

print(f"{'Video Run':<15} | {'Actual':<15} | {'Predicted':<15} | {'Match'}")
print("-" * 60)

for row in data:
    p = row['participant']
    actual = "Normal" if "Experiment_1" in row['video'] else "Simulated"
    
    mot = float(row['avg_motion'])
    freq = float(row['frequency'])
    
    # PREDICTION LOGIC: 
    # If their motion drops below 90% of their normal baseline OR frequency changes wildly, predict they are simulating
    if mot < (baselines[p]['base_mot'] * 0.90) or freq > (baselines[p]['base_freq'] * 1.5):
        predicted = "Simulated"
    else:
        predicted = "Normal"
        
    if actual == predicted:
        correct += 1
        match = "✅"
    else:
        match = "❌"
        
    # Print a short name for the video to fit the table
    vid_short = row['video'].split('\\')[-1][:12] 
    
    print(f"{vid_short:<15} | {actual:<15} | {predicted:<15} | {match}")

print("-" * 60)
print(f"Prediction Accuracy: {correct}/{total} ({(correct/total)*100:.1f}%)")
