import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from author.models import Author, ArcticleAuthor
from core.custom_node import CustomNode
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = {
            'name': ['icontains', 'exact'],
            'race': ['exact'],
            'state': ['exact'],
            'city': ['icontains', 'exact'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)


class ArcticleAuthorType(DjangoObjectType):
    class Meta:
        model = ArcticleAuthor
        filter_fields = {
            'author': ['exact'],
            'author_send': ['icontains', 'exact'],
            'valid': ['exact'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)


class Query(ObjectType):
    author = graphene.Field(AuthorType, id=graphene.Int(required=True))
    authors = DjangoFilterConnectionField(AuthorType)
    articles_churches = DjangoFilterConnectionField(ArcticleAuthorType)

    def resolve_church(self, info, **kwargs):
        id = kwargs.get('id')
        try:
            return Author.objects.get(pk=id)
        except Exception:
            raise GraphQLError('Author not found')
