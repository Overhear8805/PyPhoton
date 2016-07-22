from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^info/$', views.info, name='info'),
        url(r'^image/(?P<hash>[a-zA-Z0-9]+)/$', views.get_image_by_hash, name='get_image_by_hash'),
        url(r'^image/(?P<hash>[a-zA-Z0-9]+)/meta/$', views.get_metadata_by_hash, name='get_metadata_by_hash'),
        url(r'^upload/(?P<file_name>[a-zA-Z0-9._-]+)/$', views.upload_image, name='upload_image'),
        ]
