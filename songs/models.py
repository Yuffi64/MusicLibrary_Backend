from secrets import choice
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    album = models.CharField(max_length=150)
    release_date = models.DateField()
    genre = models.CharField(max_length=150)
#    likes = models.ManyToManyField(User, default=None, blank=True, related_name='like')
    
#    @property
#    def num_likes(self):
#        return self.liked.all().count()
    
#Like_CHOICES = (
#    ('like','like'),
#    ('unlike','unlike')
#)
    
#class Like(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    song = models.ForeignKey(Song, on_delete=models.CASCADE)
#    Value = models.CharField(choices=Like_CHOICES, default='like',max_length=5)