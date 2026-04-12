import numpy as np

class GaitMetrics:
    def __init__(self, motion_series):
        self.motion = np.array(motion_series)

    def average_motion(self):
        return float(np.mean(self.motion))

    def variability(self):
        return float(np.std(self.motion))

    def movement_frequency(self):
        diff = np.diff(self.motion)

        peaks = np.sum((diff[:-1] > 0) & (diff[1:] < 0))
        return int(peaks)