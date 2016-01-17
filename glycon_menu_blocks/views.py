from django.template.loader import render_to_string

from glycon.models import MenuItem


def menu_block_html(menu_name):
    menu = MenuItem.objects.filter(menu__name=menu_name).order_by('weight', 'short_name')
    return render_to_string("menublock.html", context={"menu": menu})