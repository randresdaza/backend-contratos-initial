from authApp.models.subserie import Subserie
from rest_framework import serializers

class SubserieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subserie
        fields = ['id','nombre']
    
    def to_representation(self, obj):
        subserie = Subserie.objects.get(id = obj.id)
        return {
            'id':subserie.id,
            'nombre':subserie.nombre,
        }