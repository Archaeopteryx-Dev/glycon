from django.db import models
from django.contrib.auth.models import User


class PublishingMixin(models.Model):

    class Meta:
        abstract=True

    comments_allowed = models.BooleanField()
    featured = models.BooleanField()


class Menu(models.Model):
    name = models.CharField(max_length=40)


class MenuItem(PublishingMixin):
    """

    """
    short_name = models.CharField(max_length=20)
    alt_text = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu)
    weight = models.IntegerField(blank=True, null=True)


class BaseContent(models.Model):
    """

    """
    title = models.CharField(max_length=255)
    create_dt = models.DateTimeField()
    change_dt = models.DateTimeField()
    author = models.ForeignKey(User)
    teaser = models.TextField()
    image_1 = models.ImageField(blank=True, null=True)
    image_2 = models.ImageField(blank=True, null=True)
    published = models.BooleanField
    body = models.TextField()
    menu = models.ForeignKey(Menu, blank=True, null=True)
    url_slug = models.SlugField(max_length=255)
    content_type = models.CharField(max_length=255)


class Page(BaseContent):
    """

    """


class Article(PublishingMixin, BaseContent):
    """

    """