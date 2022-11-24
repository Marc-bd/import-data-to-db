from django.db import models
import uuid
import ipdb
from .utils.read_text import read_text

# Create your models here.

# Save the upload file with UUID
def upload_data_formatter(instance, filename):

    file_name = f"`{str(uuid.uuid4())}.json`"

    return file_name


class Data(models.Model):

    file = models.FileField(upload_to=upload_data_formatter, blank=True, null=True)
