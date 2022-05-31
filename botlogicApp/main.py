from .strategy import Indicadores
from binance.spot import Spot
import pandas as pd  # Pandas
from time import sleep
import requests
from .config import API_KEY, API_SECRET_KEY, bot_token, bot_chatID

class BotyBinance:
    """
    Bot de señales, compras / ventas en el mercado de Criptomonedas VOLUMEN TOTAL $xx millones
    """
    # Variables de clase privadas __apis
    __api_key = API_KEY  # API de usuario Publica
    __api_secret = API_SECRET_KEY
    binance_client = Spot(key=__api_key, secret=__api_secret)  # guarda la conexion

    def __init__(self, pair: str, temporality: str):  # Inicializa parametros

        # Variables de instancia
        self.pair = pair.upper()  # BTC/USDT
        self.temporality = temporality  # 4h, 15m
        self.symbol = self.pair.removesuffix("USDT")

    def _request(self, endpoint: str, parameters: dict = None):  # Conexion usuario/API
        """
        #endpoits son las funiones de la api, account, klines etc.
        Log de errores
        :return: response con informacion de errores en casos fallido, 
        """
        try:
            response = getattr(self.binance_client, endpoint)
            return response() if parameters is None else response(**parameters)
        except:
            print(f'el endopoint {endpoint} ha fallado.\n Parametros: {parameters}\n\n')
            sleep(2)

    def binance_account(self):
        """
        Devuelve estado de cuenta general con referencia a la API
        :return: Cuenta de binance. ->Dic [datos]
        """

        return self._request('account')

    def criptomonedas(self) -> list[dict]:
        """
        Devuelve una lista de diccionarios en con las cuentas que tienen un saldo
        :return: Critomonedas con saldo 
        """
        lista = self.binance_account().get('balances')

        return [crypto for crypto in lista if float(crypto.get('free')) > 0]

    def precio(self, pair: str = None):
        """
        Calcula precio en tiempo real de un activo digital pair:"BTCUSDT", temporality:"4h"
        :return: valor flotante del precio actual
        """

        symbol = self.pair if pair is None else pair

        return float(self._request('ticker_price', {'symbol': symbol.upper()}).get('price'))
    
    def candlestick(self, limit: int = 565) -> pd.DataFrame:
        """
        Se calcula el intervalo de tiempo de casa vela para analisar
        :return: Un data Frame de tipo pandas, un candle!

        """
        
        params = {
            'symbol': self.pair, 
            'interval': self.temporality,
            'limit': limit
        }
        
        candle = pd.DataFrame(self._request(
            'klines',
            params
        ),

            columns=[
                'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
                'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
                'Taker buy quote asset volume', 'Ignore'
            ],
            dtype=float
        )
        return candle[['Open', 'High', 'Low', 'Close', 'Volume', 'Number of trades']]

#  pprint(bot.binance_account())
#  pprint(type(bot.binance_account()))
# pprint(bot.criptomonedas())  # saldos en crypto de la cuenta

#  pprint(bot.candlestick())
#  mensaje =  bot.candlestick()
#  bot.mensajeALerta(mensaje)
#  precioActual= bot.candlestick()
#  pprint(precioActual)
#  pprint(bot.precio())

#  Calcula el valor del indicador
#  pprint(Indicadores(bot.candlestick()).rsi(14))
 #Indicadores(bot.candlestick()).grafica_adx()

if __name__ == '__main__':

    bot = BotyBinance("btcusdt", "1m")  # Nombre y temporalidad

    print("Boty Online.... ----> btcusdt 1m \ncontador")
    compra = 0
    venta = 0
    poscicionLarga = 2
    poscicionCorta = 1
    columns = ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION', 'CortoE', 'LargoE']

    #  LogBoty.csv
    df = pd.DataFrame(columns=columns)

    #  Calcular el valor de la ema20 fin de COBRAR C/V
    #  Calcular divergencias
    #  Mensajes
    #  email?


    def mensaje(msj):

        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + msj

        response = requests.get(send_text)

        return response

    def info():

        return Indicadores(bot.candlestick()).crearDatos()

    #btc1m = info()

    while True:

        ema200 = Indicadores(bot.candlestick()).ema(200)
        rsi = Indicadores(bot.candlestick()).rsi(14)
        precio = bot.precio()
        ultimo = len(df.index)
        
        if 35 > rsi and precio > ema200:
            compra = compra + 1
            print(compra)

            if compra == 3 and poscicionLarga == 0:  # señal de posible oportunidad LONG
                compra = 0
                poscicionLarga = 1
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f1'
                tendencia = 'Alcista'
                recomendacion = 'SEÑAL LONG/ Precio bajo y subiendo'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje
                señal = df.loc[[ultimo], ['ESTADO', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))

            elif compra == 3 and poscicionLarga == 1:  # compra en casa de cambio
                compra = 0
                poscicionLarga = 2
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f1'
                tendencia = 'Alcista'
                recomendacion = 'COMPRAR LONG/'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                señal = df.loc[[ultimo], ['ESTADO', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))


            elif compra == 4 and poscicionLarga == 2:  #
                compra = 0
                poscicionCorta = 0  # COBRAR CORTO FASE ANTERIOR
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f1'
                tendencia = 'Alcista'
                recomendacion = 'COMPRADO / precio entrada, venta short'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje

                señal = df.loc[[ultimo], ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))

            else:
                precio = str(int(precio))
                rsi = str(int(rsi))
                estado = 'f1'
                tendencia = 'Alcista'
                recomendacion = 'ESPERANDO SEÑAL'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

        elif 35 > rsi and precio < ema200:
            compra = compra + 1
            print(compra)

            if compra == 3 and poscicionLarga == 0:  # señal de posible oportunidad LONG
                compra = 0
                poscicionLarga = 1
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f1'
                tendencia = 'Bajista'
                recomendacion = 'SEÑAL LONG/ Precio muy bajo'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje

                señal = df.loc[[ultimo], ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))


            elif compra == 3 and poscicionLarga == 1:
                # compra en casa de cambio

                compra = 0
                poscicionLarga = 2
                precio = str(int(precio))
                rsi = str(int(rsi))
                estado = 'f1'
                tendencia = 'Bajista'
                recomendacion = 'COMPRA LONG/'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje

                señal = df.loc[[ultimo], ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))

            elif compra == 4 and poscicionLarga == 2:  # vender en BINANCE
                compra = 0
                poscicionCorta = 0
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f1'
                tendencia = 'Bajista'
                recomendacion = 'COMPRADO / precio entrada, venta short'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje

                señal = df.loc[[ultimo], ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))

            else:  # Inicia la secuencia de señal y confirmacion de compra de LONG, Vende la fase anterior
                precio = str(int(precio))
                rsi = str(int(rsi))
                estado = 'f1'
                tendencia = 'Bajista precio muy bajo'
                recomendacion = 'ESPERANDO SEÑAL LONG/Continuación'
                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

        elif 56 > rsi and precio > ema200:
            compra = 0
            precio = str(int(precio))
            rsi = str(int(rsi))

            estado = 'f2'
            tendencia = 'Alcista'
            recomendacion = 'NoC/V comprar f1'

            df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

        elif 56 > rsi and precio < ema200:
            compra = 0
            precio = str(int(precio))
            rsi = str(int(rsi))

            estado = 'f2'
            tendencia = 'Bajando'
            recomendacion = 'NoC/V comprarf1'
            poslarga = poscicionLarga
            poscorto = poscicionCorta

            df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

        elif 65 > rsi and precio > ema200:
            compra = 0
            precio = str(int(precio))
            rsi = str(int(rsi))

            estado = 'f3'
            tendencia = 'Alcista'
            recomendacion = 'NoC/V comprarf1'

            df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

        elif 65 > rsi and precio < ema200:
            compra = 0
            precio = str(int(precio))
            rsi = str(int(rsi))

            estado = 'f3'
            tendencia = 'Bajista'
            recomendacion = 'NoC/V comprarf1'

            df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

        elif 99 > rsi and precio > ema200:

            compra = compra + 1
            print(compra)

            if compra == 4 and poscicionCorta == 0:  # señal de posible oportunidad SHORT
                compra = 0
                poscicionCorta = 1
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f4'
                tendencia = 'Alcista'
                recomendacion = 'SEÑAL SHORT/70% VENDER Fase anterior'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje

                señal = df.loc[[ultimo], ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))

            elif compra == 4 and poscicionCorta == 1:
                # compra en casa de cambio
                compra = 0
                poscicionCorta = 2

                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f4'
                tendencia = 'Alcista'
                recomendacion = 'COMPRA SHORT/70%'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje

                señal = df.loc[[ultimo], ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))

            elif compra == 4 and poscicionCorta == 2:
                compra = 0
                poscicionLarga = 0
                #  vender en BINANCE
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f4'
                tendencia = 'Alcista precio alto'
                recomendacion = 'COMPRADO / COBRAR LONG'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje

                señal = df.loc[[ultimo], ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))

            else:
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f4'
                tendencia = 'precio muy alto'
                recomendacion = 'COBRAR confirmacion? LONG'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

        elif 99 > rsi and precio < ema200:
            compra = compra + 1
            print(compra)

            if compra == 4 and poscicionCorta == 0:  # señal de posible oportunidad
                compra = 0
                poscicionCorta = 1
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f4'
                tendencia = 'Bajista cruce avg?'
                recomendacion = 'SEÑAL SHORT/ VENDER Fase anterior'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje

                señal = df.loc[[ultimo], ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))

            elif compra == 4 and poscicionCorta == 1:  # compra en casa de cambio
                # pprint(f"f1 Señal CONFIRMACION compra SHORT : $ {precio} count :{compra}")
                compra = 0
                poscicionCorta = 2
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f4'
                tendencia = 'Bajista'
                recomendacion = 'COMPRA SHORT/ GRAFICA'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje

                señal = df.loc[[ultimo], ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))

            elif compra == 4 and poscicionCorta == 2:  #
                compra = 0
                #  vender en BINANCE
                poscicionLarga = 0

                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f5'
                tendencia = 'Bajista'
                recomendacion = 'COMPRADO / precio entrada'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

                #  Envio de mensaje

                señal = df.loc[[ultimo], ['RSI', 'ESTADO', 'TENDENCIA', 'PRECIO', 'RECOMENDACION']]
                mensaje(str(señal))

            else:
                precio = str(int(precio))
                rsi = str(int(rsi))

                estado = 'f4'
                tendencia = 'Subiendo mas alto'
                recomendacion = 'COBRAR, C SHORT'

                df.loc[ultimo] = [rsi, estado, tendencia, precio, recomendacion, poscicionCorta, poscicionLarga]

        df.to_csv('logboty.csv')

        #  valor de divergencias y ema20

        sleep(45)
