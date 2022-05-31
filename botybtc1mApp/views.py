from django.shortcuts import render
from botlogicApp.main import BotyBinance
from .strategy import Indicadores
import pandas as pd
from time import sleep
import requests
from .config import bot_token, bot_chatID

# Create your views here.

def botybtc1m(request):
    bot = BotyBinance("btcusdt", "1m")  # Nombre y temporalidad

    def info():

        return Indicadores(bot.candlestick()).crearDatos()

    btc1m = info()

    return render(request, "datos/datos.html")

