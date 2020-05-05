from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path('download/(?P<file>[a-zA-Zа-яА-Я0-9\/_.:-]*)/', views.download, name='download_file'),
]
