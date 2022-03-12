from flask import Flask, render_template
import datetime
import requests


app = Flask(__name__)

@app.get('/')
def index():
    time = datetime.datetime.now()
    response = requests.get("https://www.cbr-xml-daily.ru/latest.js")
    rates = response.json()["rates"]
    rates = {key: 1 / value for key, value in rates.items()}
    return render_template('index.html', time=time, rates=rates.items())

@app.get('/<currency>')
def get(currency):
    response = requests.get("https://www.cbr-xml-daily.ru/latest.js")
    rates = response.json()["rates"]
    rates = {key: 1 / value for key, value in rates.items()}
    if currency not in rates:
        currency = "USD"
    value = rates.get(currency, rates["USD"])
    return render_template('currency.html', currency=currency, value=value)