import requests
import json
import subprocess as sp
from flask import request
from flask import Flask, render_template

from requests import NullHandler, api



app = Flask(__name__)
kFile = open("key.txt", "r")
api_key = kFile.readline()



def getCryptoData(symbol):
    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + symbol + '&tsyms=USD&api_key=' + api_key
    r = requests.get(url)
    data = r.json()

    info = data['RAW'][symbol]['USD']
    return info
    

def getDiff(crypto1, crypto2):
    temp = crypto1['PRICE'] - crypto2['PRICE']
    return temp




def printF(info):
    print(str(info['FROMSYMBOL']) + " price: $" + str(info['PRICE']))


def main():
    printF(getCryptoData('BTC'))
    printF(getCryptoData('ETH'))
    print('$' + str(getDiff(getCryptoData('BTC'), getCryptoData('ETH'))))


#---------------------------------------------------------------------------


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', diff=getDiff(getCryptoData('BTC'), getCryptoData('ETH')))


@app.route("/search", methods=['GET', 'POST'])
def searchTag():
    tag = NullHandler
    if request.method == "POST":
        tag = request.form['q']
        return render_template('search.html', tag=tag)
    else:
        return render_template('search.html', tag=tag)


if __name__ == "__main__":
    app.run(debug=True)