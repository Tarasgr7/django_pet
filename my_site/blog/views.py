from datetime import date
from django.views.generic import ListView,DetailView

from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import CommentForm

class StartingPageView(ListView):
    template_name="blog/index.html"
    model=Post
    ordering=["-date",]
    context_object_name="posts"
    def get_queryset(self):
        queryset=super().get_queryset()
        data=queryset[:3]
        return data


class PostsView(ListView):
    template_name="blog/all-posts.html"
    model=Post
    ordering=["-date"]
    context_object_name="all_posts"

class SinglePostView(DetailView):
    template_name="blog/post-detail.html"
    model=Post
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["posts_tags"]=self.object.tag.all()
        context["comment_form"]=CommentForm()
        return context