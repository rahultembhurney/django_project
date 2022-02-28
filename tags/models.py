from tkinter import CASCADE
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Tag (models.Model):
    label = models.CharField(max_length=255)


class TagItems(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    '''If we use poduct instead then we create a dependency on Procduct app. we want tag class to be independent.
    Hence we use contenttypes which takes on searches data as follows:
    ContentType = what kind of data it is.
    object_id = the Object ID of content.
    content_object = what object is in that object ID
    Since object IDs are unique they can be used to look for data in database'''
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
