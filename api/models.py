from django.db import models

# Create your models here.

class SongLyric(models.Model):
    name = models.CharField(max_length=40)
    album = models.CharField(max_length=40)
    singer = models.CharField(max_length=40)
    writer = models.CharField(max_length=40)
    music = models.CharField(max_length=40)
    slug = models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    image = models.ImageField(upload_to="songs")
    publish = models.DateField()
    lyrics = models.TextField()

    def __str__(self):
        return self.name
    
class SongCollection(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    songs = models.ManyToManyField(SongLyric, blank=True)
    image = models.ImageField(upload_to="collections")

    def __str__(self):
        return self.title