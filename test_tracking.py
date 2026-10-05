#tracking test experiment
from ultralytics import YOLO

#load a pretrained YOLO model
model = YOLO("yolo11s.pt")

#run detection on a video
results = model.track(
    "videos/shot1leftbehindtrimmed.mov", 
    show=True, 
    stream=True, 
    imgsz=1280, 
    conf=0.5,
    persist=True
)

for result in results:
    if result.boxes.id is not None:
        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            track_id = int(box.id[0])

            name = result.names[class_id]

            if name == "sports ball":

                x1, y1, x2, y2 = box.xyxy[0]

                print("BALL")
                print("Track ID:", track_id)
                print("Confidence:", confidence)
                print("Coordinates:", x1, y1, x2, y2)