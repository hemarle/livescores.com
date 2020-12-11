from django.db import models

# Create your models here.
class Score(models.Model):
    home_team= models.CharField(max_length=500)
    away_team= models.CharField(max_length=500)
    home_score= models.IntegerField(default=0)
    away_score=  models.IntegerField(default=0)
    time= models.CharField(max_length=30)