from django.shortcuts import render 
import requests 

import Website.Models as models

def Crypto_Prices(request):

    # Make an API request to get the Crypto prices from Coinbase
    response = requests.get('https://api.exchange.coinbase.com/accounts')

    price = response.json()['price']

    # Pass the price to the template for rendering 
    context = {"price": price}
    
    crypto = models.objects.all()
    
    # Return the render from the Crypto prices function so you can get prices via request
    return render(request, 'crypto_prices.html', context)




