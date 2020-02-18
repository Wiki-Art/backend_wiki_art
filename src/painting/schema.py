import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from painting.models import WorkArt


class AuthorType(DjangoObjectType):
    class Meta:
        model = WorkArt


class Query(ObjectType):
    work_art = graphene.Field(AuthorType, id=graphene.Int())
    work_arts = graphene.List(AuthorType)

    def resolve_work_art(self, info, **kwargs):
        id = kwargs.get('id', None)

        if id is not None:
            return WorkArt.objects.get(pk=id)

        return None

    def resolve_work_arts(self, info, **kwargs):
        return WorkArt.objects.all()
