from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('mypass/', views.mypass, name='mypass'),
    path('passgen/', views.passgen, name='passgen'),
    path('profile/', views.profile, name='profile'),
]