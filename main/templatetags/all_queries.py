from django import template
register = template.Library()
from django.utils import timezone

from ..models import Query, Track
import datetime
import pdb


@register.simple_tag
def all_queries(cat_id):
    count=Query.objects.filter(category__id=cat_id).count()
    return count

