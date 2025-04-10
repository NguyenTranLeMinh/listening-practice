import random
import pygame
import time
from TTS.api import TTS

words = ["hello", "world", "Vietnam", "example", "on track", "schedule", "Thuy"]

random.shuffle(words)

pygame.mixer.init()

tts = TTS(model_name="tts_models/en/ljspeech/vits")
# tts = TTS(model_name="tts_models/en/ljspeech/vits", phonemizer="gruut")
# glow-tts

for word in words:
    file_path = f"files/{word}.wav"
    tts.tts_to_file(text=word, file_path=file_path)

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  
        try:
            
            input()

        except KeyboardInterrupt:  
            pygame.mixer.music.stop()
            print("Stopped.")
            break


    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

pygame.mixer.quit()
# pygame.quit()