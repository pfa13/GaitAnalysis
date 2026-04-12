def get_landmark_coords(landmarks, index, width, height):
    lm = landmarks[index]
    return int(lm.x * width), int(lm.y * height)