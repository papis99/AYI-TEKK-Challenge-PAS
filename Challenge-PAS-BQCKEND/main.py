from fastapi import FastAPI
from recordAudio import record_audio
from trancription import transcription1

app = FastAPI()

@app.post("/enregistrement")
def renregistrement():
    record_audio()

@app.get("/transcription")
def transcription():
    audio_file = "recording1.wav"
    return transcription1(audio_file)
