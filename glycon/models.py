from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class Tag(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

    class Data:
        description = "Tags for classifying content"


class PublishingMixin(models.Model):

    class Meta:
        abstract = True

    comments_allowed = models.BooleanField()
    featured = models.BooleanField()
    

class Theme(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    colour_1 = models.CharField(max_length=6, null=True, blank=True)
    colour_2 = models.CharField(max_length=6, null=True, blank=True)
    colour_3 = models.CharField(max_length=6, null=True, blank=True)
    colour_4 = models.CharField(max_length=6, null=True, blank=True)
    colour_5 = models.CharField(max_length=6, null=True, blank=True)
    colour_6 = models.CharField(max_length=6, null=True, blank=True)
    background_image = models.ImageField(blank=True, null=True)
    logo_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Data:
        description = "Configure a look and feel for your site(s)"

class Menu(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Data:
        description = "Collections of menu items / links"


class MenuItem(models.Model):
    """

    """
    short_name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu)
    weight = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.short_name

    class Data:
        description = "A single link on a menu"

class BaseContent(models.Model):
    """

    """
    title = models.CharField(max_length=255)
    create_dt = models.DateTimeField()
    change_dt = models.DateTimeField()
    author = models.ForeignKey(User)
    teaser = models.TextField(blank=True, null=True)
    image_1 = models.ImageField(blank=True, null=True)
    image_2 = models.ImageField(blank=True, null=True)
    published = models.BooleanField(default=True)
    body = models.TextField(blank=True, null=True)
    menu = models.ForeignKey(Menu, blank=True, null=True)
    url_slug = models.SlugField(max_length=255)
    content_type = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True)
    sites = models.ManyToManyField(Site, blank=True)

    @property
    def link_url(self):
        return ("/content/{}".format(self.url_slug))

    @property
    def link_url_qualified(self):
        return ("http://{}{}".format(Site.objects.get_current().domain, self.link_url))


class Page(BaseContent):
    """

    """

    def __str__(self):
        return self.title

    class Data:
        description = "The most basic form of content"

class Article(PublishingMixin, BaseContent):
    """

    """

    def __str__(self):
        return "Article: '{}'".format(self.title)

    class Data:
        description = "A more flexible content format"

class SiteConfiguration(models.Model):
    site = models.ForeignKey(Site)
    theme = models.ForeignKey(Theme)
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    active = models.BooleanField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site config"

    class Data:
        description = "Basic settings for your site(s)"


class BaseBlock(models.Model):
    name = models.CharField(max_length=255)
    block_type = models.CharField(max_length=255)
    weight = models.IntegerField(default=1)
    pages = models.TextField(null=True, blank=True)
    site = models.ManyToManyField(Site, blank=True)

    @property
    def all_pages(self):
        if self.pages:
            return self.pages.split("\n")
        else:
            return []

    def __str__(self):
        return self.name

class Block(BaseBlock):

    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Data:
        description = "Reusable blocks of text or code"


class Region(models.Model):
    name = models.CharField(max_length=255)
    blocks = models.ManyToManyField(BaseBlock, blank=True)

    def __str__(self):
        return self.name

    class Data:
        description = "A region of a template (add blocks here)"