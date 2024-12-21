from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import call_kateb_api
from .serializers import AudioFileSerializer
from io import BytesIO

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transcribe_audio(request):
    """
    Endpoint to upload an audio file, check the user's quota, and get transcription from Kateb API.
    """
    serializer = AudioFileSerializer(data=request.data)

    if serializer.is_valid():
        audio_file = serializer.validated_data['audio_file']
        user = request.user
        
        # Read the file content as bytes
        file_content = BytesIO(audio_file.read())

        # Call the service to process the audio file and check the user's quota
        result = call_kateb_api(file_content, user)

        if result.get("success"):
            return Response({"transcribed_text": result["transcribed_text"]}, status=status.HTTP_200_OK)

        return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Invalid file or input. Please provide a valid audio file."}, status=status.HTTP_400_BAD_REQUEST)
