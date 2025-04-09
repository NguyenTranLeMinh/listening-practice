import random
from playsound import playsound
from TTS.api import TTS

words = ["hello", "world", "Vietnam", "example"]
random.shuffle(words)

tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")
# tts = TTS(model_name="tts_models/en/ljspeech/vits", phonemizer="gruut")
# glow-tts

for word in words:
    tts.tts_to_file(text=word, file_path=f"files/{word}.wav")
    playsound(f"files/{word}.wav")