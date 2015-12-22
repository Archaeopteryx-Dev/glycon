from django.contrib import admin

from glycon.models import Page, Article


class PageUserInterface(admin.ModelAdmin):

    fields = ["title", "create_dt", "change_dt", "author", "teaser", "image_1", "image_2", "body", "menu", "url_slug"]


class ArticleUserInterface(admin.ModelAdmin):

    fields = ["create_dt", "change_dt", "author", "teaser", "image_1", "image_2", "comments_allowed", "featured", "body"]

admin.site.register(Page, PageUserInterface)
admin.site.register(Article, ArticleUserInterface)