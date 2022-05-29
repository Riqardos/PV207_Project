from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    STATE_CHOICES = [
        ('U', 'in_use'),
        ('I', 'idle'),
        ('S', 'in_service'),
        ('M', 'maintanance'),
        ('D', 'disabled'),
    ]
    model = models.CharField(max_length=40)
    vin = models.CharField(max_length=40)
    state = models.CharField(
        max_length=1,
        choices=STATE_CHOICES,
        default='D',
    )

    def __str__(self) -> str:
        return f"{self.model} - {self.vin}"

class Incident(models.Model):
    STATE_CHOICES = [
        ('P', 'pending'),
        ('I', 'in_progress'),
        ('R', 'resolved'),
        ('D', 'declined'),
    ]
    TYPE_CHOICES = [
        ('C', 'cleaning'),
        ('M', 'maintenance'),
    ]
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES, 
        default='C'
    )
    description = models.CharField(max_length=200)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.CharField(
        max_length=1,
        choices=STATE_CHOICES,
        default='P',
    )