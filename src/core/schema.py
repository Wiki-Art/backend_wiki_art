import graphene
from graphene_django.debug import DjangoDebug

from django.conf import settings

from author.graphql.querry import Query as QueryAuthor
from church.graphql.querry import Query as QueryChurch
from church.graphql.mutation import Mutation as MutationChurch
from work_art.schema import Query as QueryWorkArt


class Query(QueryAuthor, QueryChurch, QueryWorkArt, graphene.ObjectType):
    if settings.DEBUG:
        # Debug output - seeMost APIs don’t just allow you to read data, they also allow you to write. # noqa
        # http://docs.graphene-python.org/projects/django/en/latest/debug/
        debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(MutationChurch, graphene.ObjectType):
    if settings.DEBUG:
        # Debug output - see
        # http://docs.graphene-python.org/projects/django/en/latest/debug/
        debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query,
                         mutation=Mutation,
                         auto_camelcase=False,
                         )
