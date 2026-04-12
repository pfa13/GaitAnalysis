import cv2
from pose_detector import PoseDetector
from gait_metrics import GaitAnalyzer
from utils import get_landmark_coords
import mediapipe as mp

mp_pose = mp.solutions.pose

cap = cv2.VideoCapture("data/walking.mp4")

detector = PoseDetector()
analyzer = GaitAnalyzer()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    result = detector.process_frame(frame)

    if result.pose_landmarks:
        h, w, _ = frame.shape
        lm = result.pose_landmarks.landmark

        left_ankle = get_landmark_coords(lm, mp_pose.PoseLandmark.LEFT_ANKLE, w, h)
        right_ankle = get_landmark_coords(lm, mp_pose.PoseLandmark.RIGHT_ANKLE, w, h)

        analyzer.update(left_ankle, right_ankle)

    frame = detector.draw_landmarks(frame, result)

    cv2.imshow("Gait Analysis", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

print("Average step length:", analyzer.compute_step_length())