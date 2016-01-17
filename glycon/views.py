from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site

from glycon.models import BaseContent, Article, Page, Menu, MenuItem, Region, Block, SiteConfiguration
from glycon.config import *


def content(request, page_name):

    # Load primary page content
    contents = BaseContent.objects.filter(url_slug=page_name).first()
    if contents is None:
        return render(request, template_name="welcome.html", context={})
    contents = CONTENT_TYPES[contents.content_type].objects.get(
        url_slug=page_name,
        sites__id=get_current_site(request).id
    )
    if hasattr(contents, "published"):
        if not contents.published:
            raise render(request, template_name="error.html", context={"error": "No published content"})

    # Load blocks
    regions = {}
    for region in Region.objects.all():
        blocks = []

        def b_id(s):
            b = []
            for all_blocks in s:
                b.append(all_blocks.id)
            return b

        filtered_blocks = [block for block in region.blocks.order_by("weight") if
                           page_name in block.all_pages and get_current_site(request).id in b_id(block.site.all())]

        for block in filtered_blocks:
            for all_blocks in block.site.all():
                print(all_blocks.id)
            block_contents = BLOCK_TYPES[block.block_type].objects.filter(id=block.id).first()
            blocks.append(block_contents.content)
        regions[region.name] = blocks

    template = "{}.html".format(contents.content_type.lower())
    menu = MenuItem.objects.filter(menu__name="Main").order_by('weight', 'short_name')
    current_site = Site.objects.get_current().id
    logo = SiteConfiguration.objects.get(site__id=current_site).theme.logo_image
    return render(request, template, dict(
        menu=menu,
        content=contents,
        regions=regions,
        sitename=SITENAME,
        media=GLYCON_MEDIA_URL,
        logo=logo
    ))

def home(request):
    return content(request, HOME_URL)
