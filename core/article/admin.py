from django.contrib import admin

# Register your models here.

from article.models import Article, CommentOnArticle


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(CommentOnArticle)
class CommentOnArticleAdmin(admin.ModelAdmin):
    pass

