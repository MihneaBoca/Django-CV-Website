from django.views import generic
from .models import Post


class Blog(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog.html'


class Post(generic.DetailView):
    model = Post
    template_name = 'post.html'
