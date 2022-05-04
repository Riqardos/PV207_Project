from django.db import models

class Vehicle(models.Model):
    STATE_CHOICES = [
        ('U', 'in use'),
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

class Incident(models.Model):
    STATE_CHOICES = [
        ('P', 'pending'),
        ('I', 'in progress'),
        ('R', 'resolved'),
        ('D', 'declined'),
    ]
    description = models.CharField(max_length=200)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=1,
        choices=STATE_CHOICES,
        default='P',
    )