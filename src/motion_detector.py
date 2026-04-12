import cv2
import numpy as np

class MotionDetector:
    def __init__(self):
        self.prev_gray = None
        self.motion_values = []

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if self.prev_gray is None:
            self.prev_gray = gray
            return 0

        diff = cv2.absdiff(self.prev_gray, gray)
        score = np.sum(diff) / diff.size

        self.prev_gray = gray
        self.motion_values.append(score)

        return score

    def get_motion_series(self):
        return self.motion_values