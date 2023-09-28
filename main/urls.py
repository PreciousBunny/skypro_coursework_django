from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.views.decorators.cache import never_cache, cache_page

from main.apps import MainConfig
from .views import *


app_name = MainConfig.name


urlpatterns = [
    path('', never_cache(IndexView.as_view()),  name='index'),  # http://127.0.0.1:8000/
    path('client/',  cache_page(60)(ClientListView.as_view()), name='client_list'),
    path('client/<int:pk>/', never_cache(ClientDetailView.as_view()), name='client_detail'),
    path('client/create/', never_cache(ClientCreateView.as_view()), name='client_create'),
    path('client/update/<int:pk>/', never_cache(ClientUpdateView.as_view()), name='client_update'),
    path('client/delete/<int:pk>/', never_cache(ClientDeleteView.as_view()), name='client_delete'),
    path('message/', cache_page(60)(MessageListView.as_view()), name='message_list'),
    path('message/<int:pk>/', never_cache(MessageDetailView.as_view()), name='message_view'),
    path('message/create/', never_cache(MessageCreateView.as_view()), name='message_create'),
    path('message/update/<int:pk>/', never_cache(MessageUpdateView.as_view()), name='message_update'),
    path('message/delete/<int:pk>/', never_cache(MessageDeleteView.as_view()), name='message_delete'),
    path('sending/', cache_page(60)(SendingListView.as_view()), name='sending_list'),
    path('sending/<int:pk>/', cache_page(60)(SendingDetailView.as_view()), name='sending_view'),
    path('sending/create/', never_cache(SendingCreateView.as_view()), name='sending_create'),
    path('sending/update/<int:pk>/', never_cache(SendingUpdateView.as_view()), name='sending_update'),
    path('sending/delete/<int:pk>/', never_cache(SendingDeleteView.as_view()), name='sending_delete'),
    path('attempt/', cache_page(60)(AttemptListView.as_view()), name='attempt_list'),
    path('attempt/<int:pk>/', cache_page(60)(AttemptDetailView.as_view()), name='attempt_view'),
    path('set_status_sending/<int:pk>', login_required(set_status_sending), name='set_status_sending'),
    path('set_is_active/<int:pk>', login_required(set_is_active), name='set_is_active'),
]

