import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from author.models import Author


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class Query(ObjectType):
    actor = graphene.Field(AuthorType, id=graphene.Int())
    actors = graphene.List(AuthorType)

    def resolve_actor(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Author.objects.get(pk=id)

        return None

    def resolve_actors(self, info, **kwargs):
        return Author.objects.all()
