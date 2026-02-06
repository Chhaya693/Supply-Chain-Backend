from django.contrib import admin
from django.urls import path
from account.views import RegisterAPI,LoginView

urlpatterns = [
    path('register/',view=RegisterAPI.as_view() ),
    path('login/',view=LoginView.as_view() ),
]