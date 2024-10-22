from rest_framework import serializers
from .models import Phim

class PhimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phim
        fields = '__all__'
