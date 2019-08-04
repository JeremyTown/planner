from django.shortcuts import render
from django.shortcuts import HttpResponse
from ..models import Post, Tag, Category


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    context = {'post_list': post_list}
    return render(request, 'index.html', context=context)
