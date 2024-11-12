from rest_framework import serializers
from .models import Phim,LichChieu,PhongChieu

class PhimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phim
        fields = '__all__'

class LichChieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = LichChieu
        fields = '__all__'

class PhongChieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhongChieu
        fields = '__all__'