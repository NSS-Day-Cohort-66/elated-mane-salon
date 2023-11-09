"""Appointment class module"""
from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    """Appointment model class"""
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    stylist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upcoming_appointments')
    prepaid = models.BooleanField(default=False)
    appointment_date = models.DateField(auto_now=False, auto_now_add=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments_scheduled')
