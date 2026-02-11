from django.urls import path
from signup_app import views

urlpatterns = [
    path('',views.signup_page, name='signup'),
    path('login/',views.login_page, name='login'),
    path('counter/',views.counter_view, name='counter'),
    path('logout/',views.logout_view, name='logout')
]