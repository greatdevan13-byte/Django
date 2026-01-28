from django.urls import path
from welcome import views
urlpatterns = [
  path('', views.home),
  path('about/',views.about)


]