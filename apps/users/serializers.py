from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from plans.serializers import PlanSerializer


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=False, max_length=10,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户已经存在')])

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username',
                  'password',
                  'email']
