# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField('UserUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MenuMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_menu'


class PersonCondiciondomiciliaria(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    denominacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'person_condiciondomiciliaria'


class PersonCorreo(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=254)
    is_primary = models.IntegerField()
    is_verified = models.IntegerField()
    verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id_estado = models.ForeignKey('PersonEstado', models.DO_NOTHING)
    id_persona = models.ForeignKey('PersonPersona', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'person_correo'


class PersonDepartamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    departamento = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'person_departamento'


class PersonDireccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    ubigeo = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=250)
    numero = models.CharField(max_length=10, blank=True, null=True)
    piso = models.CharField(max_length=10, blank=True, null=True)
    bloque = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id_departamento = models.ForeignKey(PersonDepartamento, models.DO_NOTHING)
    id_distrito = models.ForeignKey('PersonDistrito', models.DO_NOTHING)
    id_estado = models.ForeignKey('PersonEstado', models.DO_NOTHING)
    id_persona = models.ForeignKey('PersonPersona', models.DO_NOTHING, blank=True, null=True)
    id_provincia = models.ForeignKey('PersonProvincia', models.DO_NOTHING)
    id_tipo_via = models.ForeignKey('PersonTipovia', models.DO_NOTHING, blank=True, null=True)
    id_tipo_zona = models.ForeignKey('PersonTipozona', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_direccion'


class PersonDistrito(models.Model):
    id = models.BigAutoField(primary_key=True)
    distrito = models.CharField(max_length=150)
    id_provincia = models.ForeignKey('PersonProvincia', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'person_distrito'


class PersonEstado(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'person_estado'


class PersonGenero(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    denominacion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'person_genero'


class PersonNacionalidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    denominacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'person_nacionalidad'


class PersonOperador(models.Model):
    id = models.BigAutoField(primary_key=True)
    operador = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'person_operador'


class PersonOrigenentidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    denominacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'person_origenentidad'


class PersonPersona(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero_documento = models.CharField(unique=True, max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id_condiciondomiciliaria = models.ForeignKey(PersonCondiciondomiciliaria, models.DO_NOTHING, db_column='id_condicionDomiciliaria_id')  # Field name made lowercase.
    id_estado = models.ForeignKey(PersonEstado, models.DO_NOTHING, blank=True, null=True)
    id_nacionalidad = models.ForeignKey(PersonNacionalidad, models.DO_NOTHING)
    id_tipo_contribuyente = models.ForeignKey('PersonTipocontribuyente', models.DO_NOTHING, blank=True, null=True)
    id_tipo_documento = models.ForeignKey('PersonTipodocumento', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'person_persona'


class PersonPersonajuridica(models.Model):
    id = models.BigAutoField(primary_key=True)
    razon_social = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=100)
    id_origen_entidad = models.ForeignKey(PersonOrigenentidad, models.DO_NOTHING)
    id_persona = models.OneToOneField(PersonPersona, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'person_personajuridica'


class PersonPersonanatural(models.Model):
    id = models.BigAutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey(PersonGenero, models.DO_NOTHING)
    id_persona = models.OneToOneField(PersonPersona, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'person_personanatural'


class PersonProvincia(models.Model):
    id = models.BigAutoField(primary_key=True)
    provincia = models.CharField(max_length=150)
    id_departamento = models.ForeignKey(PersonDepartamento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'person_provincia'


class PersonTelefono(models.Model):
    id = models.BigAutoField(primary_key=True)
    telefono = models.CharField(max_length=20)
    tipo_telefono = models.CharField(max_length=50, blank=True, null=True)
    is_primary = models.IntegerField()
    is_verified = models.IntegerField()
    verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id_estado = models.ForeignKey(PersonEstado, models.DO_NOTHING)
    id_operador = models.ForeignKey(PersonOperador, models.DO_NOTHING)
    id_persona = models.ForeignKey(PersonPersona, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'person_telefono'


class PersonTipocontribuyente(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=6)
    denominacion = models.CharField(max_length=220)

    class Meta:
        managed = False
        db_table = 'person_tipocontribuyente'


class PersonTipodocumento(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_sunat = models.CharField(max_length=10)
    denominacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'person_tipodocumento'


class PersonTipovia(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=100)
    deniminacion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'person_tipovia'


class PersonTipozona(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=100)
    denominacion = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'person_tipozona'


class UserUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    is_staff = models.IntegerField()
    date_joined = models.DateTimeField()
    image_perfil = models.CharField(max_length=100, blank=True, null=True)
    id_persona = models.OneToOneField(PersonPersona, models.DO_NOTHING)
    is_active = models.ForeignKey(PersonEstado, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_users'


class UserUsersGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    users = models.ForeignKey(UserUsers, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_users_groups'
        unique_together = (('users', 'group'),)


class UserUsersUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    users = models.ForeignKey(UserUsers, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_users_user_permissions'
        unique_together = (('users', 'permission'),)
