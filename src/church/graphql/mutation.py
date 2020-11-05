import graphene
from church.models import Church, ArticleChurch
from graphene_django.types import ObjectType
from .schema import ChurchType, ArticleChurchType


class ArticleChurchInput(graphene.InputObjectType):
    url = graphene.String(required=True)


class ChurchMutation(graphene.Mutation):
    class Arguments:
        author_send = graphene.String(required=True)
        name = graphene.String(required=True)
        year_foundation = graphene.Int(required=True)
        state = graphene.String(required=True)
        city = graphene.String(required=True)
        articles = graphene.List(ArticleChurchInput)

    church = graphene.Field(ChurchType)
    articles = graphene.List(ArticleChurchType)
    ok = graphene.Boolean()

    def mutate(self, info, **kwargs):
        author_send = kwargs.get('author_send')
        name = kwargs.get('name')
        year_foundation = kwargs.get('year_foundation')
        state = kwargs.get('state')
        city = kwargs.get('city')
        articles = kwargs.get('articles', None)
        church = Church.objects.create(author_send=author_send, name=name,
                                       year_foundation=year_foundation,
                                       state=state, city=city)

        if articles is not None:
            articles = [ArticleChurch.objects.create(
                url=article['url'], church=church) for article in articles]

        return ChurchMutation(church=church, ok=True, articles=articles)


class ArticleChurchMutation(graphene.Mutation):
    class Arguments:
        author_send = graphene.String(required=True)
        url = graphene.String(required=True)
        church_id = graphene.Int(required=True)

    article = graphene.Field(ArticleChurchType)
    ok = graphene.Boolean()

    def mutate(self, info, **kwargs):
        author_send = kwargs.get('author_send')
        url = kwargs.get('url')
        church_id = kwargs.get('church_id')
        church = Church.objects.get(pk=church_id)
        article = ArticleChurch.objects.create(author_send=author_send,
                                               url=url, church=church,)

        return ArticleChurchMutation(article=article, ok=True)


class Mutation(ObjectType):
    create_church = ChurchMutation.Field()
    create_article = ArticleChurchMutation.Field()
