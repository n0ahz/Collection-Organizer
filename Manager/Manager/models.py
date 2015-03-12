from django.db import models


class LibraryPath(models.Model):
    """Defines the db for storing HDD paths for importing Media Collection"""
    path = models.CharField(max_length=500)
    type = models.CharField(max_length=100)

    '''
    def __init__(self, path, type):
        self.path = path
        self.type = type
    '''
    class Meta:
        unique_together = ['type', 'path']

    def __str__(self):
        return self.type + " : " + self.path