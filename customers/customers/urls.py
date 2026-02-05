from django.urls import path
from customersapp import views

urlpatterns =[
    path('',views.details),
    path('filtered/',views.filtered)
]