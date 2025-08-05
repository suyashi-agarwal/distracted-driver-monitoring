import cv2
import os
import time
from ultralytics import YOLO
from PIL import Image
import numpy as np

# CONSTANTS
MODEL_PATH = 'models/best.pt'
VIDEO_PATH = r"C:\Users\SUYASHI.AGARWAL\Downloads\test_vid.avi"
GIF_PATH = 'wait_for_it.GIF'

CONFIDENCE_THRESHOLD = 0.3
ALERT_PERSISTENCE_SECONDS = 2  # time for which the alert stays on the screen


last_phone_detection_time = 0
last_seatbelt_detection_time = float('-inf')
# intentionally starting with a very old time so the seatbelt alert can trigger immediately


def check_path():
    """Checks if the model and video source paths are actually valid"""
    if not os.path.exists(MODEL_PATH):
        print(f"Error: Model file not found at '{MODEL_PATH}'")
        return False
    if not os.path.exists(VIDEO_PATH):
        print(f"Error: Video file not found at '{VIDEO_PATH}'")
        return False
    return True


if not check_path():
    exit()

try:
    model = YOLO(MODEL_PATH)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")


cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("ERROR😟: Couldn't open the video file.")

    exit()

try:
    gif = Image.open(GIF_PATH)
    print("Displaying loading animation...")
    # Loop through each frame of the GIF
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        # Convert PIL image to OpenCV format========================
        frame_bgr = cv2.cvtColor(np.array(gif.convert('RGB')), cv2.COLOR_RGB2BGR)

        cv2.imshow("Driver Monitoring System", frame_bgr)
        # Wait for a short duration (e.g., 50ms) to control animation speed
        if cv2.waitKey(50) & 0xFF == ord('s'):  # Press 's' to skip animation
            break
except Exception as e:
    print(f"Could not load GIF: {e}. Starting video directly.")
# --- End of new section ---


print("PROCESSING VIDEO...")
while True:

    success, frame = cap.read()
    if not success:
        print("End of video reached")
        break

    results = model(frame, verbose=False)

    phone_found_this_frame = False
    seatbelt_found_this_frame = False

    for r in results:
        for box in r.boxes:
            if box.conf[0] > CONFIDENCE_THRESHOLD:
                class_name = model.names[int(box.cls[0])]
                if class_name == 'phone':
                    phone_found_this_frame = True
                elif class_name == 'seatbelt':
                    seatbelt_found_this_frame = True

    current_time = time.time()

    if phone_found_this_frame:
        last_phone_detection_time = current_time
    if seatbelt_found_this_frame:
        last_seatbelt_detection_time = current_time

    # Decides if alerts should be active based on persistence ---
    phone_alert_active = (current_time - last_phone_detection_time) < ALERT_PERSISTENCE_SECONDS
    seatbelt_alert_active = (current_time - last_seatbelt_detection_time) > ALERT_PERSISTENCE_SECONDS

    # Drawing logic
    if phone_alert_active:
        cv2.putText(frame, "PHONE USAGE DETECTED", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    if seatbelt_alert_active:
        # Corrected position so it doesn't overlap with the phone alert
        cv2.putText(frame, "NO SEATBELT", (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow("Driver Monitoring System", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


print("Shutting down...")
cap.release()
cv2.destroyAllWindows()

