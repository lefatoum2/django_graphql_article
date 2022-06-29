import graphene

import article.schema

class Query(article.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)