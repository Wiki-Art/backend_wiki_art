import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from author.models import Author


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class Query(ObjectType):
    author = graphene.Field(AuthorType, id=graphene.Int())
    authors = graphene.List(AuthorType)

    def resolve_author(self, info, **kwargs):
        id = kwargs.get('id', None)

        if id is not None:
            return Author.objects.get(pk=id)

        return None

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()
