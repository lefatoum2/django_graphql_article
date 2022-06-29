import graphene 
from graphene_django import DjangoObjectType

from article.models import(
    Article, CommentOnArticle,
)

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article

class CommentOnArticleType(DjangoObjectType):
    class Meta:
        model = CommentOnArticle
        fiels = ('id','commenter','replies','body','created_on_timestamp',)


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType)
    article = graphene.Field(ArticleType, id = graphene.Int(required=True))

    def resolve_articles(root, info):
        return Article.objects.all()

    def resolve_article(root, info, id =None):
        return Article.objects.get(pk=id)