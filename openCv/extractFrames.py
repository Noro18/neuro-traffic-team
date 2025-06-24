import cv2
import os

video_path = 'cctv_comoro.mp4'
output_folder = 'images'

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_rate = 5  # capture every 5th frame
frame_id = 0
img_id = 0

while cap.isOpened(): # wainhira nia video sei loke
    ret, frame = cap.read()
    if not ret:
        break
    if frame_id % frame_rate == 0:
        cv2.imwrite(f'{output_folder}/frame_{img_id}.jpg', frame)
        img_id += 1
    frame_id += 1

cap.release()
