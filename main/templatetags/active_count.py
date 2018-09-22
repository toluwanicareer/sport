from django import template
register = template.Library()
from django.utils import timezone

from ..models import Query, Track
import datetime
import pdb


@register.simple_tag
def active_count(cat_id):
    count=Track.objects.filter(query__category__id=cat_id).filter(date=datetime.datetime.now().date()).values_list('query', flat=True).distinct().count()
    return count

