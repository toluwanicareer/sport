from django import template
register = template.Library()
from django.utils import timezone

from ..models import Query

@register.simple_tag
def active_count(cat_id):
    count=Query.c_objects.active(cat_id).count()
    return count

