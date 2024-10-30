from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ContactForm


class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label = 'Correo')
    customer_name = forms.CharField(max_length = 64, label = 'Nombre')
    message = forms.CharField(widget = forms.TextInput(attrs={'class': 'mensaje'}), label = 'Mensaje')


class ContactFormModelForm(forms.ModelForm):
    message = forms.CharField(widget = forms.Textarea(attrs={'rows': '4', 'cols': '30', 'style': 'resize: none;'}))
    
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Correo electrónico")
    username = forms.CharField(label = "Nombre de usuario")
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput)

    class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']
            help_text = {k:"" for k in fields }
