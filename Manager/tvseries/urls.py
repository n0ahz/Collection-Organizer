from django.conf.urls import patterns, url

from tvseries import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^settings/$', views.settings, name='settings'),
)
