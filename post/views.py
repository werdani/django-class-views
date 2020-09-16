from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView

# Create your views here.
from .models import Post


class PostList(ListView):
    model = Post
    context_object_name ='all_posts'
   # queryset = Post.objects.filter(active=True)
   # template_name = 'post/test.html'
    def get_queryset(self):
        return Post.objects.filter(active=True)
class PostDetail(DetailView):

    model = Post
class PostCreate(CreateView):

    model = Post

class PostDelete(DeleteView):

    model = Post

class PostUpdate(UpdateView):

    model = Post
