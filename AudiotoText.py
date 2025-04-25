#Import the openai Library
from openai import OpenAI

import os
from dotenv import load_dotenv
load_dotenv()

#openai.api_key=os.getenv("OPENAI_API_KEY")
my_api_key = os.getenv("OPENAI_API_KEY")
print(my_api_key)

my_file_path=os.getenv("AUDIO_FILE_PATH")
print(my_file_path)
     
      
# Create an api client
client = OpenAI(api_key=my_api_key)

# Load audio file
audio_file= open(my_file_path, "rb")


# Transcribe
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print("Showing the contents of the Audio Clip\n")

# Print the transcribed text
print(transcription.text)