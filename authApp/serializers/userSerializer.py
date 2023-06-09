from authApp.models.user import User
from authApp.models.rol import Rol
from rest_framework import serializers
from authApp.serializers.rolSerializer import RolSerializer
from django.contrib.auth.hashers import is_password_usable

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','name','email','rol', 'estado','password']

    def to_representation(self, obj):
        user = User.objects.get(id = obj.id)
        return {
            'id':user.id,
            'username':user.username,
            'name': user.name,
            'email':user.email,
            'rol': user.rol,
            'estado': user.estado
        }

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            new_password = validated_data.pop('password')
            if is_password_usable(new_password) and new_password != instance.password:
                instance.set_password(new_password)
        return super().update(instance, validated_data)