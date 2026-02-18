from products_app import views
from django.urls import path

urlpatterns = [
    path('',views.add_details, name='createproduct'),
     path('products/',views.view_product, name='viewproduct'),
      path('<int:pk>/pdf/', views.generate_pdf, name='generate_pdf'),
]