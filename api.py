import io

from fastapi import FastAPI,File,UploadFile
from ultralytics import YOLO

from PIL import Image
import cv2
import numpy as np

MODEL_PATH = 'models/best.pt'
CONFIDENCE_THRESHOLD = 0.4

try:
    model = YOLO(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

app = FastAPI(title="Driver Monitoring API")


@app.get("/")


def read_root():
    return {"message":"Welcome to the driver monitoring API.Send a POST request to /predict to analyze an image"}


@app.post("/predict")
async def predict(file:UploadFile = File(...)):
    """
    Receives an image file,runs inference and returns detections
    """
    # Read an image file from the upload
    contents = await file.read()

    # Converting to opencv image

    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    results = model(img,verbose=False)

    # Detection Logic
    phone_detected = False
    seatbelt_detected = False
    detections = []

    for r in results:
        for box in r.boxes:
            if box.conf[0] > CONFIDENCE_THRESHOLD:
                class_name = model.names[int(box.cls[0])]
                detections.append(class_name)
                if class_name == 'phone':
                    phone_detected = True
                elif class_name == 'seatbelt':
                    seatbelt_detected = True

    # Return the results in a json format
    return{
        "phone_detected": phone_detected,
        "seatbelt_detected": seatbelt_detected,
        "all_detections": detections
    }

