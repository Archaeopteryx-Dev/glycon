from django.shortcuts import render
from django.http import HttpResponse, Http404

from glycon.models import BaseContent, Article, Page
from glycon.config import *


def content(request, page_name):
    contents = BaseContent.objects.filter(url_slug=page_name).first()
    if contents is None:
        raise Http404
    template = "page.html"
    return render(request, template, dict(
        content=contents,
        sitename=SITENAME,
        media=GLYCON_MEDIA_URL
    ))

def home(request):
    return render(request, 'home.html', {} )
