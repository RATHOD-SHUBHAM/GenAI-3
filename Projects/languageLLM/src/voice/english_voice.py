import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

HOME = os.getcwd()
print(HOME)

ELEVENLABS_API_KEY = ""

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def english_text_to_speech_file(text: str) -> str:
    """
    Converts text to speech and saves the output as an MP3 file.

    This function uses a specific client for text-to-speech conversion. It configures
    various parameters for the voice output and saves the resulting audio stream to an
    MP3 file with a unique name.

    Args:
        text (str): The text content to convert to speech.

    Returns:
        str: The file path where the audio file has been saved.
    """
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="EXAVITQu4vr4xnSDxMaL",  # Sarah pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"{HOME}/src/voice/generated_audio/{uuid.uuid4()}.mp3"
    # Writing the audio stream to the file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"A new audio file was saved successfully at {save_file_path}")

    # Return the path of the saved audio file
    return save_file_path


# if __name__ == "__main__":
#     text_to_speech_file("In ultrasonic wirebonding, low pressure and ultrasonic energy are used at a temperature of 25°C, and it can use either gold or aluminium wire. In thermosonic wirebonding, low pressure and ultrasonic energy are also used, but the temperature is higher, between 100-150°C, and it specifically uses gold wire.")