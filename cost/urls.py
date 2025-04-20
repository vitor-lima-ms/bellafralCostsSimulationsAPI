from django.urls import path
from cost import views

urlpatterns = [
    path('', views.CostsAPIView.as_view(), name='costs'),
]