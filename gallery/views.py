from content.generic.views import GenericObjectDetail, GenericObjectList 
from gallery.models import Gallery

class ObjectList(GenericObjectList):
    def get_queryset(self):
        
        return Gallery.permitted.all()

    def get_extra_context(self, *args, **kwargs):
        extra_context = super(ObjectList, self).get_extra_context(*args, **kwargs)
        added_context = {'title': 'Galleries'}
        if extra_context:
            extra_context.update(
                added_context,
            )
        else:
            extra_context = added_context

        return extra_context

object_list = ObjectList()

class ObjectDetail(GenericObjectDetail):
    def get_queryset(self):
        return Gallery.permitted.all()
    
    def get_extra_context(self):
        return {'title': 'Galleries'}

object_detail = ObjectDetail()
