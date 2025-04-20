from rest_framework import generics
from diaper.models import Diaper
from diaper.serializers import DiaperSerializer

# Create your views here.

class DiapersAPIView(generics.ListCreateAPIView):
    queryset = Diaper.objects.all()
    serializer_class = DiaperSerializer

class DiaperAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diaper.objects.all()
    serializer_class = DiaperSerializer