from ultralytics import YOLO

#load a pretrained YOLO model
model = YOLO("yolo11s.pt")

#run detection on a video
results = model("videos/shot1leftbehindtrimmed.mov", show=True, stream=True, 
                imgsz=1280, conf=0.5)

for result in results:
    for box in result.boxes:

        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        name = result.names[class_id]

        if name == "sports ball":

            x1, y1, x2, y2 = box.xyxy[0]

            print("BALL")
            print("Confidence:", confidence)
            print("Coordinates:", x1, y1, x2, y2)