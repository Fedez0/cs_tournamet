from django.db import models
from core.models import User
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='team_icons/', blank=True, null=True)
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']