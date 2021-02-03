from django.db import models
from datetime import datetime
# Create your models here.
class Inquiry(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=11)
    message = models.TextField(blank = True)
    contact_date = models.DateField(default = datetime.now)
    user_id = models.IntegerField(blank = True)

    def __str__(self):
        return self.listing
     