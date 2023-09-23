from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from main.apps import MainConfig
from .views import *


app_name = MainConfig.name


urlpatterns = [
    path('', IndexView.as_view(),  name='index'),  # http://127.0.0.1:8000/
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_view'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('sending/', SendingListView.as_view(), name='sending_list'),
    path('sending/<int:pk>/', SendingDetailView.as_view(), name='sending_view'),
    path('sending/create/', SendingCreateView.as_view(), name='sending_create'),
    path('sending/update/<int:pk>/', SendingUpdateView.as_view(), name='sending_update'),
    path('sending/delete/<int:pk>/', SendingDeleteView.as_view(), name='sending_delete'),
    path('attempt/', AttemptListView.as_view(), name='attempt_list'),
    path('attempt/<int:pk>/', AttemptDetailView.as_view(), name='attempt_view'),
    path('set_status_sending/<int:pk>', login_required(set_status_sending), name='set_status_sending'),
    path('set_is_active/<int:pk>', login_required(set_is_active), name='set_is_active'),
]

