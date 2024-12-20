from rest_framework import serializers


class AudioFileSerializer(serializers.Serializer):
    audio_file = serializers.FileField(required=True, allow_empty_file=False)

    def validate_audio_file(self, value):
        """
        Optionally, validate file type or size before proceeding.
        """
        if not value.name.endswith('.wav'):
            raise serializers.ValidationError("Only WAV files are allowed.")
        # Add any other validation like file size if needed
        return value
