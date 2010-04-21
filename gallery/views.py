from content.generic.views import GenericObjectDetail, GenericObjectList 
from gallery.models import Gallery

class ObjectList(GenericObjectList):
    def get_queryset(self):
        return Gallery.permitted.all()

    def get_extra_context(self):
        return {'title': 'Galleries'}

object_list = ObjectList()

class ObjectDetail(GenericObjectDetail):
    def get_queryset(self):
        return Gallery.permitted.all()
    
    def get_extra_context(self):
        return {'title': 'Galleries'}

object_detail = ObjectDetail()
