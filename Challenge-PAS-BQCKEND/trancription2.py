# import colabutils.audio
# from fastapi import FastAPI
# from IPython.display import Audio, display, clear_output
# from colabutils import *
# #from colab_utils import record_audio
# import ipywidgets as widgets
# from scipy.io import wavfile
# import numpy as np
# from wolof import Speech2Text
# from wolof import Speech2Text
#
#
# asr = Speech2Text(model_name="abdouaziiz/wav2vec2-xls-r-300m-wolof")
#
# app = FastAPI()
# record_seconds =   10#@param {type:"number", min:1, max:100, step:1}
# sample_rate = 16000
#
#
# @app.get("/test")
# async def _record_audio():
#     clear_output()
#     audio = colabutils.audio.record(record_seconds)
#     #audio = record_audio(record_seconds)
#     display(Audio(audio, rate=sample_rate, autoplay=True))
#     wavfile.write('recorded.wav', sample_rate, (32767 * audio).numpy().astype(np.int16))
#
#     a = asr("recorded.wav")
#     return (a)
#
#     button = widgets.Button(description="Record Speech")
#     button.on_click(_record_audio)
#     display(button)