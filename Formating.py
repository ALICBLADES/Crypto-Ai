import coinbase

import Website.Views as Views 

def Formating_prices(prices):
    
    client = Views.Crypto_Prices(prices)
    
    for clients in client:
        charges = clients 
        if charges != None: 
           staged = print("{!r}".format(charges))
           return staged
        else: 
           return  None
        



