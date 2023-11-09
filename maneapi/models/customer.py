"""Customer class module"""
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """Customer model class"""
    name = models.CharField(max_length=50)
    style = models.ForeignKey("HairStyle", on_delete=models.CASCADE, related_name='customers')
    date_created = models.DateField(auto_now=True)
    stylists = models.ManyToManyField(User,
                                      through="Appointment",
                                      through_fields=('customer', 'stylist'),
                                      related_name='clients')
