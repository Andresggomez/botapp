from django import forms
# Create your forms here!

class formularioUsuario(forms.Form):

    nombre = forms.CharField(label= "Nombre", required=True, max_length=30)
    apellidos = forms.CharField(label= "Apellidos", required=True, max_length=30)
    email = forms.EmailField(label= "Email", required=True)
    password = forms.CharField(label= "Password", required=True)
    API_KEY = forms.CharField(label= "API Bot Publica", max_length=65)
    API_SECRET_KEY = forms.CharField(label= "API Bot Privada", max_length=65)
    protecionDatos = forms.BooleanField(label= "Politica de Datos", required=True)
    avisoTelegram = forms.CharField(label= "Usuario Telegram")
