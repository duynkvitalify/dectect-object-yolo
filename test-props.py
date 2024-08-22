from ultralytics import YOLO

# Load a pretrained YOLOv8n-cls Classify model
model = YOLO("yolo-Weights/yolov8n-cls.pt")

# Run inference on an image
results = model("bus.jpg")  # results list

# View results
for r in results:
    print(r.probs)  # print the Probs object containing the detected class probabilities