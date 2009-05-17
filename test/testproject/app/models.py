from django.db import models
from djangodetox.ormcache.models import CachedModel
from djangodetox.ormcache import managers,fields
from djangodetox.simpleormcache import *

class BoardData(models.Model):
    title = models.CharField(max_length=32)
    objects = SimpleCacheManager()

class Author(CachedModel):
    name = models.CharField(max_length=32)
    objects = managers.CachingManager()

    def __unicode__(self):
        return self.name

class Site(CachedModel):
    name = models.CharField(max_length=32)
    objects = managers.CachingManager()

    def __unicode__(self):
        return self.name

class Article(CachedModel):
    name = models.CharField(max_length=32)
    author = models.ForeignKey('Author')
    sites = fields.CachingManyToManyField(Site, related_name='articles')
    objects = managers.CachingManager()

    def __unicode__(self):
        return self.name


