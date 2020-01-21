from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('blog_app/', PostList.as_view(), name='post_list'),
    path('blog_app/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]