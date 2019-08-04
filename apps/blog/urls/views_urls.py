from django.urls import path
from apps.blog.views import basic_view

urlpatterns = [
    path('', basic_view.index, name='index'),
    path('post/<pk>/', basic_view.detail, name='detail')
]