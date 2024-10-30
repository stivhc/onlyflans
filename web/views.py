from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import ContactForm, Flan
from .forms import ContactFormForm, ContactFormModelForm, UserRegisterForm


def index(request):
    public_flans = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"public_flans": public_flans})


def acerca(request):
    return render(request, "about.html", {})


@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(request, "welcome.html", {"private_flans": private_flans})


def contacto(request):
    if request.method == "POST":
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("exito")
    else:
        form = ContactFormModelForm()
    return render(request, "contact.html", {"form": form})


def exito(request):
    return render(request, "success.html", {})


def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # El método '.save()' permite guardar en la BD el registro de la variable 'form'
            form.save()
            # Se inicia la sesión  del usuario inmediatemente después del registro.
            usuario = form.cleaned_data["username"]
            contrasena = form.cleaned_data["password1"]
            new_user = authenticate(username=usuario, password=contrasena)
            login(request, user=new_user)
            # Se agrega un mensaje de éxito.
            messages.success(request, f"Usuario {usuario} registrado exitosamente.")
            # Redirección a la página de inicio
            return HttpResponseRedirect("web")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


def buscaflanes(request):
    if request.method == "POST":
        # 'buscador' guarda el valor ingresado en el formulario de búsqueda.
        buscador = request.POST["buscador"]
        # Filtrar los distintos objetos flanes para que coincidan con nuestro
        # criterio de búsqueda. En este caso, con el nombre de cada flan.
        flanes = Flan.objects.filter(name__contains=buscador)
        return render(
            request,
            "results_flans.html",
            {
                "buscador": buscador,
                "flanes": flanes,
            },
        )
    else:
        return render(request, "results_flans.html", {})
