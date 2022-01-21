

from unicodedata import category
from .models import Category

def menu_links(request):
    """
    Returns a dictionary with the menu links.
    """
    links = Category.objects.all()
    return dict(links=links)