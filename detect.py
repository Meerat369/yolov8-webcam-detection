"""
Real-time object detection on webcam feed using YOLOv8.
Press 'q' to quit.
"""
 
import cv2
from ultralytics import YOLO
 
# Load pretrained YOLOv8 nano model (small + fast, good for real-time on CPU)
# Options: yolov8n.pt (nano), yolov8s.pt (small), yolov8m.pt (medium) - bigger = more accurate but slower
model = YOLO("yolov8n.pt")
 
# Open default webcam (0 = default camera)
cap = cv2.VideoCapture(0)
 
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
 
print("Starting detection. Press 'q' to quit.")
 
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
 
    # Run YOLOv8 inference on the frame
    results = model(frame, verbose=False)
 
    # results[0].plot() draws boxes, labels, and confidence scores on the frame
    annotated_frame = results[0].plot()
 
    # Show the annotated frame
    cv2.imshow("YOLOv8 Object Detection", annotated_frame)
 
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()