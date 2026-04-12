import numpy as np

class GaitAnalyzer:
    def __init__(self):
        self.step_count = 0
        self.positions = []

    def update(self, left_ankle, right_ankle):
        self.positions.append((left_ankle, right_ankle))

    def compute_step_length(self):
        distances = []
        for i in range(1, len(self.positions)):
            prev = self.positions[i-1]
            curr = self.positions[i]

            dist = np.linalg.norm(
                np.array(curr[0]) - np.array(prev[0])
            )
            distances.append(dist)

        return np.mean(distances) if distances else 0