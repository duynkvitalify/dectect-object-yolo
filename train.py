from ultralytics import YOLO

# Load a model
model = YOLO("runs/detect/train7/weights/last.pt")  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
# Resume training
# results = model.train(resume=True)
results = model.train(data="/Users/vfa/code/yolo/demo-yolo/dataset/data.yaml", epochs=20, imgsz=640, device="mps")
# print(results)
# results = model.train(data="coco8.yaml", epochs=20, imgsz=640, device="mps")


# from roboflow import Roboflow
#
# rf = Roboflow(api_key="0PQyOfjRaNGVqUNyBQL5")
# project = rf.workspace("demoyolo-rgcod").project("demo-mrfim")
# version = project.version(13)
# dataset = version.download("yolov8")
# print(dataset)