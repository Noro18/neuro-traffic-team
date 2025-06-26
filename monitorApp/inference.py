import os
import cv2
from ultralytics import YOLO
from django.utils import timezone
from collections import Counter
from .models import DetailDetail, Detecta, Class  # Import your Django model

# Get the absolute path to best.pt
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best.pt")
VIDEO_PATH = os.path.join(BASE_DIR, "cctv_comoro.mp4")

def run_inference(video_source=VIDEO_PATH, save_to_db=True, save_interval=30):
    """
    Run YOLO inference on video source and optionally save results to database.
    
    Args:
        video_source: Path to video file or camera index
        save_to_db: Whether to save detection results to database
        save_interval: Save to database every N frames (to avoid too frequent saves)
    """
    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(video_source)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frame_count += 1
        results = model(frame)
        
       
        # ida ne'e check se quando nia frame to'o ona frame save ne'ebe ida set entain nia langsun save
        if save_to_db and frame_count % save_interval == 0:
            save_detections_to_db(results[0])
        
        annotated_frame = results[0].plot()
        ret, jpeg = cv2.imencode('.jpg', annotated_frame)
        if not ret:
            continue
        yield jpeg.tobytes()
    
    cap.release()

def save_detections_to_db(result):
    """
    Save detection results to database using existing Django models.
    
    Args:
        result: YOLO detection result object
    """
    try:
        if result.boxes is not None and len(result.boxes) > 0:
            # Get class names from detections
            class_ids = result.boxes.cls.cpu().numpy().astype(int)
            class_names = [result.names[class_id] for class_id in class_ids]
            
            # Count occurrences of each class
            class_counts = Counter(class_names)
            total_detections = sum(class_counts.values())
            
            # Create Detecta record
            detecta_record = Detecta.objects.create(
                total=total_detections,
                oras=timezone.now()
            )
            
            # Save each detected class and quantity
            for class_name, quantity in class_counts.items():
                # Get or create Class record
                class_record, created = Class.objects.get_or_create(
                    naran_class=class_name
                )
                
                # Create DetailDetail record
                DetailDetail.objects.create(
                    id_detecta=detecta_record,
                    id_class=class_record,
                    quantity=quantity
                )
            
            print(f"Saved detection: {total_detections} total objects detected")
            
    except Exception as e:
        print(f"Error saving to database: {e}")