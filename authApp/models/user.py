from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth.hashers import make_password
from .rol import Rol

class UserManager (BaseUserManager):
    def create_user(self,username,password = None):
        if not username:
            raise ValueError('Usuario ya existente')
        user = self.model(username=username)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,password = None):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username',max_length=30,unique=True)
    password = models.CharField('Password',max_length=256, blank=True)
    name = models.CharField('Name',max_length=100)
    email = models.EmailField('Email',max_length=256)
    rol = models.CharField('Rol', max_length=50)
    estado = models.CharField('Estado', max_length=50, default="Activo")

    def save(self, *args, **kwargs):
        if self.pk is None:
            some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
            self.password = make_password(self.password, some_salt)
        else:
            user = User.objects.get(pk=self.pk)
            if self.password != user.password:
                some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
                self.password = make_password(self.password, some_salt)
        super().save(*args, **kwargs)

    @staticmethod
    def esta_activo(id):
        user = User.objects.filter(id=id)
        for item in user:
            if (item.estado == 'Activo'):
                print('el usuario esta {1}', item.estado)
                return True
            else:
                print('el usuario esta {1}', item.estado)
                return False
    
    objects = UserManager()
    USERNAME_FIELD = 'username'

