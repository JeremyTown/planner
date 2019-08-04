from rest_framework import serializers
from .models import Tag, Category, Post


class TagSerializer(serializers.ModelSerializer):
    pass


class CategorySerializer(serializers.ModelSerializer):
    pass


class PostSerializer(serializers.ModelSerializer):
    pass
