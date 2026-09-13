from ultralytics import YOLO

#load small pretrained YOLO model
model = YOLO("yolo11n.pt")

#run detection on an image
results = model("videos/test_image.jpg")

#show image with YOLO's boxes drawn on it
results[0].show()

