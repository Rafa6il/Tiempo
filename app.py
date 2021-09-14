import json
import requests
import sys
from flask import Flask, request

app = Flask(__name__)

APIKEY = '67422af3a25ed304bc3f605989c25d03'  # your API Key here as string


def urlbuilder(citytmp):
    link = f"https://api.openweathermap.org/data/2.5/weather?lang=es&q={citytmp}&appid={APIKEY}&units=metric"
    return link


def model(res, citytmp):
    try:
        temp = res['main']['temp']
        resp = {
        "city": citytmp,
        "temperature": temp
        }
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        print("Error al decodificar JSON", sys.exc_info()[0])
    return resp


@app.route('/')
def service():  # put application's code here
    city = request.args.get('city')
    # Consultamos a la página la información de la ciudad, esperando que la devuelva en formato JSON
    url = urlbuilder(city)
    try:
        res = requests.get(url).json()
    except (requests.exceptions.Timeout, requests.exceptions.BaseHTTPError, requests.exceptions.ConnectionError):
        print("Something Unexpected has happened.", sys.exc_info()[0])
    response = model(res, city)

    return json.dumps(response)


if __name__ == '__main__':
    app.run()
