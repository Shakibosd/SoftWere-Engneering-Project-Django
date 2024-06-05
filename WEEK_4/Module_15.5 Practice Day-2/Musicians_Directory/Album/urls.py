from django.urls import path
from Album.views import album_create, album_edit, album_delete

urlpatterns = [
    path('',album_create,name='album'),
    path('Edit/<int:pk>/',album_edit,name='edit_album'),
    path('Delete/<int:pk>/',album_delete,name='dlt_album')
]


