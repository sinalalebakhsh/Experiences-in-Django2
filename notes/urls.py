from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_views, name='list views'),
]
