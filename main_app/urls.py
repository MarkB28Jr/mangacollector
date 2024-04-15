from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mangas/', views.mangas_index , name='index'),
    path('mangas/<int:manga_id>/', views.mangas_detail, name='detail'),
]