import os
import cv2
from ultralytics import YOLO


# Get the absolute path to best.pt
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best.pt")
VIDEO_PATH = os.path.join(BASE_DIR, "cctv_comoro.mp4")

def run_inference(video_source=VIDEO_PATH):
    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(video_source)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        annotated_frame = results[0].plot()
        ret, jpeg = cv2.imencode('.jpg', annotated_frame)
        if not ret:
            continue
        yield jpeg.tobytes()
    cap.release()