from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView

# Create your views here.
from .models import Post


class PostList(ListView):

    model = Post

class PostDetail(DetailView):

    model = Post
class PostCreate(CreateView):

    model = Post

class PostDelete(DeleteView):

    model = Post

class PostUpdate(UpdateView):

    model = Post
