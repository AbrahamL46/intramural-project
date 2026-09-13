from ultralytics import YOLO

#load small pretrained YOLO model
model = YOLO("yolo11n.pt")

#run detection on an image
results = model("videos/test_image.jpg")

result = results[0]

for box in result.boxes:
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])

    name = result.names[class_id]

    print(name, confidence)

    x1, y1, x2, y2 = box.xyxy[0]

    print(x1, y1, x2, y2)