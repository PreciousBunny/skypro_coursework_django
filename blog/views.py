from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from blog.models import Post
from blog.services import send_post_email


# Create your views here.

class PostListView(ListView):
    model = Post
    extra_context = {
        'title': 'SkyVillage',  # дополнение к статической информации
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        if self.request.user.has_perm('blog.can_change_post'):
            return queryset
        return queryset


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.increase_views()
        if obj.view_count == 100:
            send_post_email(obj)
        return obj


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('name', 'content', 'image', 'is_published', 'user',)
    success_url = reverse_lazy('blog:post_list')

    def get_initial(self):
        return {'user': self.request.user}

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('name', 'content', 'image', 'is_published', 'user',)

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', args=[str(self.object.slug)])


def toggle_publish(request, slug):
    """
    Функция переключения поста.
    """
    post_detail = get_object_or_404(Post, slug=slug)
    if post_detail.is_published:
        post_detail.is_published = False
    else:
        post_detail.is_published = True

    post_detail.save()

    return redirect(reverse('blog:post_list'))


class PostAllListView(LoginRequiredMixin, ListView):
    model = Post
    extra_context = {
        'title': 'Все записи SkyVillage',  # дополнение к статической информации
    }

