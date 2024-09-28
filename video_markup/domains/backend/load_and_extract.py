import cv2
from pydub import AudioSegment

def load_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise Exception(f"Cannot open video file {video_path}")
    return cap

def extract_frames(cap):
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Изменение размера кадра
        frame = cv2.resize(frame, (224, 224))
        frames.append(frame)
    cap.release()
    return frames
#%%

def extract_audio(video_path, audio_path):
    video = AudioSegment.from_file(video_path)
    video.export(audio_path, format="wav")