# Import libraries
import torch
from ultralytics import YOLO  # Import YOLO model from Ultralytics
import cv2                   # Import OpenCV library
import math                  # Import math module for mathematical operations
import numpy


def check_imshow(warn=False):
    """Checks environment support for image display; warns on failure if `warn=True`."""
    try:
        cv2.imshow("test", numpy.zeros((1, 1, 3)))
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        return True
    except Exception as e:
        if warn:
            print(f"WARNING ⚠️ Environment does not support cv2.imshow() or PIL Image.show()\n{e}")
        return False

# Start webcam
cap = cv2.VideoCapture(1)    # Open default camera (index 0)
cap.set(3, 640)               # Set frame width to 640 pixels
cap.set(4, 480)               # Set frame height to 480 pixels

# Load the YOLO model
model = YOLO("yolo-Weights/yolov8n.pt")  # Load YOLOv8 model with pre-trained weights

while True:
    # Read a frame from the camera
    success, img = cap.read()

    # Perform object detection using the YOLO model on the captured frame
    results = model(img, stream=True)

    # Iterate through the results of object detection
    for r in results:
        boxes = r.boxes  # Extract bounding boxes for detected objects
        # Iterate through each bounding box
        for box in boxes:
            # Extract coordinates of the bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integer values

            # Draw the bounding box on the frame
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Calculate and print the confidence score of the detection
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->", confidence)

            # Determine and print the class name of the detected object
            cls = int(box.cls[0])
            print(box.cls[0])
            print("Class name -->", r.names[cls])

            # Draw text indicating the class name on the frame
            org = [x1, y1]


            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(img, r.names[cls], org, font, fontScale, color, thickness)

            # Display the frame with detected objects in a window named "Webcam"
            # if img:
            cv2.imshow('Cam', img)

    # Check for the 'q' key press to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

