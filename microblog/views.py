from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import Post

from taggit.models import Tag

# Create your views here.
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

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
    fields = 'title', 'image', 'author', 'body', 'status', 'tags'
    
class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    
class EditPost(UpdateView):
    model = Post
    template_name = 'microblog/post_edit.html'
    fields = 'title', 'image','author', 'body', 'status', 'tags'
    
def About(request):
    return render(request,'microblog/about.html')

class TagIndexView(TagMixin, ListView):
    template_name = 'microblog/post_list.html'
    model = Post
    paginate_by = 4
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))
    
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def register_success(request):
    return render_to_response(
    'registration/register_success.html',
    )