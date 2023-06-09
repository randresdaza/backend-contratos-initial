from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.rolSerializer import RolSerializer

class RolCreateView(views.APIView):
    def post (self, request, *args, **kwargs):
        serializer = RolSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # libroData = {"nombreL": request.data["nombreL"],
        #             #"estadoL": request.data["estadoL"],
        #             "autor": request.data["autor"],
        #             "editorial": request.data["editorial"],
        #             "categoria": request.data["categoria"] }
        # token = TokenObtainPairSerializer(data = libroData)
        # token.is_valid(raise_exception=True)

        return Response (status = status.HTTP_201_CREATED)
