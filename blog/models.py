from django.conf import settings
from django.db import models
from django.utils import timezone


class Team(models.Model):
    TName = models.CharField(max_length=200)
    text = models.TextField()
    funds = models.IntegerField()

    def __str__(self):
        return self.TName

class Player(models.Model):
    TName= models.ForeignKey(Team, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name