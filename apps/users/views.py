from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from users.serializers import UserRegisterSerializer
from rest_framework import viewsets


User = get_user_model()


class CustomBackend:
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(Q(username=username) | Q(
                mobile=username) | Q(email=username))
            if user.check_password(password):
                return user
        except:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None


class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    serializer_class = UserRegisterSerializer
