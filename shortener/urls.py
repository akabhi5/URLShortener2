from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('result/', views.ResultPageView.as_view(), name='result'),
    path('<str:url>/', views.RedirectToUrl.as_view(), name='redirect'),
]
