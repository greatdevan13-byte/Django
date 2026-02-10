from django.urls import path
from classapp import views
 
urlpatterns = [
    path('',views.add , name='home'),
    path('list', views.view_students , name='student_list'),
    path('edit/<int:id>/' , views.update_students , name='edit_students'),
    path('delete/<int:id>/' ,views.delete_students ,name='delete_students'),
]