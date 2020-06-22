from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField

# Create your models here.


class Resource(models.Model):
    id = models.CharField(primary_key=True, name='id',
                          blank=True, max_length=2)
    title = models.CharField(name='title', blank=True,
                             null=True, max_length=50)
    eventColor = ColorField(default='#FF0000')

    def __str__(self):
        return self.title


class Event(models.Model):
    resourceId = models.ForeignKey(
        'Resource', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(name='title', blank=True,
                             null=True, max_length=99)
    description = models.CharField(
        name='description', blank=True, null=True, max_length=99)
    start = models.DateTimeField(name='start', blank=True, null=True)
    end = models.DateTimeField(name='end', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sharedSch')
