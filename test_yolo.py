from ultralytics import YOLO

#load small pretrained YOLO model
model = YOLO("yolo11n.pt")

#run detection on a video
results = model("videos/abrahamtrainingtest.mov", show=True, stream=True)

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