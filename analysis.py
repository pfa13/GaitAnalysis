import csv
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("results/plots", exist_ok=True)

normal_motion, normal_var = [], []
sim_motion, sim_var = [], []

# 1. Read the existing data
with open('results/metrics.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        vid_name = row['video'].lower()
        motion = float(row['avg_motion'])
        variability = float(row['variability'])
        
        # Categorize based on file name
        if "parkinson" in vid_name or "simul" in vid_name or "disease" in vid_name:
            sim_motion.append(motion)
            sim_var.append(variability)
        else:
            normal_motion.append(motion)
            normal_var.append(variability)

# 2. Calculate Averages
avg_norm_mot = sum(normal_motion) / len(normal_motion) if normal_motion else 0
avg_norm_var = sum(normal_var) / len(normal_var) if normal_var else 0

avg_sim_mot = sum(sim_motion) / len(sim_motion) if sim_motion else 0
avg_sim_var = sum(sim_var) / len(sim_var) if sim_var else 0

print("--- RESULTS ---")
print(f"Normal Walk -> Avg Motion: {avg_norm_mot:.2f} | Variability: {avg_norm_var:.2f}")
print(f"Parkinson's -> Avg Motion: {avg_sim_mot:.2f} | Variability: {avg_sim_var:.2f}")

# 3. Generate Comparison Graph
labels = ['Avg Motion', 'Variability']
normal_means = [avg_norm_mot, avg_norm_var]
sim_means = [avg_sim_mot, avg_sim_var]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, normal_means, width, label='Normal')
ax.bar(x + width/2, sim_means, width, label="Simulated Parkinson's")

ax.set_ylabel('Scores')
ax.set_title('Gait Metrics: Normal vs Simulated Disease')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.savefig("results/plots/comparison_chart.png")
print("Chart saved to results/plots/comparison_chart.png")
