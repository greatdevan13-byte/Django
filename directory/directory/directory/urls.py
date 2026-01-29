
from django.urls import path
from employees import views

urlpatterns = [
    path('d',views.details)
]