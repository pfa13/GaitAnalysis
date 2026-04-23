import csv
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("results/plots", exist_ok=True)

exp1_motion, exp1_var = [], []
exp2_motion, exp2_var = [], []

# 1. Read the existing data
with open('results/metrics.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        vid_name = row['video']
        motion = float(row['avg_motion'])
        variability = float(row['variability'])
        
        # Categorize based on Experiment folder
        if "Experiment_1" in vid_name:
            exp1_motion.append(motion)
            exp1_var.append(variability)
        elif "Experiment_2" in vid_name:
            exp2_motion.append(motion)
            exp2_var.append(variability)

# 2. Calculate Averages
avg_e1_mot = sum(exp1_motion) / len(exp1_motion) if exp1_motion else 0
avg_e1_var = sum(exp1_var) / len(exp1_var) if exp1_var else 0

avg_e2_mot = sum(exp2_motion) / len(exp2_motion) if exp2_motion else 0
avg_e2_var = sum(exp2_var) / len(exp2_var) if exp2_var else 0

print("--- RESULTS ---")
print(f"Experiment 1 (Normal) -> Avg Motion: {avg_e1_mot:.2f} | Variability: {avg_e1_var:.2f}")
print(f"Experiment 2 (Simulated) -> Avg Motion: {avg_e2_mot:.2f} | Variability: {avg_e2_var:.2f}")

# 3. Generate Comparison Graph
labels = ['Avg Motion', 'Variability']
e1_means = [avg_e1_mot, avg_e1_var]
e2_means = [avg_e2_mot, avg_e2_var]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, e1_means, width, label='Experiment 1 (Normal)')
ax.bar(x + width/2, e2_means, width, label="Experiment 2 (Simulated)")

ax.set_ylabel('Scores')
ax.set_title('Gait Metrics: Normal vs Simulated Pathological Gait')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.savefig("results/plots/comparison_chart.png")
print("Chart saved to results/plots/comparison_chart.png")
