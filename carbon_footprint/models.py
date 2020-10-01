from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


CHOICES = (
        ('option1', 'Yes'),
        ('option2', 'No'),
        ('option3', 'Yes'),
        ('option4', 'No'),
    )
class Carbon_footprint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    electric = models.IntegerField()
    gas = models.IntegerField()
    oil = models.IntegerField()
    car = models.IntegerField()
    flights = models.IntegerField()
    newspaper = models.CharField(max_length=10, choices=CHOICES)
    aluminium = models.CharField(max_length=10, choices=CHOICES)
    date        =  models.DateTimeField(default=timezone.now)

   
    def __str__(self):
        return f'{self.user.username} carbon_footprint'