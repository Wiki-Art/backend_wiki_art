import graphene
from church.models import ArticleChurch, Church, PictureChurch
from core.custom_node import CustomNode
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType, ObjectType
from graphql import GraphQLError


class ChurchType(DjangoObjectType):
    class Meta:
        model = Church
        filter_fields = {
            'name': ['icontains', 'exact'],
            'year_foundation': ['exact'],
            'state': ['exact'],
            'city': ['icontains', 'exact'],
            'author_send': ['icontains', 'exact'],
            'valid': ['exact'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)

    created = graphene.String()

    def resolve_created(self, info):
        return str(self.created.strftime('%d/%m/%Y'))


class ArticleChurchType(DjangoObjectType):
    class Meta:
        model = ArticleChurch
        filter_fields = {
            'church__name': ['exact', 'icontains'],
            'church__state': ['exact'],
            'church__city': ['icontains', 'exact'],
            'author_send': ['icontains', 'exact'],
            'valid': ['exact'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)


class PictureChurchType(DjangoObjectType):
    class Meta:
        model = PictureChurch
        filter_fields = {
            'church__name': ['exact', 'icontains'],
            'church__state': ['exact'],
            'church__city': ['exact', 'icontains'],
            'created': ['exact'],
            'edited': ['exact'],
        }
        interfaces = (CustomNode,)


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


class Query(ObjectType):
    church = graphene.Field(ChurchType, id=graphene.Int(required=True))
    random_church = graphene.Field(ChurchType)
    churches = DjangoFilterConnectionField(ChurchType)
    pictures_churches = DjangoFilterConnectionField(PictureChurchType)
    articles_churches = DjangoFilterConnectionField(ArticleChurchType)

    def resolve_church(self, info, **kwargs):
        id = kwargs.get('id')
        try:
            return Church.objects.get(pk=id)
        except Exception:
            raise GraphQLError('Church not found')

    def resolve_random_church(self, info, **kwargs):
        return Church.objects.order_by('?').first()


class Mutation(ObjectType):
    create_church = ChurchMutation.Field()
    create_article = ArticleChurchMutation.Field()
