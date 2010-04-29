Django Gallery
==============
**Django gallery app.**

Views
=====

object_list::

    views.object_list

Displays gallery objects with paging and filtering by utilizing *content.generic.views.GenericObjectList*. Customize template by overriding *gallery/gallery_list.html*. You can also customize the view itself by subclassing and overriding *views.ObjectList* and providing your new view to a url pattern, or directly through ducktyping.

Tag Reference
=============

Inclusion Tags
--------------

Enable in your templates with the {% load gallery_inclusion_tags %} tag.

gallery_listing
~~~~~~~~~~~~~~~
Outputs gallery listing for provided galleries. Renders block template for each gallery: *gallery/inclusion_tags/gallery_block.html*

Arguments: list of gallery objects to render 

Sample usage:

    {% gallery_listing object_list %}

Customize template by overriding *gallery/inclusion_tags/gallery_list.html*.
