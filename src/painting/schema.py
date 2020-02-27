import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from painting.models import WorkArt, ArcticleWorkArt, PictureWorkArt
from core.custom_node import CustomNode
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError


class WorkArtType(DjangoObjectType):
    class Meta:
        model = WorkArt
        filter_fields = {
            'name': ['icontains', 'exact'],
            'title': ['icontains', 'exact'],
            'state': ['exact'],
            'city': ['icontains', 'exact'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)


class ArcticleWorkArtType(DjangoObjectType):
    class Meta:
        model = ArcticleWorkArt
        filter_fields = {
            'work_art__name': ['exact', 'icontains'],
            'work_art__state': ['exact'],
            'work_art__city': ['icontains', 'exact'],
            'author_send': ['icontains', 'exact'],
            'valid': ['exact'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)


class PictureWorkArtType(DjangoObjectType):
    class Meta:
        model = PictureWorkArt
        filter_fields = {
            'work_art__name': ['exact', 'icontains'],
            'work_art__state': ['exact'],
            'work_art__city': ['exact', 'icontains'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)


class Query(ObjectType):
    work_art = graphene.Field(WorkArtType, id=graphene.Int(required=True))
    work_arts = DjangoFilterConnectionField(WorkArtType)
    articles_work_arts = DjangoFilterConnectionField(ArcticleWorkArtType)
    pictures_work_arts = DjangoFilterConnectionField(PictureWorkArtType)

    def resolve_church(self, info, **kwargs):
        id = kwargs.get('id')
        try:
            return WorkArt.objects.get(pk=id)
        except Exception:
            raise GraphQLError('WorkArt not found')
