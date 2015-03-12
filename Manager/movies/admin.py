from django.contrib import admin

from movies.models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    #extra modification of the admin page...
    list_display = ['title', 'present']
    list_filter = ['title']
    search_fields = ['title']
    fieldsets = [
        ('Movie Name',{'fields': ['title']}),
        ('Details', {'fields': ['year', 'genre', 'type', 'duration', 'category', 'plot', 'tagline', 'rating', 'poster', 'cast', 'directors'], 'classes': ['']}),
        ('Current status', {'fields': ['present']}),
    ]

admin.site.register(Movie, MovieAdmin)
