from django.conf.urls import patterns, include, url

from glycon import glycon_site

urlpatterns = patterns('',
                       url(r'^admin/', include(glycon_site.urls)),
                       url(r'^content/(?P<page_name>[\w-]+)/', 'glycon.views.content', name='content'),
                       url(r'^$', 'glycon.views.home', name='home'),
                       )
