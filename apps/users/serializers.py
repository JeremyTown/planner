from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from plans.serializers import PlanSerializer


User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        # fields = '__all__'
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    user_plan = PlanSerializer(many=True)
    groups = GroupSerializer()

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id',
                  'username',
                  'password',
                  'last_login',
                  'username',
                  'last_name',
                  'first_name',
                  'gender',
                  'mobile',
                  'email',
                  'groups',
                  'user_plan']
