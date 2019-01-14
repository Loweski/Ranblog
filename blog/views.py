from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Post
# Create your views here.


def index(request):
    latest_posts = Post.objects.order_by('-created_date')[:5]
    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/index.html', context)

def topics(request, topic_id):
    return HttpResponse("You are looking at topic: %s." % topic_id)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)
