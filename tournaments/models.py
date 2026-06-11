from django.db import models
from teams.models import Team
from core.models import User
# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=200)
    teams = models.ManyToManyField(Team, related_name='tournaments', blank=True)
    ## aperto / in corso / chiuso
    status = models.CharField(max_length=20, default='aperto')
    prize = models.CharField(max_length=200, blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='organized_tournaments')
    max_teams = models.PositiveIntegerField(default=16)
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_tournaments')
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date']