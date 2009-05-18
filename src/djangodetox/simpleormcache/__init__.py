from django.core.cache import cache
from django.db import models,connection
from django.db.models.query import QuerySet
from django.db.models.signals import post_save,pre_delete

SIMPLE_CACHE_SECONDS = 60 * 60

def key_from_instance(instance):
    opts = instance._meta
    cache_key = "%s.%s:%s" % (opts.app_label,opts.module_name,instance.pk)
    return cache_key

def post_save_cache(sender,instance,**kwargs):
    cache.set(key_from_instance(instance),instance,SIMPLE_CACHE_SECONDS)
post_save.connect(post_save_cache)

def pre_delete_uncache(sender,instance,**kwargs):
    cache.delete(key_from_instance(instance))
pre_delete.connect(pre_delete_uncache)


class SimpleCacheQuerySet(QuerySet):
    def filter(self,*args,**kwargs):
        pk = None
        for val in ('pk','pk_exact','id','id_exact'):
            if val in kwargs:
                pk = kwargs[val]
                break
        if pk is not None:
            opts = self.model._meta
            key = '%s.%s:%s' % (opts.app_label, opts.module_name, pk)
            obj = cache.get(key)
            if obj is not None:
                self._result_cache = [obj]
                return self
        return super(SimpleCacheQuerySet, self).filter(*args, **kwargs)


class SimpleCacheManager(models.Manager):
    def get_query_set(self,connection=connection):
        return SimpleCacheQuerySet(self.model,connection=connection)

