from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # newsletter_abo = models.BooleanField()
    # email_address = models.EmailField()
    # account = models.FloatField()