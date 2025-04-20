from django.urls import path
from cost import views

urlpatterns = [
    path('', views.CostsAPIView.as_view(), name='costs'),

    path('<int:pk>', views.CostAPIView.as_view(), name='cost'),
]