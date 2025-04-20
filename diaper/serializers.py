from rest_framework import serializers
from diaper.models import Diaper

class DiaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diaper
        fields = '__all__'