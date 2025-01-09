from typing import List, Dict

# Define a list of available voices
AVAILABLE_VOICES: List[Dict[str, str]] = [
    {"id": "v2/en_speaker_6", "name": "Male 1"},
    {"id": "v2/en_speaker_9", "name": "Male 2"},
    {"id": "v2/en_speaker_0", "name": "Female 1"},
    {"id": "v2/en_speaker_1", "name": "Female 2"},
]

def get_available_voices() -> List[Dict[str, str]]:
    """
    Returns a list of available voices.
    """
    return AVAILABLE_VOICES

def generate_prompt(text: str, voice_id: str) -> str:
    """
    Generate a prompt for the text-to-speech model based on the input text and voice ID.
    
    Args:
    text (str): The text to be converted to speech.
    voice_id (str): The ID of the voice to use.
    
    Returns:
    str: A formatted prompt for the text-to-speech model.
    """
    return f"[{voice_id}] {text}"

def get_voice_by_id(voice_id: str) -> Dict[str, str]:
    """
    Get voice details by ID.
    
    Args:
    voice_id (str): The ID of the voice to retrieve.
    
    Returns:
    Dict[str, str]: A dictionary containing the voice details.
    """
    for voice in AVAILABLE_VOICES:
        if voice["id"] == voice_id:
            return voice
    raise ValueError(f"Voice with ID '{voice_id}' not found.")

