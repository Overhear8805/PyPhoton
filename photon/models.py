from django.db import models

# Create your models here.
class ImageEntity(models.Model):
    modified = models.DateTimeField(auto_now_add=True)
    image_hash = models.CharField(max_length=255, db_index=True, unique=True)
    file_name = models.CharField(max_length=70, null=True)
    file_type = models.CharField(max_length=5, null=True)
    owner = models.CharField(max_length=40, null=True)
