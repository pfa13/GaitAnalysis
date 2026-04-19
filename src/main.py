import cv2
import matplotlib.pyplot as plt

from src.dataset_loader import DatasetLoader
from src.motion_detector import MotionDetector
from src.gait_metrics import GaitMetrics
from src.exporter import Exporter

import os
os.makedirs("results/plots", exist_ok=True)

def get_participant(video_path):
    parts = video_path.split("\\")
    for p in parts:
        if "participant" in p.lower():
            return p
    return "unknown"

# LOAD DATASET
loader = DatasetLoader()
dataset_path = loader.download()
video_files = loader.find_all_videos()

print(f"Found {len(video_files)} videos")

all_results = []

# PROCESS ALL VIDEOS
for video_file in video_files:
    print(f"\nProcessing: {video_file}")

    cap = cv2.VideoCapture(video_file)
    detector = MotionDetector()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detector.process_frame(frame)

    cap.release()

    motion_series = detector.get_motion_series()

    if len(motion_series) == 0:
        continue

    metrics = GaitMetrics(motion_series)

    # identify participant
    participant = get_participant(video_file)

    result = {
        "video": video_file,
        "participant": participant,
        "avg_motion": metrics.average_motion(),
        "variability": metrics.variability(),
        "frequency": metrics.movement_frequency()
    }

    all_results.append(result)

# EXPORT CSV
exporter = Exporter()
exporter.save_to_csv(all_results)

# ANALYSIS
print("\n📊 SUMMARY ANALYSIS\n")

avg_motion = [r["avg_motion"] for r in all_results]
variability = [r["variability"] for r in all_results]
frequency = [r["frequency"] for r in all_results]

print("Average motion (global):", sum(avg_motion)/len(avg_motion))
print("Average variability:", sum(variability)/len(variability))
print("Average frequency:", sum(frequency)/len(frequency))

# PLOTS
plt.figure()
plt.bar(range(len(avg_motion)), avg_motion)
plt.title("Average Motion per Video")
plt.xlabel("Video Index")
plt.ylabel("Motion")
plt.savefig("results/plots/avg_motion.png")

plt.figure()
plt.bar(range(len(variability)), variability)
plt.title("Variability per Video")
plt.xlabel("Video Index")
plt.ylabel("Variability")
plt.savefig("results/plots/variability.png")

plt.figure()
plt.bar(range(len(frequency)), frequency)
plt.title("Frequency per Video")
plt.xlabel("Video Index")
plt.ylabel("Frequency")
plt.savefig("results/plots/frequency.png")

plt.show()