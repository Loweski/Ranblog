from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Post
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.order_by('-created_date')[:5]

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def topics(request, topic_id):
    return HttpResponse("You are looking at topic: %s." % topic_id)
