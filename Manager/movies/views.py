from django.shortcuts import render


# Create your views here.
def index(request, **kwargs):
    return render(request, 'movies/index.html')


def settings(request, **kwargs):

    from Manager.models import LibraryPath
    from movies.models import Movie

    if request.GET.get('path'):
        path_to_delete = LibraryPath.objects.filter(path=request.GET.get('path'), type='movies')
        for each in path_to_delete:
            each.delete()

    paths = LibraryPath.objects.filter(type='movies')
    movies = Movie.objects.all()

    context = {'paths': paths, 'media_list': movies, 'item': 'Movies', 'app':'movies'}

    return render(request, 'movies/settings.html', context)