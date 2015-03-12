from django.contrib import admin

from Manager.models import LibraryPath
# Register your models here.


class PathsAdmin(admin.ModelAdmin):
    # extra modification of the admin page...
    list_display = ['type', 'path']


admin.site.register(LibraryPath, PathsAdmin)
