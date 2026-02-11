from .import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup, name='signup'),
     path('login/',views.login_page,name='login'),
     path('logout/',views.logout_view , name='logout')
]
