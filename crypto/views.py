from django.shortcuts import render
from django.contrib import messages

def home(request):
    import requests
    import json
    # Grab Crypto Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR")
    price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    context = {
        'api': api,
        'price': price,
    }
    return render(request, 'crypto/home.html', context)

def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD,EUR")
        crypto = json.loads(crypto_request.content)

        context = {
            'quote': quote,
            'crypto': crypto,
        }
        return render(request, 'crypto/prices.html', context)
    else:
        import requests
        import json
        # Grab Crypto Price Data
        price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR")
        price = json.loads(price_request.content)

        context = {
            'price': price,
        }
        return render(request, 'crypto/prices.html', context)
