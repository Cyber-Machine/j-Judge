from unicodedata import name
from django.urls import path
from django.contrib.auth import views as auth_views
from submissions import views

urlpatterns = [path('', auth_views.LoginView.as_view(), name='Login'),path('logout', auth_views.LogoutView.as_view(), name='logout'),
path('register', views.register, name="register"),
path('dashboard', views.dashboard,name='dashboard'),
path('add_submission', views.add_submission, name = 'add_submission'),
]