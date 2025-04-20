from django.urls import path
from simulation import views

urlpatterns = [
    path('', views.SimulationsAPIView.as_view(), name='simulations'),

    path('<int:pk>/', views.SimulationAPIView.as_view(), name='simulation'),
]