from rest_framework import serializers
from .models import PictureWorkArt


class PictureWorkArtSerializer(serializers.ModelSerializer):

    class Meta:
        model = PictureWorkArt
        fields = ['work_art', 'picture']
