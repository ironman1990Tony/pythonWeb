# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Topic(models.Model):
    """user learning topic"""
    text = models.CharField( max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        """return model's string """
        return self.text

class Entry(models.Model):
    """the entry of some learning topic"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        """return model's string"""
        return self.text[:50] + '...'
