from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template_post = 'posts/index.html'
    posts = Post.objects.all()
    context = {
        'posts': posts, 
    }
    return render(request, template_post, context)


def group_list(request, slug):
    template_post = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template_post, context)

