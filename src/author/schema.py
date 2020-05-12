import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from author.models import Author, ArticleAuthor
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

    created = graphene.String()

    def resolve_created(self, info):
        return str(self.created.strftime('%d/%m/%Y'))


class ArticleAuthorType(DjangoObjectType):
    class Meta:
        model = ArticleAuthor
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
    random_author = graphene.Field(AuthorType)
    authors = DjangoFilterConnectionField(AuthorType)
    articles_author = DjangoFilterConnectionField(ArticleAuthorType)

    def resolve_author(self, info, **kwargs):
        id = kwargs.get('id')
        try:
            return Author.objects.get(pk=id)
        except Exception:
            raise GraphQLError('Author not found')

    def resolve_random_author(self, info, **kwargs):
        return Author.objects.order_by('?').first()
