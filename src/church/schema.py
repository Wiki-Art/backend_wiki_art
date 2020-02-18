import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from church.models import Church


class AuthorType(DjangoObjectType):
    class Meta:
        model = Church


class Query(ObjectType):
    church = graphene.Field(AuthorType, id=graphene.Int())
    churchs = graphene.List(AuthorType)

    def resolve_church(self, info, **kwargs):
        id = kwargs.get('id', None)

        if id is not None:
            return Church.objects.get(pk=id)

        return None

    def resolve_churchs(self, info, **kwargs):
        return Church.objects.all()
