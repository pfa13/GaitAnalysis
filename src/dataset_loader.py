import kagglehub
import os

class DatasetLoader:
    def __init__(self):
        self.path = None

    def download(self):
        self.path = kagglehub.dataset_download("salmon1/demo-gait-video")

        print("Dataset path:", self.path)
        print("Files:", os.listdir(self.path))

        return self.path

    def list_files(self):
        return os.listdir(self.path)