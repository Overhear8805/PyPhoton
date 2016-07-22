from django.http import JsonResponse, HttpResponse, Http404
from django.core import serializers
from photon.models import ImageEntity 
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import Storage, FileSystemStorage

import logging
import json
import hashlib
import datetime
import socket

log = logging.getLogger(__name__)
MEDIA_DIR = "/home/simon/Photon/"

hasher = hashlib.sha1()
file_storage = FileSystemStorage(location=MEDIA_DIR)
file_storage.file_permission_mode=644

# Ping endpoint
# /photon/api/vX.X/info
def info(request):
    info = {}
    info['time'] = datetime.datetime.now().isoformat()
    info['version'] = "v1.0"
    info['host'] = socket.gethostname()
    return JsonResponse(info)

# Get metadata by hash
# /photon/api/vX.X/<hash>/meta
def get_metadata_by_hash(request, hash):
    image_entity = ImageEntity.objects.filter(image_hash=hash)
    return HttpResponse(serializers.serialize("json", image_entity))

# Get image by hash
# /photon/api/vX.X/<hash>
def get_image_by_hash(request, hash):
    image_entity = ImageEntity.objects.filter(image_hash=hash)
    if image_entity.values():
        image_entity = ImageEntity.objects.get(image_hash=hash)
        try:
            with open(MEDIA_DIR + image_entity.file_name, "rb") as image:
                 return HttpResponse(image.read(), content_type="image/jpeg")
        except IOError:
            log.error("Failed to load image with hash %s" % hash)
    else:
        raise Http404("No image with that hash exists")

# POST image as raw body
# /photon/api/vX.X/upload/<filename>.<file extention>/
@csrf_exempt
def upload_image(request, file_name):
    new_file_name = file_storage.save(file_name, request)

    with open(MEDIA_DIR+new_file_name, 'rb') as f:
        hash = hashlib.sha1(f.read()).hexdigest()

    image = ImageEntity(image_hash=hash, file_name=new_file_name)
    image.save()

    return JsonResponse({"hash":hash})
