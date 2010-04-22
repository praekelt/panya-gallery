from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'gallery.views',
    url(r'^list/$', 'object_list', name='gallery_object_list'),
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='gallery_object_detail'),
)
