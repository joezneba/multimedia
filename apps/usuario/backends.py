from django.contrib.auth import backends
from django.contrib.auth import get_user_model
from django.db.models.query_utils import Q

'''  INICIO DE SESIÓN PERSONALIZADO PARA ACEPTAR EMAIL Y USERNAME PARA LOGIN '''
class CustomBackend(backends.ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            # below line gives query set,you can change the queryset as per your requirement
            user = UserModel.objects.filter(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            ).distinct()

        except UserModel.DoesNotExist:
            return None

        if user.exists():
            ''' get the user object from the underlying query set,
            there will only be one object since username and email
            should be unique fields in your models.'''
            user_obj = user.first()
            if user_obj.check_password(password):
                return user_obj
            return None
        else:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None