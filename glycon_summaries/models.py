""" Provides extra models for page summary views and summary blocks
"""
from django.db import models

from glycon.models import BaseContent, BaseBlock
from glycon_summaries.views import summary_block_html


class BaseSummary(models.Model):

    tag_filter = models.CharField(max_length=255)

    @property
    def filter_items(self):
        items = BaseContent.objects.filter(tags__text=self.tag_filter).filter(published=True).all()[0:4]
        return items

    class Meta:
        abstract = True

class Summary(BaseSummary, BaseContent):

    def __str__(self):
        return self.title

    class Data:
        description = "A collection of filtered content."


class SummaryBlock(BaseSummary, BaseBlock):

    @property
    def content(self):
        return summary_block_html(self)

    def __str__(self):
        return self.name

    class Data:
        description = "Place a summary anywhere in a page"