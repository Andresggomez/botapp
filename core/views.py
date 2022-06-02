from django.shortcuts import render, redirect, HttpResponse
from noticiaApp.models import Noticia
from usuariosApp.forms import formularioUsuario
from django.core.mail import EmailMessage
from carro.carro import Carro

# Create your views here.

def inicio(request):

    carro = Carro(request)
    return render(request, "core/home.html")

def boty(request):
    return render(request, "core/boty.html")

def activos(request):
    return render(request, "core/activos.html")

def noticias(request):
    consultadb = Noticia.objects.all()
    return render(request, "core/noticias.html", {"Noticia":consultadb})

def contacto(request):
    return render(request, "core/contacto.html")

def registro(request):

    form_usuario = formularioUsuario()

    if request.method=="POST":
        form_usuario= formularioUsuario(data=request.POST)
        if form_usuario.is_valid():

            nombre =request.POST.get("Nombre")
            apellidos =request.POST.get("Apellidos")
            email =request.POST.get("Email")
            password =request.POST.get("Password")
            API_KEY =request.POST.get("API Bot Publica")
            API_SECRET_KEY =request.POST.get("API Bot Privada")
            protecionDatos =request.POST.get("Politica de Datos")
            avisoTelegram =request.POST.get("Usuario Telegram")

            nuevoemail=EmailMessage("Registro Boty Señales",
                               "El usuario {} con email {} acaba de resgistrase en boty.com".format(nombre, email),
                               "",
                               ["soporteboty@gmail.com"],
                               reply_to=[email])
            try:
                nuevoemail.send()
                return redirect("/registro") #  retorna valido cuando registra en el modelo
            except:
                return redirect("/contacto")  # retorna valido cuando registra en el modelo

    return render(request, "core/registro.html", {'formulario':form_usuario})






