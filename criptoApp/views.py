from django.shortcuts import render

# Create your views here.

def cripto(request):

    return render(request, "cripto/cripto.html")
