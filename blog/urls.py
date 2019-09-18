from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, about, cat_list_post, search_post

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('cat/<int:id>/', cat_list_post, name='cat-list-post'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('post/create', PostCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    path('about', about, name='blog-about'),
    path('post/search/', search_post, name='search-post')
]
