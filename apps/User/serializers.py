from rest_framework import serializers
from django.contrib.auth import password_validation, authenticate

from .models import Users, Persona
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    id_persona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())

    class Meta:
        model = Users
        fields = ['id', 'username', 'id_persona', 'password', 'is_active', 'is_staff', 'date_joined', 'image_perfil']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        image_perfil = validated_data.pop('image_perfil', None)
        user = Users.objects.create_user(
            username=validated_data['username'],
            id_persona=validated_data['id_persona'],
            password=validated_data['password'],
            is_active=validated_data.get('is_active', True),
            is_staff=validated_data.get('is_staff', False)
        )
        if image_perfil:
            user.image_perfil = image_perfil
            user.save()
        return user
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
class UserTokenSerializer(serializers.Serializer):
    class Meta:
        model = Users
        fields = ['id', 'username']
    
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username']
    