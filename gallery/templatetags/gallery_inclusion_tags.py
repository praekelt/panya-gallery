from django import template

register = template.Library()

@register.inclusion_tag('gallery/inclusion_tags/gallery_listing.html')
def gallery_listing(object_list):
    return {'object_list': object_list}
