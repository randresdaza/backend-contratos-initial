from authApp.models.dependencia import Dependencia
from rest_framework import serializers

class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = ['id','nombre']
    
    def to_representation(self, obj):
        dependencia = Dependencia.objects.get(id = obj.id)
        return {
            'id':dependencia.id,
            'nombre':dependencia.nombre,
        }