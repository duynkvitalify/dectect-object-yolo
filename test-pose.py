from ultralytics import YOLO

# Load a model
model = YOLO("yolo-Weights/yolov8n-pose.pt")  # load an official model
# model = YOLO("path/to/best.pt")  # load a custom trained model

# Predict with the model
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
results[0].show()
print(results)