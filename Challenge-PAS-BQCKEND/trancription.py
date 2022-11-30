#from fastapi import FastAPI
from wolof import Speech2Text

asr = Speech2Text(model_name="abdouaziiz/wav2vec2-xls-r-300m-wolof")

def transcription1(audio):
     print("transcription en cour...")
     a = asr(audio)
     print("Fin de la transcription")
     #print("RESULTAT : ", a)
     return a
