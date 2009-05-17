from django.test import TestCase
from app.models import *

class CacheTest(TestCase):
    fixtures = ['test']

    def test_cache_get_by_pk(self):
        self.assertFalse(Author.objects.get(pk=1).from_cache)
        self.assertTrue(Author.objects.get(pk=1).from_cache)

    def test_cache_get_not_pk(self):
        # Prime cache
        self.assertFalse(Author.objects.get(pk=1).from_cache)
        self.assertTrue(Author.objects.get(pk=1).from_cache)

        # Not from cache b/c it's not a simple get by pk
        self.assertFalse(
            Article.objects.get(pk=1, name='anarcher').from_cache)
