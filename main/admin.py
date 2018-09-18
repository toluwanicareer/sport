from django.contrib import admin
from .models import Query, Category, Track

# Register your models here.
admin.site.register(Category)
admin.site.register(Query)
admin.site.register(Track)
