import re

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string

from gallery.models import Gallery, GalleryItem
from panya.generic.views import GenericObjectDetail, GenericObjectList 
from panya.view_modifiers import DefaultViewModifier

from photologue.models import PhotoSize

def galleryimage_response(context):
    template = "gallery/ajax/galleriffic_galleryimage.html"
    return render_to_string(template, context)
    
def videoembed_response(context):
    template = "gallery/ajax/galleriffic_videoembed.html"
    result = render_to_string(template, context)

    try:
        photosize = context['object'].get_videoembed_large_photosize()
    except AttributeError:
        return result
        
    result = re.sub('width=".{0,4}"', 'width="%s"' % photosize.width, result)
    result = re.sub('height=".{0,4}"', 'height="%s"' % photosize.height, result)
    return result
    
def videofile_response(context):
    # grab a photosize and fallback to default if not available
    try:
        photosize = context['object'].get_videofile_large_photosize()
        width = photosize.width
        height = photosize.height
    except AttributeError:
        # TODO: get some better way to specify defaults
        width = 500
        height = 300
   
    context.update({
        'width': width,
        'height': height,
    })
    template = "gallery/ajax/galleriffic_videofile.html"
    return render_to_string(template, context)

def gallery_item_ajax_galleriffic(request, slug):
    try:
        obj = GalleryItem.permitted.filter(slug=slug).get()
    except GalleryItem.DoesNotExist:
        raise Http404

    obj = obj.as_leaf_class()

    options = {
        'GalleryImage': galleryimage_response,
        'VideoEmbed': videoembed_response,
        'VideoFile': videofile_response,
    }
    
    context = {'object':  obj}
    result = options[obj._meta.object_name](context)
    return HttpResponse(result)

class ObjectList(GenericObjectList):
    def get_extra_context(self, *args, **kwargs):
        return {'title': 'Galleries'}
        
    def get_view_modifier(self, request, *args, **kwargs):
        return DefaultViewModifier(request, *args, **kwargs)

    def get_paginate_by(self, *args, **kwargs):
        return 12
    
    def get_queryset(self, *args, **kwargs):
        return Gallery.permitted.all()

object_list = ObjectList()

class ObjectDetail(GenericObjectDetail):
    def get_queryset(self, *args, **kwargs):
        return Gallery.permitted.all()
    
    def get_extra_context(self, *args, **kwargs):
        return {'title': 'Galleries'}
    
    def get_view_modifier(self, request, *args, **kwargs):
        return DefaultViewModifier(request, base_url=reverse("gallery_object_list"), ignore_defaults=True, *args, **kwargs)
    
object_detail = ObjectDetail()
