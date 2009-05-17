from django.db import models

class CachedModel(models.Model):
    from_cache = False
    class Meta:
        abstract = True

