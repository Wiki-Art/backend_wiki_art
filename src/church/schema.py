import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from church.models import Church, ArcticleChurch, PictureChurch
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError
from core.custom_node import CustomNode


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


class ArcticleChurchType(DjangoObjectType):
    class Meta:
        model = ArcticleChurch
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


class Query(ObjectType):
    church = graphene.Field(ChurchType, id=graphene.Int(required=True))
    churches = DjangoFilterConnectionField(ChurchType)
    pictures_churches = DjangoFilterConnectionField(PictureChurchType)
    articles_churches = DjangoFilterConnectionField(ArcticleChurchType)

    def resolve_church(self, info, **kwargs):
        id = kwargs.get('id')
        try:
            return Church.objects.get(pk=id)
        except Exception:
            raise GraphQLError('Church not found')
