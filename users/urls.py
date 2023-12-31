from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.cache import never_cache


from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', ProfileUpdateView.as_view(), name='profile'),
    path('list', UserListView.as_view(), name='list'),
    path('register', RegisterView.as_view(), name='register'),
    path('activate/<str:token>', activate_user, name='activate'),
    path('page_after_registration/<str:token>', page_after_registration, name='page_after_registration'),
    path('profile/gennpassword', generate_new_password, name='generate_new_password'),
    path('set_is_active_users/<int:pk>', login_required(set_is_active_users), name='set_is_active_users'),
]