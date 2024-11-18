import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

HOME = os.getcwd()

ELEVENLABS_API_KEY = ""

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def tamil_text_to_speech_file(text: str) -> str:
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
        voice_id="EVL7m7geFc0iIITWhlsA",
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
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
#     tamil_text_to_speech_file("Capillaries என்பது ball bonding செயலில் பயன்படுத்தப்படும் கருவிகள். இவை சிமெட்ரிக் செராமிக் கருவிகள் ஆகும், மற்றும் இவற்றில் wire feed க்கென செங்குத்து துளைகள் உள்ளன.")