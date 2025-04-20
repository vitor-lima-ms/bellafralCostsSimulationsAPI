from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from cost.models import Cost
from cost.serializers import CostSerializer

# Create your views here.

class CostsAPIView(APIView):
    def get(self, request):
        costs = Cost.objects.all()
        serializer = CostSerializer(costs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data['custoGel'])
        serializer = CostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)