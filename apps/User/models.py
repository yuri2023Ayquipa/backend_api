from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from apps.Person.models.models_person import Persona
from apps.Person.models.models_correo import Correo
from apps.Person.models.models_estado import Estado

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, username, id_persona, password=None, **extra_fields):
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        
        if not isinstance(id_persona, Persona):
            raise ValueError('id_persona debe ser una instancia de Persona')
        
        user = self.model(username=username, id_persona=id_persona, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, id_persona, password=None, **extra_fields):
        user = self.create_user(
            username=username, id_persona=id_persona, password=password, **extra_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    
    id_persona = models.OneToOneField(Persona, on_delete=models.PROTECT, blank=False, null=False)
    username = models.CharField(max_length=150, unique=True, blank=False, null=False)
    is_active = models.ForeignKey(Estado, on_delete=models.PROTECT, default=True, null=False)
    is_staff = models.BooleanField(default=False) # Indica si el usuario tiene permisos de administrador del sitio.
    date_joined = models.DateTimeField(auto_now_add=True) # Fecha y hora en que el usuario se registró.
    image_perfil = models.ImageField(upload_to="profiles/", null=True, blank=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['id_persona']

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def correos(self):
        return Correo.objects.filter(id_persona=self.id_persona)
    
