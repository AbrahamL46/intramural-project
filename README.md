# Intramural Soccer Project

Lil side project to analyze soccer training footage using computer vision

## Main Goal

Analyze practice footage by detecting and tracking soccer balls

## Current Progress

Currently the program can:

- Read video using OpenCV
- Run pretrained YOLO object detection
- Detect people and soccer balls in the video
- Display YOLO bounding boxes and confidence scores

## Setup

### 1. Clone repository

Clone the repository from GitHub and open project folder in IDE

### 2. Create virtual environment

Windows: 

    python -m venv .venv

### 3. Active virtual environment

Windows:

    .venv\Scripts\activate

### 4. Install dependencies

    pip install -r requirements.txt

### 5. Add a test video

Create a folder in project directory and place a video inside it

Videos are ignored by Git and will not be uploaded to the repo

### 6. Run OpenCV test

    python test_opencv.py

### 7. Run YOLO test

Update video path inside 'test_yolo.py' to match your filename, then run:

    python test_yolo.py

YOLO should display the video with detected objects and bounding boxes

## Current Goal

Test YOLO on real soccer shooting footage and determine how reliably it 
detects a moving soccer ball