import graphene
from church.models import ArticleChurch, Church, PictureChurch
from core.custom_node import CustomNode
from graphene_django.types import DjangoObjectType


class ChurchType(DjangoObjectType):
    class Meta:
        model = Church
        filter_fields = {
            'name': ['icontains', 'exact'],
            'year_foundation': ['exact'],
            'state': ['exact'],
            'city': ['icontains', 'exact'],
            'author_send': ['icontains', 'exact'],
            'valid': ['exact'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)

    created = graphene.String()

    def resolve_created(self, info):
        return str(self.created.strftime('%d/%m/%Y'))


class ArticleChurchType(DjangoObjectType):
    class Meta:
        model = ArticleChurch
        filter_fields = {
            'church__name': ['exact', 'icontains'],
            'church__state': ['exact'],
            'church__city': ['icontains', 'exact'],
            'author_send': ['icontains', 'exact'],
            'valid': ['exact'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)


class PictureChurchType(DjangoObjectType):
    class Meta:
        model = PictureChurch
        filter_fields = {
            'church__name': ['exact', 'icontains'],
            'church__state': ['exact'],
            'church__city': ['exact', 'icontains'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)
