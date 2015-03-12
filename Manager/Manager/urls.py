from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Manager.views.home', name='home'),
    url(r'^about$', 'Manager.views.about', name='about'),
    url(r'^admins$', 'Manager.views.admin', name='admin'),
    url(r'^na$', 'Manager.views.not_available', name='N/A'),
    url(r'^ff$', 'Manager.views.navigator', name='Navigator'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^movies/', include('movies.urls', namespace='movies')),
    url(r'^tv/', include('tvseries.urls', namespace='tvseries')),
    url(r'^toons/', include('toons.urls', namespace='toons')),

    url(r'^admin/', include(admin.site.urls)),

)
