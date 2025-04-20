from django.urls import path
from diaper import views

urlpatterns = [
    path('', views.DiapersAPIView.as_view(), name='diapers'),

    path('<int:pk>/', views.DiaperAPIView.as_view(), name='diaper'),
]