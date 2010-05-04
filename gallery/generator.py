import random

from django.conf import settings

from generate import IMAGES, VIDEOS
from generate.json_loader import load_json

GALLERY_COUNT = 20

def generate():
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
    for i in range(1, (GALLERY_COUNT * 3)):
        objects.append({
            "model": "gallery.GalleryImage",
            "fields": {
                "title": "Gallery Image %s Title" % i,
                "state": "published",
                "gallery": {
                    "model": "gallery.Gallery",
                    "fields": { 
                        "title": "Gallery %s Title" % (i / 3 + 1)
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
                        "title": "Gallery %s Title" % (i / 3 + 1)
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
            "model": "gallery.VideoFile",
            "fields": {
                "title": "Video File %s Title" % i,
                "state": "published",
                "file": random.sample(VIDEOS, 1)[0],
                "gallery": {
                    "model": "gallery.Gallery",
                    "fields": { 
                        "title": "Gallery %s Title" % (i / 3 + 1)
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

    
    load_json(objects)
    
    # fix embed escaping
    from gallery.models import VideoEmbed
    for obj in VideoEmbed.objects.all():
        obj.embed = obj.embed.replace("&#39;", '"')
        obj.save()
