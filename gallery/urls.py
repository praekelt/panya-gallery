from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'gallery.views',
    url(r'^listing/$', 'object_listing', name='gallery_object_listing'),
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='gallery_object_detail'),
)
