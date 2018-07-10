from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist', views.show_artist_detail, name='artist_detail'),
]
