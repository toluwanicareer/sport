from django import template
register = template.Library()
from django.utils import timezone

from ..models import Query, Category


@register.simple_tag
def cat_id(category_name):
    cat=Category.objects.get(name__icontains=category_name)
    return cat.id

