from django.contrib import admin

from glycon.models import Page, Article, Menu, MenuItem, SiteConfiguration, Tag, Block, Region, Theme


class PageUserInterface(admin.ModelAdmin):

    fields = ["title", "create_dt", "change_dt", "author", "teaser", "image_1", "image_2", "body", "menu", "url_slug", "tags", "sites", "content_type"]


class ArticleUserInterface(admin.ModelAdmin):

    fields = ["title", "create_dt", "change_dt", "author", "teaser", "image_1", "image_2", "comments_allowed", "featured", "body", "url_slug", "tags", "sites", "content_type", "published"]

admin.site.register(Page, PageUserInterface)
admin.site.register(Article, ArticleUserInterface)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(SiteConfiguration)
admin.site.register(Tag)
admin.site.register(Block)
admin.site.register(Region)
admin.site.register(Theme)