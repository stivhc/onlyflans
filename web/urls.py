from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index, acerca, bienvenido, contacto, exito, registro, buscaflanes

app_name = "web"

urlpatterns = [
    path("", index, name="índice"),
    path("acerca", acerca, name="acerca"),
    path("bienvenido", bienvenido, name="bienvenido"),
    path("contacto", contacto, name="contáctanos"),
    path("exito", exito, name="éxito"),
    path("registrar", registro, name="regístrate"),
    path("accounts/login", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login",),
    path("accounts/logout", auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout",),
    path("buscaflan", buscaflanes, name="búscalo"),
]
