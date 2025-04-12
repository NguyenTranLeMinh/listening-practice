import pygame
import keyboard
import time
import random
from TTS.api import TTS

words = ["hello", "world", "Vietnam", "example", "on track", "schedule", "Thuy"]
random.shuffle(words)

print("*** Initializing is done! ***")
tts = TTS(model_name="tts_models/en/ljspeech/vits")
pygame.mixer.init()


pause_requested = False
exit_program = False

def handle_space_press():
    global pause_requested
    while True:
        if keyboard.is_pressed('space'):
            pause_requested = not pause_requested
            print("\nPAUSED" if pause_requested else "\nRESUMING...")
            
            while keyboard.is_pressed('space'):
                time.sleep(0.1)
        time.sleep(0.1)


import threading
space_thread = threading.Thread(target=handle_space_press, daemon=True)
space_thread.start()


for word in words:
    file_path = f"files/{word}.wav"
    tts.tts_to_file(text=word, file_path=file_path)
    if exit_program:
        break
    

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    # Monitor status
    while pygame.mixer.music.get_busy() and not exit_program:
        if pause_requested:
            # Finish current file before pausing
            continue
            
        if keyboard.is_pressed('esc'):
            print("\nExiting program...")
            exit_program = True
            pygame.mixer.music.stop()
            break
            
        time.sleep(0.1)
    

    while pause_requested and not exit_program:
        print("\rPress SPACE to continue...", end="")
        time.sleep(0.1)
        if keyboard.is_pressed('esc'):
            exit_program = True
            break

pygame.mixer.quit()
print("\nDon't be nervous, everything will be fine! ☺️")