from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Post, Catagory
from django.views.generic import (
    ListView, DetailView, DeleteView, UpdateView, CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# def home(request):
#     posts = Post.objects.order_by('-id')
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog/home.html', context)

def cat_list_post(request,id):
    qs = Catagory.objects.get(id=id)
    context = {
        'cat': qs
    }
    return render(request, 'blog/cat_list_post.html', context)

def search_post(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query != None and query != '':
        post_list =post_list.filter(
            Q(title__icontains = query) |
            Q(overview__icontains = query) |
            Q(content__icontains = query) |
            Q(author__username__icontains= query) |
            Q(author__first_name__icontains = query) |
            Q(author__last_name__icontains = query) |
            Q(catagories__title__icontains = query)
        ).distinct()
    else:
        post_list = None
    context ={
        'post_list' : post_list,
        'query':query
    }
    return render(request, 'blog/search_post.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    # Default : <app>/<model>_<viewtype> = blog/post_list
    ordering = ['-id']
    context_object_name = 'posts'
    paginate_by = 5




class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    ordering = ['-id']
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = ['title', 'overview', 'content',  'thumbnail', 'catagories']

    # to tell the new post author will be current logged in user/author/profile
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ['title', 'overview', 'content', 'thumbnail', 'catagories']

    # to tell the new post author will be current logged in user/author/profile
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # only author of the post can upadate the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    context_object_name = 'post'
    success_url='/'

    # only author of the post can upadate the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html')
