from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'gallery.views',
    url(r'^list/$', 'object_list', name='gallery_object_list'),
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='gallery_object_detail'),
    url(r'^item/ajax/galleriffic/(?P<slug>[\w-]+)/$', 'gallery_item_ajax_galleriffic', name='gallery_item_ajax_galleriffic'),
)
