YOLOv8 Real-Time Webcam Object Detection



Real-time object detection on a live webcam feed using YOLOv8 (Ultralytics) and OpenCV. Detects 80 common object classes (people, phones, bottles, chairs, etc.) with bounding boxes and confidence scores, running live at webcam frame rate.



Demo

<!-- Add your demo video/GIF here, e.g.: --> <!-- !\[Demo](demo.gif) --> <!-- or link to it: --> <!-- \[Watch the demo](demo.mp4) -->

Features

Real-time inference on live webcam feed

Pretrained YOLOv8n (nano) model — fast enough to run on CPU

Draws bounding boxes, class labels, and confidence scores per frame

Simple, single-file implementation

Tech Stack

Python

Ultralytics YOLOv8

OpenCV

PyTorch (via Ultralytics)

Setup

bash

\# Clone the repo

git clone https://github.com/Meerat369/yolov8-webcam-detection.git

cd yolov8-webcam-detection



\# Create and activate a virtual environment

python -m venv venv

venv\\Scripts\\activate      # Windows

\# source venv/bin/activate # macOS/Linux



\# Install dependencies

pip install ultralytics opencv-python

Usage

bash

python detect.py

The pretrained yolov8n.pt weights download automatically on first run.

A window opens showing your webcam feed with live detections.

Press q to quit.

How It Works

Captures frames from the default webcam using OpenCV (cv2.VideoCapture).

Passes each frame to the YOLOv8 model for inference.

Draws the resulting bounding boxes, labels, and confidence scores directly on the frame.

Displays the annotated frame in a live window, looping until the user quits.

Future Improvements

Swap yolov8n.pt for yolov8s.pt/yolov8m.pt for higher accuracy (slower)

Filter detections to specific object classes

Log detected objects with timestamps

Send detected object coordinates to an Arduino/robot for vision-guided tracking

