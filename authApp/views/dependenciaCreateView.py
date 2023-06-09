from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.dependenciaSerializer import DependenciaSerializer

class DependenciaCreateView(views.APIView):
    def post (self, request, *args, **kwargs):
        serializer = DependenciaSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (status = status.HTTP_201_CREATED)
