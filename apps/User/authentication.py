from datetime import timedelta
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import TokenAuthentication

class ExpiringTokenAuthentication(TokenAuthentication):
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)
    
    def token_expire_handler(self, token):  # Corregido el nombre del método
        is_expire = self.is_token_expired(token)
        if is_expire:
            token.delete()
            # aquí va el código que borra las sesiones
            message = "Sesión finalizada."
            return Response({"message": message}, status=status.HTTP_403_FORBIDDEN)
        return is_expire
    
    def authenticate_credentials(self, key):
        message, token, user = None, None, None
        try: 
            token = self.get_model().objects.select_related('user').get(key=key)
        except self.get_model().DoesNotExist:
            message = "Token inválido."
            return None, None, message  # Devuelve None para usuario y token si no se encuentra el token

        if not token.user.is_active:
            message = "El usuario asociado a este token ya no está activo."
            return None, None, message

        is_expired = self.token_expire_handler(token)
        if is_expired:
            message = "Token expirado."
            return None, None, message

        return token.user, token, message