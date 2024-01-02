# csa-openai-whisper-test

Test the API to Whisper from OpenAI

# Execute

python main.py

python main.py > trscpt-Urlaub-in-den-Bergen.txt

# Environment to load on Ubuntu

python3 -m venv env

source env/bin/activate

pip install --upgrade pip

pip install openai

pip install python-dotenv  # in case to read the api-key from .env

# Audio Sample

In directory "audio" - Urlaub-in-den-Bergen.mp3 which was recorded with ffmpeg, see "Record by ffmpeg to file".

# Record Audio with ffmpeg

## Find the audio input devices on ubuntu

pactl list short sources

## Record by ffmpeg to file

ffmpeg -f pulse -i alsa_input.usb-MICE_MICROPHONE_USB_MICROPHONE_201308-00.mono-fallback audio/Urlaub-in-den-Bergen.mp3

Source text - https://lingua.com/de/deutsch/lesen/reisen/
