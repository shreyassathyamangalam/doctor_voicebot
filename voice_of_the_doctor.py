#Step 1a: Setup Text to Speech–TTS–model with gTTS
from dotenv import load_dotenv
load_dotenv()
import os
from gtts import gTTS


# Function to convert text to speech using gTTS
def text_to_speech_with_gtts_old(input_text, output_filepath):
    # Set the language for the TTS model
    language = 'en'
    
    # Create a gTTS object
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    
    # Save the audio file
    audioobj.save(output_filepath)

# Example usage
# input_text = "Hello, this is a test of the text to speech functionality."
# output_filepath= "gtts_testing.mp3"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath=output_filepath)

#Step 1b: Setup Text to Speech–TTS–model with ElevenLabs
import requests
import os

def text_to_speech_with_elevenlabs_old(input_text: str, output_filepath: str):
    """
    Converts input text to speech using ElevenLabs API and saves the audio to a file.

    Parameters:
        input_text (str): The text to convert to speech.
        output_filepath (str): Path to save the generated audio file.
    """
    # Replace with your actual ElevenLabs API key
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Default voice ID (can be customized)
    
    if not ELEVENLABS_API_KEY:
        raise ValueError("ElevenLabs API key is missing. Set ELEVENLABS_API_KEY environment variable.")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }

    payload = {
        "text": input_text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Failed to convert text to speech: {response.status_code}, {response.text}")

    with open(output_filepath, "wb") as f:
        f.write(response.content)

    print(f"Audio saved to {output_filepath}")

# Example usage
# input_text = "Hello, this is a test of the ElevenLabs text to speech functionality."
# output_filepath = "elevenlabs_testing.mp3"
# text_to_speech_with_elevenlabs_old(input_text=input_text, output_filepath=output_filepath)

# Step 2: Use Model for text output to voice

import subprocess
import platform

# Function to convert text to speech using gTTS
def text_to_speech_with_gtts(input_text, output_filepath):
    # Set the language for the TTS model
    language = 'en'
    
    # Create a gTTS object
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    
    # Save the audio file
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Example usage
# input_text = "Hello, this is a test of the automatic text to speech functionality."
# output_filepath= "gtts_testing_autoplay.mp3"
# text_to_speech_with_gtts(input_text=input_text, output_filepath=output_filepath)

def text_to_speech_with_elevenlabs(input_text: str, output_filepath: str):
    """
    Converts input text to speech using ElevenLabs API and saves the audio to a file.

    Parameters:
        input_text (str): The text to convert to speech.
        output_filepath (str): Path to save the generated audio file.
    """
    # Replace with your actual ElevenLabs API key
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Default voice ID (can be customized)
    
    if not ELEVENLABS_API_KEY:
        raise ValueError("ElevenLabs API key is missing. Set ELEVENLABS_API_KEY environment variable.")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }

    payload = {
        "text": input_text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Failed to convert text to speech: {response.status_code}, {response.text}")

    with open(output_filepath, "wb") as f:
        f.write(response.content)

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Example usage
# input_text = "Hello, this is an automatic test of the ElevenLabs text to speech functionality."
# output_filepath = "elevenlabs_testing_autoplay.mp3"
# text_to_speech_with_elevenlabs(input_text=input_text, output_filepath=output_filepath)

