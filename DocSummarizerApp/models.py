from django.db import models
from .storages import OutsideRootStorage

class Document(models.Model):
    title = models.CharField(max_length=100, default='Untitled')
    file = models.FileField(storage=OutsideRootStorage(), upload_to='UploadedDocuments')
