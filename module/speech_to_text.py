import whisper
import os

def convert_speech_to_text(audio_path):
    model = whisper.load_model("base", device="cpu")
    result = model.transcribe(audio_path)
    return result["text"].strip()
