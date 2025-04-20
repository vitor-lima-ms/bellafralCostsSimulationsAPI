from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from cost.models import Cost
from cost.serializers import CostSerializer

# Create your views here.

class CostsAPIView(generics.ListCreateAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer

class CostAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer