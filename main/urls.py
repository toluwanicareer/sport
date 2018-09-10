from django.conf.urls import url
from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('active_queries', views.getActiveQuery.as_view(), name='active_queries'),
    path('format_data', views.format_data.as_view()),
    path('save_query', views.saveQuery.as_view(), name="save_query")
    ]
