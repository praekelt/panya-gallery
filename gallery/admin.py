from copy import deepcopy

from django.contrib import admin

from content.admin import ModelBaseAdmin

from gallery.models import Gallery, GalleryImage, VideoEmbed, VideoFile

class GalleryImageAdmin(ModelBaseAdmin):
    fieldsets = deepcopy(ModelBaseAdmin.fieldsets)
    list_display = ModelBaseAdmin.list_display + ('gallery',)
    list_filter = ModelBaseAdmin.list_filter + ('gallery',)
    
    for fieldset in fieldsets:
        if fieldset[0] == None:
            fieldset[1]['fields'] += ('gallery',)

admin.site.register(Gallery, ModelBaseAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(VideoEmbed, ModelBaseAdmin)
admin.site.register(VideoFile, ModelBaseAdmin)
