from django.urls import path
from . import views

app_name = 'news_stories'

urlpatterns = [
    path('', views.index, name='index')
    ]
