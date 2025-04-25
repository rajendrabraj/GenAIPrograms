import pygame
import os
import time

import os
from dotenv import load_dotenv
load_dotenv()

#openai.api_key=os.getenv("OPENAI_API_KEY")


folder_path=os.getenv("folder_path")
print(folder_path +"\n")
     


def play_audio_files_from_folder(folder_path):
    pygame.mixer.init()
    audio_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav', '.ogg'))]

    if not audio_files:
        print("No audio files found in the specified folder.\n")
        return

    for audio_file in audio_files:
        file_path = os.path.join(folder_path, audio_file)
        try:
             pygame.mixer.music.load(file_path)
             pygame.mixer.music.play()
             print(f"Playing: {audio_file}")
             while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        except pygame.error as e:
            print(f"Error playing {audio_file}: {e}")
            continue
        
    pygame.mixer.quit()

if __name__ == "__main__":
    #folder_path = input("Enter the path to the folder containing audio files: ")
    print("Playing Songs from :  "  + folder_path + "\n")
             
    play_audio_files_from_folder(folder_path)