from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-movie/', views.create_movie, name='create-movie'),
    path('all-movies/', views.all_movies, name='movies'),
    path('update-movie/<int:id>/', views.update_movie, name='update-movie'),
    path('delete-movie/<int:id>/', views.delete_movie, name='delete-movie'),
]