
from django.urls import path
from musician.views import musician_form, edit_musician, musician_delete

urlpatterns = [
    path('',musician_form, name='musician'),
    path('Edit_Musician/<int:pk>/',edit_musician, name='edit_musician'),
    path('Delete_Musician/<int:pk>/',musician_delete, name='delete_musician'),
]


