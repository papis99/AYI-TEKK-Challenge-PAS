from fastapi import FastAPI
from recordAudio import record_audio
from trancription import transcription1
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/enregistrement")
def renregistrement():
    record_audio()

@app.get("/transcription")
def transcription():
    audio_file = "recording1.wav"
    return transcription1(audio_file)
