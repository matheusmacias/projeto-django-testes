from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/view', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('image/<int:pk>/delete/', views.ImageDeleteView.as_view(), name='image_delete'),
]