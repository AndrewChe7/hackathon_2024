from rest_framework.serializers import Serializer, FileField

class FileUploadSerializer(Serializer):
    file_uploader = FileField()
    class Meta:
        fields = ['file_uploader']


