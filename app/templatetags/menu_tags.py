from django import template
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404

from app.models import MenuItem, Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu = get_object_or_404(Menu, title=menu_name)
    menu_items = MenuItem.objects.filter(parent__title=menu_name).prefetch_related('items')

    def render_menu_item(menu_item):
        children = menu_item.children.all()
        if children:
            return f'<li><a href="{menu_item.url}">{escape(menu_item.title)}</a><ul>{"".join(render_menu_item(child) for child in children)}</ul></li>'
        else:
            return f'<li><a href="{menu_item.url}">{escape(menu_item.title)}</a></li>'

    menu_html = ''.join(render_menu_item(item) for item in menu_items)
    context['menu_items'] = mark_safe(f'<ul>{menu_html}</ul>')
    return ''
