import graphene
from church.models import Church
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import ObjectType
from graphql import GraphQLError
from .schema import ChurchType, PictureChurchType, ArticleChurchType


class Query(ObjectType):
    church = graphene.Field(ChurchType, id=graphene.Int(required=True))
    random_church = graphene.Field(ChurchType)
    churches = DjangoFilterConnectionField(ChurchType)
    pictures_churches = DjangoFilterConnectionField(PictureChurchType)
    articles_churches = DjangoFilterConnectionField(ArticleChurchType)

    def resolve_church(self, info, **kwargs):
        id = kwargs.get('id')
        try:
            return Church.objects.get(pk=id)
        except Exception:
            raise GraphQLError('Church not found')

    def resolve_random_church(self, info, **kwargs):
        return Church.objects.order_by('?').first()
