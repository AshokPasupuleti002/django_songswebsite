from django.contrib import admin
from .models import Movie, Audio, Video

# Register your models here.

admin.site.register(Movie)
admin.site.register(Audio)
admin.site.register(Video)
