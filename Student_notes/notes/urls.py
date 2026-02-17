from django.urls import path
from .views import signup, login, add_note, list_notes

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('add-note/', add_note),
    path('notes/', list_notes),
]
