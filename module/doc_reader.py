import pytesseract
import cv2
import pyttsx3
from PIL import Image

def preprocess_image(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    processed_path = "assets/processed/temp.png"
    cv2.imwrite(processed_path, thresh)
    return processed_path

def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Text-to-speech error:", e)

def read_text_from_image(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        text = pytesseract.image_to_string(image).strip()
        return text
    except Exception as e:
        return f"Error reading image: {e}"
