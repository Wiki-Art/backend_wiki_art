from rest_framework import serializers
from .models import PictureChurch


class PictureChurchSerializer(serializers.ModelSerializer):

    class Meta:
        model = PictureChurch
        fields = ['church', 'picture']
