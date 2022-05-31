from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

"""def nuevoUsuario(request):
    return render(request, "registro/registro.html)"""

class nuevoUsuario(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})  # formulario desde get

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()  # Guarda en tb auth_user, seguridad de la info
            login(request, usuario)
            return redirect('Inicio')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "registro/registro.html", {"form":form})

            #return redirect('Error404')  # Construir paginas de errores

def cerrar_sesion(request):
    logout(request)
    return redirect('Inicio')

def entrar(request):  # esto es una vista
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user=authenticate(username=nombre_usuario, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('Noticias')
            else:
                messages.error(request, "Usuario no encontrado")
        else:
            messages.error(request, "Informacion invalida")

    form = AuthenticationForm()
    return render(request, "entrar/entrar.html", {"form": form})
