from typing import Iterable
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class AbstractModel(models.Model): 
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        abstract = True 

class Folder(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='folders')
    name = models.CharField(max_length=128)


class File(AbstractModel):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files', null=True, blank=True)
    name = models.CharField(max_length=125, null=True, blank=True)
    file = models.FileField(upload_to='files/')
    extension = models.CharField(max_length=10, null=True, blank=True)
        
    