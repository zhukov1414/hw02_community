from django.shortcuts import get_object_or_404, render

from .models import Post, Group

from django.conf import settings


def index(request):
    posts = Post.objects.all()[:settings.NUMBER_POSTS]
    return render(request, 'posts/index.html', {
        'posts': posts,
    })


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:settings.NUMBER_POSTS]
    return render(request, 'posts/group_list.html', {
        'group': group,
        'posts': posts,
    })
