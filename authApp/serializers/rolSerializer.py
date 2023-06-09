from authApp.models.rol import Rol
from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id','nombre']
    
    def to_representation(self, obj):
        rol = Rol.objects.get(id = obj.id)
        return {
            'id':rol.id,
            'nombre':rol.nombre,
        }