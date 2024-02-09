import os
# from dotenv import load_dotenv
from openai import OpenAI

# the .env method to get the api-key
# load_dotenv()

# currently reading the openai api-key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")

# alternative: place directly here
# openai_api_key = "sk-n-abcdef12345"

client = OpenAI(api_key=openai_api_key)

source_file = "/home/csalow/clouds/altii-rhea/projects/altii/interview/altii-int-BellevueAM-Uebergewicht-Lang/out/altii-int-BellevueAM-Uebergewicht-Lang_v1_00w.mp3"

audio_file= open(source_file, "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcript)