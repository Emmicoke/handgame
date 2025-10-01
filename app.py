from ultralytics import YOLO

model = YOLO("best.pt")  # load a custom model

model.predict(source="0", imgsz = 640, conf = 0.6, show=True)  # predict on webcam