import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from painting.models import WorkArt


class WorkArtType(DjangoObjectType):
    class Meta:
        model = WorkArt
        fields = '__all__'


class Query(ObjectType):
    work_art = graphene.Field(WorkArtType, id=graphene.Int())
    work_arts = graphene.List(WorkArtType)

    def resolve_work_art(self, info, **kwargs):
        id = kwargs.get('id', None)

        if id is not None:
            return WorkArt.objects.get(pk=id)

        return None

    def resolve_work_arts(self, info, **kwargs):
        return WorkArt.objects.all()
