from django.shortcuts import render


# Create your views here.
def index(request, **kwargs):
    return render(request, 'toons/index.html')


def settings(request, **kwargs):

    from Manager.models import LibraryPath
    #from movies.models import Movie

    if request.GET.get('path'):
        path_to_delete = LibraryPath.objects.filter(path=request.GET.get('path'), type='toons')
        for each in path_to_delete:
            each.delete()

    paths = LibraryPath.objects.filter(type='toons')
    #movies = Movie.objects.all()
    toons = []

    context = {'paths': paths, 'media_list': toons, 'item': 'Toons', 'app':'toons'}

    return render(request, 'toons/settings.html', context)