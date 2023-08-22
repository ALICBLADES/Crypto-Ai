import Views

# Function for putting all the informaiton of a crypto in the database
def Retrieving(Info, Crypto_Prices):
    for Crypto in Info:
        currency = Views.Cryptocurrency.object.create(
             name = ['crypto'],
             price = ['price'],
             symbol = ['symbol'] 
             
        )