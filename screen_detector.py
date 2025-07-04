import torch
import cv2
import numpy as np
from PIL import ImageGrab
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def describe_screen():
    """
    Takes a screenshot of the screen and uses YOLOv7 to detect objects.
    Returns a list of detected object names and speaks them aloud.
    """
    try:
        # Take screenshot
        screenshot = ImageGrab.grab()

        # Convert PIL image to OpenCV format
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Load the model (only if not already loaded)
        model = torch.hub.load('./yolov7', 'custom', 'yolov7.pt', source='local', trust_repo=True)
        model.eval()

        # Run inference
        results = model(screenshot_cv)
        detections = results.pandas().xyxy[0]

        detected_objects = []

        if not detections.empty:
            confidence_threshold = 0.5
            high_conf_detections = detections[detections['confidence'] >= confidence_threshold]
            detected_objects = high_conf_detections['name'].unique().tolist()

        # Speak results
        if detected_objects:
            description = f"I see the following objects on the screen: {', '.join(detected_objects)}."
        else:
            description = "I don't see anything recognizable on the screen."

        print(description)
        speak(description)

        return detected_objects

    except Exception as e:
        error_msg = f"An error occurred while analyzing the screen: {e}"
        print(error_msg)
        speak("Something went wrong while analyzing the screen.")
        return []
