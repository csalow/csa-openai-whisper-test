import os
# from dotenv import load_dotenv
from openai import OpenAI

# the .env method to get the api-key
# load_dotenv()

# currently reading the openai api-key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

# audio_file= open("audio/audio-sample-2.wav", "rb")
audio_file= open("audio/Urlaub-in-den-Bergen.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcript)