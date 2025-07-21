import whisper
import os

def convert_speech_to_text(audio_path="assets/sample_inputs/sample.wav"):
    print("Current working directory:", os.getcwd())
    print("File exists:", os.path.exists(audio_path))

    model = whisper.load_model("base", device="cpu")
    print(f"Transcribing {audio_path}...")

    try:
        result = model.transcribe(audio_path)
        print("Transcription:")
        print(result["text"])
        return result["text"]
    except Exception as e:
        print("Error during transcription:", e)
        return None
