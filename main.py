import requests
import json
import subprocess as sp
from flask import Flask, render_template

from requests import api



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



@app.route("/")
@app.route("/home")
def home():
    printF(getCryptoData('BTC'))
    printF(getCryptoData('ETH'))
    print('$' + str(getDiff(getCryptoData('BTC'), getCryptoData('ETH'))))

    return render_template('index.html', diff=getDiff(getCryptoData('BTC'), getCryptoData('ETH')))


@app.route("/searchTag/<userInfo>", methods=['POST'])
def searchTag(userInfo):
    userInfo = json.loads(userInfo)
    print('tag received')
    print(f"user selected tag: {userInfo['tag']}")

    return 'info received sucessfully'




@app.route("/Calculator")
def Calculator():
    return "<h1>Calculator</h>"

if __name__ == "__main__":
    app.run(debug=True)
