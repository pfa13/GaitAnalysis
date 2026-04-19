import os

class DatasetLoader:
    def __init__(self):
        self.path = None

    def download(self):
        import kagglehub
        self.path = kagglehub.dataset_download("salmon1/demo-gait-video")
        return self.path

    def find_all_videos(self):
        video_files = []

        for dirpath, _, filenames in os.walk(self.path):
            for file in filenames:
                if file.endswith(".mp4"):
                    full_path = os.path.join(dirpath, file)
                    video_files.append(full_path)

        return video_files