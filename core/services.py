import requests
from pydub import AudioSegment
from io import BytesIO
from .models import Quota

def get_audio_duration(audio_file):
    """
    Get the duration of the audio file in seconds.
    Uses pydub to extract the duration of the audio.

    Args:
    - audio_file: The file object of the audio file.

    Returns:
    - float: The duration of the audio file in seconds.
    """
    audio_file.seek(0)  # Ensure the file pointer is at the start before using it
    audio = AudioSegment.from_wav(audio_file)  # Load the audio file
    return audio.duration_seconds  # Get the duration in seconds


def call_kateb_api(audio_data, user):
    """
    Sends audio data to the Kateb API to convert Arabic audio to text and checks user's quota.

    Args:
    - audio_data: The audio data (file object) to be sent for transcription.
    - user: The user object to check the quota against.

    Returns:
    - dict: A dictionary containing the transcription result or an error message.
    """
    # Get user's quota and check if they have enough remaining time
    quota = user.quota
    audio_duration = get_audio_duration(audio_data)

    if not quota.can_process(audio_duration):
        return {"success": False, "error": "User has exceeded their quota."}
    
    # If the user has enough quota, send the audio to the Kateb API
    url = "https://echo-6sdzv54itq-uc.a.run.app/kateb"
    
    # Prepare the form data for the POST request
    audio_data.seek(0)  # Ensure the pointer is at the beginning
    formdata = {
        "file": ("file.wav", audio_data, "audio/wav")  # Ensure correct file format
    }

    try:
        # Send the request to the Kateb API using the correct method
        response = requests.post(url, files=formdata)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response as JSON
            response_data = response.json()
            
            # Extract the words from the response
            words = response_data.get("json", {}).get("words", [])
            
            # Extract the text from the words list
            transcribed_text = " ".join([word.get("text", "") for word in words])

            # Update user's quota with the processed audio time
            quota.add_time(audio_duration)

            return {"success": True, "transcribed_text": response_data}
        else:
            return {"success": False, "error": f"Failed to get a valid response from the Kateb API. Status code: {response.status_code}"}

    except Exception as e:
        return {"success": False, "error": str(e)}
