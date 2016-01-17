""" Provides extra models for menu blocks
"""
from django.db import models

from glycon.models import BaseBlock, Menu
from glycon_menu_blocks.views import menu_block_html


class MenuBlock(BaseBlock):

    menu = models.ForeignKey(Menu)

    def content(self, request=None):
        return menu_block_html(self.menu.name)

    def __str__(self):
        return self.name

    class Data:
        description = "Place menus in any region of the page"
