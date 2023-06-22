from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from authApp.models import Serie
from authApp.serializers.serieSerializer import SerieSerializer

class SerieView(APIView):
    permission_classes = (IsAuthenticated,)
    def validate_token(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)
        return valid_data['user_id'] == request.user.id

    def get(self, request, pk=None):
        if not self.validate_token(request):
            return Response({'detail': 'No está autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
        if pk is not None:
            try:
                serie = Serie.objects.get(pk=pk)
                serializer = SerieSerializer(serie)
                return Response(serializer.data)
            except Serie.DoesNotExist:
                return Response({'detail': 'La serie no existe'}, status=status.HTTP_404_NOT_FOUND)
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not self.validate_token(request):
            return Response({'detail': 'No está autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = SerieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not self.validate_token(request):
            return Response({'detail': 'No está autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            serie = Serie.objects.get(pk=pk)
        except Serie.DoesNotExist:
            return Response({'detail': 'La serie no existe'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SerieSerializer(serie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not self.validate_token(request):
            return Response({'detail': 'No está autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            serie = Serie.objects.get(pk=pk)
        except Serie.DoesNotExist:
            return Response({'detail': 'La serie no existe'}, status=status.HTTP_404_NOT_FOUND)
        serie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
