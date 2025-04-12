"""
This small program just speaks words individually and randomly to help you guys become familiar with them.
You can customize the list of input words. The program will choose 2 files from the sources to speak.
Author: Minh Ng
Date: 2025-04-12
"""


import os
import pygame
import keyboard
import time
import random
from TTS.api import TTS

vocabulary_path="vocabularies/"

all_words = []
files = [f for f in os.listdir(vocabulary_path) if f.endswith('.txt')]
selected_files = random.sample(files, 2)

for fname in selected_files:
    file_path = os.path.join(vocabulary_path, fname)
    try: 
        with open(file_path, 'r') as f:
            content = f.read().strip()
            words = [word.strip() for word in content.split(',')]
            all_words.extend(words)
    except Exception as e:
        print("Could not open file {}: {}".format(file_path, e))


print("*** Initializing is done! ***")
print("*** Feel free to press SPACE at any time to pause and predict the word you have heard. ***")
print("*** Hope this small program will help you guys improve yourself, even if only a little. ***")
print("*** Happy learning! 🌞 ***")

tts = TTS(model_name="tts_models/en/ljspeech/vits")
# tts_models/en/ljspeech/vits
# tts_models/en/vctk/vits
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

random.shuffle(all_words)
for word in all_words:
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
print("\n\"Don't be nervous, everything will be fine! April showers bring May flowers.☺️\"")