import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from church.models import Church


class ChurchType(DjangoObjectType):
    class Meta:
        model = Church
        fields = '__all__'


class Query(ObjectType):
    church = graphene.Field(ChurchType, id=graphene.Int())
    churchs = graphene.List(ChurchType)

    def resolve_church(self, info, **kwargs):
        id = kwargs.get('id', None)

        if id is not None:
            return Church.objects.get(pk=id)

        return None

    def resolve_churchs(self, info, **kwargs):
        return Church.objects.all()
