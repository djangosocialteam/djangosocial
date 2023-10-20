# Borrowed wagtail/bakerydemo

from django import template
from wagtail.models import Site

from ..models import NavBar

register = template.Library()
# https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return Site.find_for_request(context["request"]).root_page


def has_menu_children(page):
    # This is used by the top_menu property
    # get_children is a Treebeard API thing
    # https://tabo.pe/projects/django-treebeard/docs/4.0.1/api.html
    return page.get_children().live().in_menu().exists()


def has_children(page):
    # Generically allow index pages to list their children
    return page.get_children().live().exists()


def is_active(page, current_page):
    # To give us active state on main navigation
    return current_page.url_path.startswith(page.url_path) if current_page else False


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the Foundation menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag("tags/top_menu.html", takes_context=True)
def top_menu(context, parent, calling_page=None, is_desktop=True):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = calling_page.url_path.startswith(menuitem.url_path) if calling_page else False

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
        "is_desktop": is_desktop,
    }


@register.simple_tag
def nav_logo():
    instance = NavBar.objects.first()
    if instance:
        return instance.logo.url
