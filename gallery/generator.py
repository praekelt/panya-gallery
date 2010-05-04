import random

from django.conf import settings

from generate import IMAGES
from generate.json_loader import load_json

GALLERY_COUNT = 20

def generate_debug_true():
    objects = []

    # gen gallery objects
    for i in range(1, GALLERY_COUNT + 1):
        objects.append({
            "model": "gallery.Gallery",
            "fields": {
                "title": "Gallery %s Title" % i,
                "state": "published",
                "image": random.sample(IMAGES, 1)[0],
                "sites": {
                    "model": "sites.Site",
                    "fields": { 
                        "name": "example.com"
                    }
                },
            },
        })
    # gen gallery content
    for i in range(1, (GALLERY_COUNT * 5)):
        objects.append({
            "model": "gallery.GalleryImage",
            "fields": {
                "title": "Gallery Image %s Title" % i,
                "state": "published",
                "gallery": {
                    "model": "gallery.Gallery",
                    "fields": { 
                        "title": "Gallery %s Title" % (i / 5 + 1)
                    }
                },
                "image": random.sample(IMAGES, 1)[0],
                "sites": {
                    "model": "sites.Site",
                    "fields": { 
                        "name": "example.com"
                    }
                },
            },
        })
        objects.append({
            "model": "gallery.VideoEmbed",
            "fields": {
                "title": "Video Embed %s Title" % i,
                "embed": "<object width=&#39;480&#39; height=&#39;385&#39;><param name=&#39;movie&#39; value=&#39;http://www.youtube.com/v/VdgI0j1odkY&hl=en_US&fs=1&&#39;></param><param name=&#39;allowFullScreen&#39; value=&#39;true&#39;></param><param name=&#39;allowscriptaccess&#39; value=&#39;always&#39;></param><embed src=&#39;http://www.youtube.com/v/VdgI0j1odkY&hl=en_US&fs=1&&#39; type=&#39;application/x-shockwave-flash&#39; allowscriptaccess=&#39;always&#39; allowfullscreen=&#39;true&#39; width=&#39;480&#39; height=&#39;385&#39;></embed></object>",
                "state": "published",
                "gallery": {
                    "model": "gallery.Gallery",
                    "fields": { 
                        "title": "Gallery %s Title" % (i / 5 + 1)
                    }
                },
                "image": random.sample(IMAGES, 1)[0],
                "sites": {
                    "model": "sites.Site",
                    "fields": { 
                        "name": "example.com"
                    }
                },
            },
        })
    
    return objects
    
def generate_debug_false():
    objects = []

    # gen gallery photo sizes
    objects.append({
        "model": "photologue.PhotoSize",
        "fields": {
            "name": "gallery_gallery_block",
            "width": "188",
            "height": "104",
            "crop": True,
            "upscale": True,
        },
    })

    # gen gallery image photo sizes
    objects.append({
        "model": "photologue.PhotoSize",
        "fields": {
            "name": "gallery_galleryimage_thumbnail",
            "width": "60",
            "height": "60",
            "crop": True,
            "upscale": True,
        },
    })
    objects.append({
        "model": "photologue.PhotoSize",
        "fields": {
            "name": "gallery_galleryimage_large",
            "width": "606",
            "height": "0",
        },
    })
    objects.append({
        "model": "photologue.PhotoSize",
        "fields": {
            "name": "block",
            "width": "188",
            "height": "40",
        },
    })

    return objects
    
def generate():
    objects = generate_debug_false()
    if settings.DEBUG:
        objects += generate_debug_true()
    
    load_json(objects)
    
    # fix embed escaping
    from gallery.models import VideoEmbed
    for obj in VideoEmbed.objects.all():
        obj.embed = obj.embed.replace("&#39;", '"')
        obj.save()
