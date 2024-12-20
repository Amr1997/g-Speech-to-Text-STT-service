# core/views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import call_kateb_api
from .serializers import AudioFileSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transcribe_audio(request):
    """
    Endpoint to upload an audio file, check the user's quota, and get transcription from Kateb API.

    Args:
    - request: The HTTP request containing the audio file and user information.

    Returns:
    - Response: The response containing either the transcription or an error message.
    """
    # Deserialize the input file using a serializer for validation and structure
    serializer = AudioFileSerializer(data=request.data)

    if serializer.is_valid():
        audio_file = serializer.validated_data['audio_file']
        user = request.user

        # Call the service to process the audio file and check the user's quota
        result = call_kateb_api(audio_file, user)

        if result.get("success"):
            # Successfully transcribed, return the transcribed text
            return Response({"transcribed_text": result["transcribed_text"]}, status=status.HTTP_200_OK)

        # Return error response if something goes wrong
        return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

    # If the serializer is invalid, return a detailed error message
    return Response({"error": "Invalid file or input. Please provide a valid audio file."}, status=status.HTTP_400_BAD_REQUEST)
