from django.urls import path
from . import views
from views import index

urlpatterns = [
    path('',index),
    path('movs/', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
]