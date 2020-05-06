from rest_framework import viewsets, mixins
from .serializer import PictureWorkArtSerializer
from .models import PictureWorkArt


class PictureWorkArtUploadView(viewsets.GenericViewSet,
                               mixins.CreateModelMixin):
    queryset = PictureWorkArt.objects.all()
    serializer_class = PictureWorkArtSerializer
