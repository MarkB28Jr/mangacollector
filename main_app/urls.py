from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mangas/', views.mangas_index , name='index'),
    path('mangas/<int:manga_id>/', views.mangas_detail, name='detail'),
    path('mangas/create/', views.MangaCreate.as_view(), name='mangas_create'),
    path('mangas/<int:pk>/update/', views.MangaUpdate.as_view(), name='mangas_update'),
    path('mangas/<int:pk>/delete/', views.MangaDelete.as_view(), name='mangas_delete'),
    
    path('mangas/<int:manga_id>/add_readme/', views.add_readme, name='add_readme'),
    
    path('reads/', views.ReadList.as_view(), name='reads_index'),
    path('reads/<int:pk>/', views.ReadDetail.as_view(), name='reads_detail'),
    path('reads/create/', views.ReadCreate.as_view(), name='reads_create'),
    path('reads/<int:pk>/update/', views.ReadUpdate.as_view(), name='reads_update'),
    path('reads/<int:pk>/delete/', views.ReadDelete.as_view(), name='reads_delete'),
    
    path('mangas/<int:manga_id>/assoc_read/<int:read_id>/', views.assoc_read, name='assoc_read'),
    path('mangas/<int:manga_id>/remove_read/<int:read_id>/', views.remove_read, name='remove_read'),
]