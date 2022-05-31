from django.shortcuts import render

# Create your views here.

def botmain(request):
    return render(request, "bot/bot.html")

def error(request):
    return render(request, "error/error.html")
