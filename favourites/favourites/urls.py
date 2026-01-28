from django.urls import path
from personal import views


urlpatterns = [
    path('gallery/', views.gallery),
    path('contact/', views.contact)
]