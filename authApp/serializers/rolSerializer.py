from authApp.models.rol import Rol
from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id','nombre']
    
    def to_representation(self, obj):
        return {
            'id':obj.id,
            'nombre':obj.nombre,
        }