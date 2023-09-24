from random import sample
import django

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from blog.models import Post
from main.models import *
from main.services import send_email_to_clients
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'SkyForest',
        'object_list': Sending.objects.all()
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_posts = list(Post.objects.filter(is_published=True))
        context['random_blog_posts'] = sample(all_posts, min(3, len(all_posts)))
        return context


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'object_list': Client.objects.all(),
        'title': 'Все клиенты'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('main.can_view_client'):
            return queryset
        return Client.objects.filter(created_by=self.request.user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    extra_context = {
        'title': 'Детали клиента'
    }


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('name', 'email', 'comment', 'author', 'created_by')
    success_url = reverse_lazy('main:client_list')

    def form_valid(self, form):
        """Метод добавления создателя клиента"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'email', 'comment', 'author', 'created_by', 'is_active')

    def get_success_url(self):
        return reverse('main:client_detail', args=[str(self.object.pk)])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('main:client_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'message_list': Message.objects.all(),
        'title': 'Все Сообщения'
    }


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    success_url = reverse_lazy('main:message_list')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ('subject', 'body', 'author', 'user',)
    success_url = reverse_lazy('main:message_list')

    def form_valid(self, form):
        """Метод добавления создателя сообщения"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ('subject', 'body', 'author', 'user',)

    def get_success_url(self):
        return reverse('main:message_view', args=[str(self.object.pk)])


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('main:message_list')


class SendingListView(LoginRequiredMixin, ListView):
    model = Sending
    extra_context = {
        'object_list': Sending.objects.all(),
        'title': 'Все Рассылки'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('main.can_view_sending'):
            return queryset
        return Sending.objects.filter(created=self.request.user)


class SendingDetailView(LoginRequiredMixin, DetailView):
    model = Sending


class SendingCreateView(LoginRequiredMixin, CreateView):
    model = Sending
    fields = ('message', 'frequency', 'status', 'author', 'created', 'start_date', 'end_date',)
    success_url = reverse_lazy('main:sending_list')

    def form_valid(self, form):
        """Метод добавления создателя сообщения"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    try:
        for send in Sending.objects.all():
            if send.status == Sending.CREATED:
                send_email_to_clients(Sending.ONCE)
    except django.db.utils.ProgrammingError:
        print('ProgrammingError')


class SendingUpdateView(LoginRequiredMixin, UpdateView):
    model = Sending
    fields = ('message', 'frequency', 'status',)

    def get_success_url(self):
        return reverse('main:sending_view', args=[str(self.object.pk)])


class SendingDeleteView(LoginRequiredMixin, DeleteView):
    model = Sending
    success_url = reverse_lazy('main:sending_list')


class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    extra_context = {
        'object_list': Attempt.objects.all(),
        'title': 'Статистика рассылок'
    }


class AttemptDetailView(LoginRequiredMixin, DetailView):
    model = Attempt
    extra_context = {
        'title': 'Детали рассылки'
    }


def set_is_active(request, pk):
    client_item = get_object_or_404(Client, pk=pk)
    if client_item.is_active:
        client_item.is_active = False
    else:
        client_item.is_active = True
    client_item.save()
    return redirect(reverse('main:client_list'))


def set_status_sending(request, pk):
    sending_item = get_object_or_404(Sending, pk=pk)
    if sending_item.status == Sending.CREATED:
        sending_item.status = Sending.COMPLETED
        sending_item.save()
    else:
        sending_item.status = Sending.CREATED
        sending_item.save()
    return redirect(reverse('main:sending_list'))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
