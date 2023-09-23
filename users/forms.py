from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import User


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(FormStyleMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'country', 'first_name', 'last_name', 'avatar', 'phone', 'messenger',)

    def __init__(self, *args, **kwargs):
        """
        Метод инициализирует сокрытие пароля при вводе.
        """
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserRegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'country',)
