from django.core.urlresolvers import reverse
from django.db import models

from content.models import ModelBase

class Gallery(ModelBase):
    class Meta():
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
    
    def item_count(self):
        return GalleryItem.permitted.filter(gallery=self).count()
    
    def get_absolute_url(self):
        return reverse('gallery_object_detail', kwargs={'slug': self.slug})
    
class GalleryItem(ModelBase):
    gallery = models.ForeignKey(
        'gallery.Gallery',
    )

class GalleryImage(GalleryItem):
    class Meta():
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

class VideoEmbed(GalleryItem):
    embed = models.TextField()
    class Meta():
        verbose_name = "Video Embed"
        verbose_name_plural = "Video Embeds"

class VideoFile(GalleryItem):
    file = models.FileField(upload_to='content/videofile')
    class Meta():
        verbose_name = "Video File"
        verbose_name_plural = "Video Files"
