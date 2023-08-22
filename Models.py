from django.db import models

class Getting_Prices(models.Model): 
    Name = models.CharField(max_length= 255)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    
