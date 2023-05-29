from django import http
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from .models import *
from .forms import PostForm
from django.urls import reverse_lazy


class PostListView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.save(commit=True, request=self.request)
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.save(commit=True, request=self.request)
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ImageDeleteView(DeleteView):
    model = Image
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')