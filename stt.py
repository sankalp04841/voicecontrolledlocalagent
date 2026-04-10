import whisper
import os

model = whisper.load_model("base")

def transcribe(audio_path):
    if not os.path.exists(audio_path):
        return "Audio file not found"

    result = model.transcribe(audio_path)
    return result["text"]