from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post
# from .forms import NewPostForm

# Create your views here.
class PostListView(ListView):
    # This class is for paginating pages if content reach certain number
    # So, if you have 10 posts/articles it still showing 5 and the other is in another page
    # This will only showing published Post.
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'microblog/post_list.html'

# This function is deprecated because we have another class with pagination function
# def post_list(request):
#     # filter post by published and order by recent created = minus
#     posts = Post.objects.filter(status='published').order_by('-created')
#     return render(request, 'microblog/post_list.html', {'posts': posts})

# Get Full Post detail if user click continue reading..
# If page not exist, 404 will shown up
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)  
    posts = Post.published.all()
    return render(request, 'microblog/post_detail.html', {'post': post})

# This class is for creating new post on front-end
class CreateNewPost(CreateView):
    model = Post
    template_name = 'microblog/post_new.html'
    fields = 'title', 'author', 'body', 'status', 'tags'
    
class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    
class EditPost(UpdateView):
    model = Post
    template_name = 'microblog/post_edit.html'
    fields = 'title', 'author', 'body', 'status', 'tags'