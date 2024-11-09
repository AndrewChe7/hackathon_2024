from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import FileUploadSerializer

# ViewSets define the view behavior.
class FileUploadView(ViewSet):
    serializer_class = FileUploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # file_uploaded = request.FILES.get('file_uploaded')
            # file_uploaded.read()
            return Response({'message': 'File uploaded successfully'})
        else:
            return Response(serializer.errors, status=400)