Django Gallery
==============
**Django gallery app.**

Views
=====
object_list::

    views.object_list

Displays gallery objects with paging and filtering by utilizing **content.generic.views.GenericObjectList**. Customize template by overriding **gallery/gallery_list.html**. You can also customize the view itself by subclassing and overriding **views.ObjectList** and providing your new view to a url pattern, or directly through ducktyping.
