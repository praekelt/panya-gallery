import unittest

from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.http import Http404
from django.test import TestCase
from django.test.client import Client

from gallery import views
from gallery.models import Gallery, GalleryImage, VideoEmbed, VideoFile
from photologue.models import PhotoSize

class ViewsTestCase(TestCase):
    def test_video_file_response(self):
        # create a video file object
        gallery = Gallery()
        gallery.save()
        obj = VideoFile(gallery=gallery, file='test.flv')
        obj.save()
        
        # if the videofile_large photosize does not exist, use default dimensions (500x300)
        result = views.videofile_response({'object': obj})
        self.failUnless('width:500px' in result)
        self.failUnless('height:300px' in result)
        
        # if the videofile_large photosize exists, use its dimension
        PhotoSize(name="videofile_large", width=606, height=340).save()
        obj = VideoFile(gallery=gallery, file='test.flv')
        obj.save()
        result = views.videofile_response({'object': obj})
        self.failUnless('width:606px' in result)
        self.failUnless('height:340px' in result)
   
    def test_video_embed_response(self):
        original_embed = '<object width="480" height="385"><param name="movie" value="http://www.youtube.com/v/VdgI0j1odkY&hl=en_US&fs=1&"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/VdgI0j1odkY&hl=en_US&fs=1&" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="480" height="385"></embed></object>'
        correctly_modified_embed = '<object width="606" height="340"><param name="movie" value="http://www.youtube.com/v/VdgI0j1odkY&hl=en_US&fs=1&"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/VdgI0j1odkY&hl=en_US&fs=1&" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="606" height="340"></embed></object>\n'
      
        # create a video embed object
        gallery = Gallery()
        gallery.save()
        obj = VideoEmbed(gallery=gallery, embed=original_embed)
        obj.save()

        # if the videoembed_large photosize does not exist, return original unmodified embed
        result = views.videoembed_response({'object': obj})
        self.failUnlessEqual(result, original_embed + '\n')

        # if the videoembed_large photosize exists, return original embed scaled to its dimensions
        PhotoSize(name="videoembed_large", width=606, height=340).save()
        obj = VideoEmbed(gallery=gallery, embed=original_embed, image="test.jpg")
        obj.save()
        result = views.videoembed_response({'object': obj})
        self.failUnlessEqual(result, correctly_modified_embed)

    def test_gallery_item_ajax_galleriffic(self):
        # create objects
        gallery = Gallery()
        gallery.save()
        gi_obj = GalleryImage(gallery=gallery, state='published')
        gi_obj.save()
        gi_obj.sites.add(Site.objects.get_current())
        ve_obj = VideoEmbed(gallery=gallery, state='published')
        ve_obj.save()
        ve_obj.sites.add(Site.objects.get_current())
        vf_obj = VideoFile(gallery=gallery, state='published', file='test.flv')
        vf_obj.save()
        vf_obj.sites.add(Site.objects.get_current())

        # raise 404 on invalid slug
        self.assertRaises(Http404, views.gallery_item_ajax_galleriffic, request=None, slug='invalid_slug')

        # use galleryimage template for gallery image object
        client = Client()
        response = client.get(reverse('gallery_item_ajax_galleriffic', kwargs={'slug': gi_obj.slug}))
        self.assertTemplateUsed(response, 'gallery/ajax/galleriffic_galleryimage.html')
        
        # use videoembed template for video embed object
        response = client.get(reverse('gallery_item_ajax_galleriffic', kwargs={'slug': ve_obj.slug}))
        self.assertTemplateUsed(response, 'gallery/ajax/galleriffic_videoembed.html')
        
        # use videofile template for video file object
        response = client.get(reverse('gallery_item_ajax_galleriffic', kwargs={'slug': vf_obj.slug}))
        self.assertTemplateUsed(response, 'gallery/ajax/galleriffic_videofile.html')
