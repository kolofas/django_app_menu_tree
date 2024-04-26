from django.shortcuts import render
from .models import Menu, MenuItem


def get_menu_by_name(menu_name):
    """
    :param menu_name: Name menu
    :return: Object Menu or None
    """
    try:
        menu = Menu.objects.get(title=menu_name)
        return menu
    except Menu.DoesNotExist:
        return None


def draw_menu(request, menu_name):
    menu = get_menu_by_name(menu_name)

    if menu:
        root_menu_items = MenuItem.objects.filter(parent__title=menu_name)

        for item in root_menu_items:
            item.children = MenuItem.objects.filter(parent__title=item.title)

        return render(request, 'menu.html', {'menu_items': root_menu_items, 'menu_name': menu_name})
    else:
        return render(request, 'menu.html', {'menu_items': []})


def show_menu(request, menu_name):
    menu_html = draw_menu(request, menu_name)
    return menu_html

