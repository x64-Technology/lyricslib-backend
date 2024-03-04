from django.db import models

# Create your models here.

class SongLyrics(models.Model):
    name = models.CharField(max_length=40)
    album = models.CharField(max_length=40)
    singer = models.CharField(max_length=40)
    writer = models.CharField(max_length=40)
    image = models.ImageField(upload_to="public/songs")
    lyrics = models.TextField()

    title = f"${name} by ${singer} - ${album}"

    def __str__(self):
        return self.name
    
class SongCollection(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    songs = models.ManyToManyField(SongLyrics)
    image = models.ImageField(upload_to="public/collections")

    def __str__(self):
        return self.title