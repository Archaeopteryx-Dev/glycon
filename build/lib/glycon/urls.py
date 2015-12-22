from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^content/(?P<page_name>[\w-]+)/', 'glycon.views.content', name='content'),
                       url(r'^$', 'glycon.views.home', name='home'),
                       )
