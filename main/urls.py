from django.conf.urls import url
from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('active_queries', views.getActiveQuery.as_view(), name='active_queries'),
    path('format_data', views.format_data.as_view()),
    path('save_query', views.saveQuery.as_view(), name="save_query"),
    path('handle_content', views.handleContent.as_view(), name="handle_content"),
    path('all_queries', views.getAllQuery.as_view(), name='all_queries'),
    path('query_delete', views.deleteQuery.as_view()),
    path('query/<int:pk>', views.updateQuery.as_view(), name="update_query"),
    ]
