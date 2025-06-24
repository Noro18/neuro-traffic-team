import cv2
from ultralytics import YOLO
import numpy as np

# Load the YOLOv8 model (make sure best.pt is in the correct path)
model = YOLO('openCv/best.pt')

# Open the video file
video_path = 'openCv/cctv_comoro.mp4'
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
window_title = "YOLOv8 Detection - cctv_comoro.mp4"

if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}.")
    exit(1)

frame_count = 0
last_boxes = None
last_classes = None
last_scores = None
last_frame = None

# Set detection FPS (e.g., 2 FPS)
detect_fps = 1
frames_per_detection = 2

print(frames_per_detection)
box_thickness = 2  # Set bounding box thickness here

# Generate a color map for each class
num_classes = len(model.names)
np.random.seed(42)  # For reproducible colors
colors = [tuple(np.random.randint(0, 255, 3).tolist()) for _ in range(num_classes)]

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video or failed to grab frame.")
        break

    if frame_count % frames_per_detection == 0:
        # Run YOLOv8 detection every N frames
        results = model(frame)[0]
        last_boxes = results.boxes.xyxy.cpu().numpy() if results.boxes is not None else None
        last_classes = results.boxes.cls.cpu().numpy() if results.boxes is not None else None
        last_scores = results.boxes.conf.cpu().numpy() if results.boxes is not None else None
        last_frame = frame.copy()

    # Draw last detected boxes on the current frame
    annotated_frame = frame.copy()
    if last_boxes is not None:
        for box, cls, score in zip(last_boxes, last_classes, last_scores):
            x1, y1, x2, y2 = map(int, box)
            label = f"{model.names[int(cls)]} {score:.2f}"
            color = colors[int(cls) % num_classes]
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, box_thickness)
            cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    cv2.imshow(window_title, annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
