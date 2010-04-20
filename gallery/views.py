from django.views.generic import list_detail
from gallery.models import Gallery

def object_listing(request):
    return list_detail.object_list(
        request,
        queryset = Gallery.permitted.all(),
        template_name = 'gallery/gallery_listing.html'
    )
