import random

from generate import IMAGES
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

    # gen gallery photo sizes
    objects.append({
        "model": "photologue.PhotoSize",
        "fields": {
            "name": "gallery_small",
            "width": "188",
            "height": "104",
            "crop": True,
        },
    })
    
    load_json(objects)
