import requests as r


apikey = "cc4e9df7f3733285633974da76abdb0df41162527e2452f8f88bcf70bacd267a"

response = r.get("https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=10&api_key=" + apikey)
print(response.json())


 