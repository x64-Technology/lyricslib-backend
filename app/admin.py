from django.contrib import admin
from .models import SongLyrics, SongCollection
# Register your models here.

admin.site.register((SongLyrics, SongCollection))