from django.urls import path
from booksapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_book, name='add'),
    path('update/<int:id>/', views.update_book, name='update'),
    path('delete/<int:id>/', views.delete_book, name='delete'),
]