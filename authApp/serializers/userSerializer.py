from authApp.models.user import User
from authApp.models.rol import Rol
from rest_framework import serializers
from django.contrib.auth.hashers import is_password_usable
from authApp.serializers.rolSerializer import RolSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    rol = serializers.PrimaryKeyRelatedField(queryset=Rol.objects.all(), write_only=True)
    class Meta:
        model = User
        fields = ['id','username','name','email','rol', 'estado','password']

    def create(self, validated_data):
        rol_id = validated_data.pop('rol_id', None)
        user = User.objects.create(**validated_data)
        if rol_id:
            user.rol = rol_id
            user.save()
        return user

    def to_representation(self, obj):
        rol = obj.rol
        rol_serializer = RolSerializer(rol)
        return {
            'id':obj.id,
            'username':obj.username,
            'name': obj.name,
            'email':obj.email,
            'rol': rol_serializer.data,
            'estado': obj.estado
        }

    def update(self, instance, validated_data):
        if 'rol_id' in validated_data:
            rol_id = validated_data.pop('rol_id')
            instance.rol = rol_id
        if 'password' in validated_data:
            new_password = validated_data.pop('password')
            if is_password_usable(new_password) and new_password != instance.password:
                instance.set_password(new_password)
        return super().update(instance, validated_data)