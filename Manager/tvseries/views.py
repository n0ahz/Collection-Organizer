from django.shortcuts import render

# Create your views here.
def index(request, **kwargs):
    return render(request, 'tvseries/index.html')


def settings(request, **kwargs):

    from Manager.models import LibraryPath
    #from movies.models import Movie

    if request.GET.get('path'):
        path_to_delete = LibraryPath.objects.filter(path=request.GET.get('path'), type='tvseries')
        for each in path_to_delete:
            each.delete()

    paths = LibraryPath.objects.filter(type='tvseries')
    #movies = Movie.objects.all()
    shows = []

    context = {'paths': paths, 'media_list': shows, 'item': 'TV Series', 'app':'tvseries'}

    return render(request, 'tvseries/settings.html', context)