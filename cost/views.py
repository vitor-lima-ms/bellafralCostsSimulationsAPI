from rest_framework import generics
# from rest_framework import permissions

from cost.models import Cost
from cost.serializers import CostSerializer
# from cost.permissions import IsSuperUser

# Create your views here.

class CostsAPIView(generics.ListCreateAPIView):
    # permission_classes = (IsSuperUser, permissions.DjangoModelPermissions,) # Modifica o acesso, apenas usuários autenticados podem acessar por get
    queryset = Cost.objects.all()
    serializer_class = CostSerializer

class CostAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer