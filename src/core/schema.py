import graphene
from graphene_django.debug import DjangoDebug

from django.conf import settings

from author.schema import Query as QueryAuthor
from church.schema import Query as QueryChurch
from painting.schema import Query as QueryWorkArt


class Query(QueryAuthor, QueryChurch, QueryWorkArt, graphene.ObjectType):
    if settings.DEBUG:
        # Debug output - see
        # http://docs.graphene-python.org/projects/django/en/latest/debug/
        debug = graphene.Field(DjangoDebug, name='__debug')


# class Mutation(App1Mutation, App2Mutation, graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query,
                         # mutation=Mutation
                         )
