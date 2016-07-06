from __future__ import unicode_literals
from django.db import models

class Images(models.Model):
    id = models.AutoField()
    path = models.CharField(max_length=100)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'
