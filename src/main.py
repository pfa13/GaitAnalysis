import cv2
import os

from dataset_loader import DatasetLoader
from motion_detector import MotionDetector
from gait_metrics import GaitMetrics
from visualizer import Visualizer

def find_video_file(root_path):
    for dirpath, _, filenames in os.walk(root_path):
        for file in filenames:
            if file.endswith(".mp4"):
                return os.path.join(dirpath, file)
    return None

# 1. LOAD DATASET
loader = DatasetLoader()
dataset_path = loader.download()

files = loader.list_files()

video_file = find_video_file(dataset_path)

if video_file is None:
    raise Exception("No video file found in dataset")

# 2. PROCESS VIDEO
cap = cv2.VideoCapture(video_file)

detector = MotionDetector()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    motion = detector.process_frame(frame)

    cv2.putText(
        frame,
        f"Motion: {motion:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Gait Analysis", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

# 3. METRICS
motion_series = detector.get_motion_series()

metrics = GaitMetrics(motion_series)

print("\n📊 RESULTS")
print("Average motion:", metrics.average_motion())
print("Variability:", metrics.variability())
print("Movement frequency:", metrics.movement_frequency())

# -------------------------
# 4. VISUALIZATION
# -------------------------
viz = Visualizer()
viz.plot_motion(motion_series)