from django.contrib import admin
from .models import SongLyric, SongCollection
# Register your models here.

admin.site.register((SongLyric, SongCollection))