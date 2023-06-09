from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.subserie import Subserie
from authApp.serializers.subserieSerializer import SubserieSerializer


class SubserieDetailView(generics.ListAPIView):
    queryset = Subserie.objects.all()
    serializer_class = SubserieSerializer
    #permission_classes = (IsAuthenticated,)

    def get_one(self, request, id):
        return super().get(request)
#        return self.queryset.filter(pk=id)

    def get(self, request, *args, **kwargs):
        print(kwargs)
        if kwargs == {}:
            return super().get(request, *args, **kwargs)
