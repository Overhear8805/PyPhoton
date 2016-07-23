from django.db import models

# Create your models here.
class ImageEntity(models.Model):
    modified = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=255, db_index=True, unique=True)
    file_name = models.CharField(max_length=70, null=True)
    mime = models.CharField(max_length=20, null=True)
    owner = models.CharField(max_length=40, null=True)
