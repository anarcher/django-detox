from django.test import TestCase
from django.conf import settings
from django.core.cache import cache
from app.models import *
import time

class CacheTest(TestCase):
    fixtures = ['test']

    def test_cache_save_new(self):
        from django.db import connection
        a = Author()
        a.name = "author"
        a.save()
        self.assertFalse(a.from_cache)
        self.assertTrue(cache.get(a.cache_key))
        self.assertTrue(len(connection.queries) > 0)


    def test_cache_get_by_pk(self):
        self.assertTrue(Author.objects.get(pk=1).from_cache)
        self.assertTrue(Author.objects.get(pk=1))

    def test_cache_get_not_pk(self):
        from django.db import connection
        # Prime cache
        self.assertTrue(Author.objects.get(pk=1).from_cache)

        # Not from cache b/c it's not a simple get by pk
        a = Article.objects.get(pk=1,name='test')
        self.assertTrue(a.name == 'test')
        self.assertFalse(Article.objects.get(pk=1, name='test').from_cache)
        self.assertTrue(len(connection.queries) == 0)

    def test_cache_filter1(self):
        al = Article.objects.all()
        self.assertTrue(al) 
        self.assertTrue(len(al) > 0)
