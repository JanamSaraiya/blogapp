from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(success_url='/'), name='blog-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(success_url='/'), name='blog-delete'),
    path('post/create', PostCreateView.as_view(success_url='/'), name='blog-create'),
    path('about', views.about, name='blog-about')
]
