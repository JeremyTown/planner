from django.contrib import admin
from .models import Tag, Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    search_fields = ['name']
    list_display = ('id', 'name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    search_fields = ['name']
    list_display = ('id', 'name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    search_fields = ['name']
    list_display = ('title', 'author', 'category')
