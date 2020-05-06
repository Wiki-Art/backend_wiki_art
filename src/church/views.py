from rest_framework import viewsets, mixins
from .serializer import PictureChurchSerializer
from .models import PictureChurch


class PictureChurchUploadView(viewsets.GenericViewSet,
                              mixins.CreateModelMixin):
    queryset = PictureChurch.objects.all()
    serializer_class = PictureChurchSerializer
