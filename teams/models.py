from django.db import models
from core.models import User
# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='team_icons/', default='team_icons/default.png')
    members = models.ManyToManyField(User, related_name='teams')
    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='led_teams')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']