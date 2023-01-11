from django.shortcuts import get_object_or_404, render

from .models import Post, Group


NUMBER_POSTS = 10


def index(request):
    posts = Post.objects.all().order_by('-id')[:NUMBER_POSTS]
    return render(request, 'posts/index.html', {
        'posts': posts,
    })


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:NUMBER_POSTS]
    return render(request, 'posts/group_list.html', {
        'group': group,
        'posts': posts,
    })
