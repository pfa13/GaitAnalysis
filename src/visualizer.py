import matplotlib.pyplot as plt

class Visualizer:
    def plot_motion(self, motion):
        plt.figure()
        plt.plot(motion)
        plt.title("Gait Motion Signal")
        plt.xlabel("Frame")
        plt.ylabel("Motion Intensity")

        plt.savefig("results/plots/motion.png")
        plt.show()