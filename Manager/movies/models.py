from django.db import models

# Create your models here.
#once the db table is created from the model, it cant be recreated...so updates cant be synced with syncdb
class Movie(models.Model):

    title = models.CharField(max_length=200)

    #from directory or imdb?
    year = models.CharField(max_length=10,blank=True)
    #other info from imdb here
    genre = models.CharField(max_length=200,blank=True)
    type = models.CharField(max_length=200,blank=True)
    duration = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=200,blank=True)
    plot = models.TextField(blank=True)
    tagline = models.TextField(null=True,blank=True)
    rating = models.CharField(max_length=200,blank=True)
    #some db values will not be shown even in admin form
    poster = models.TextField(max_length=200,blank=True)
    cast = models.TextField(max_length=600,blank=True)
    directors = models.TextField(max_length=200,blank=True)
    #present or not....once seen its stored in db
    present = models.BooleanField()

    def __str__(self):
        return self.title