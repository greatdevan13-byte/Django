from django.urls import path
from bookapp import views

urlpatterns = [
    path('',views.signup_view, name='signup'),
    path('login/',views.login_view, name='login'),
    path('welcome/',views.welcome, name='welcome'),
    path('logout/',views.logout_view ,name='logout')
]