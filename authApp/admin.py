from django.contrib import admin
from .models.user import User
from .models.rol import Rol
from .models.dependencia import Dependencia
from .models.serie import Serie
from .models.subserie import Subserie


admin.site.register(User)
admin.site.register(Rol)
admin.site.register(Dependencia)
admin.site.register(Serie)
admin.site.register(Subserie)

# Register your models here.
