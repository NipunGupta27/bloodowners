from django.urls import path
from . import views

urlpatterns=[
    path('', views.BD.index),
    path('sign', views.BD.sign, name="log"),
    path('signup', views.BD.register, name="signup"),
    path('signin', views.BD.login, name="signin"),
    path('logout', views.BD.logout, name="logout"),
    path('bloodsearch', views.BD.finddonor, name="bloodsearch")
]
