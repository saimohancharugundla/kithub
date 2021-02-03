from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.register, name="register"),
    path("register/confirm/",views.confirmregister, name="confirmregister"),
    path('signout/',views.signout,name='signout'),
    path('signin/',views.signin,name='signin'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
