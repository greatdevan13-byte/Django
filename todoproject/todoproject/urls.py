from django.contrib import admin
from django.urls import path,include
from greeting import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', views.greeting,name='home'),
    path('about-us', views.aboutUs,name='about-us'),
    path('page/<str:title>/', views.pages,name='page'),
    path('count/<int:num>/', views.count,name='count'),
    path('login/', RedirectView.as_view(pattern_name='about-us')),
    path('signup/',include('login.urls'))
]  # Redirect to 'home' URL

