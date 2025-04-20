from rest_framework import serializers
from cost.models import Cost

class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'