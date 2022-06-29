from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

ARTICLE_STATUS_CHOICES = [
    ('published','Publish'),
    ('draft','draft'),
]

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles',)
    title = models.CharField(max_length=155,)
    body = models.TextField()
    cover_picture = models.ImageField(blank = True, null = True, upload_to='articles/coverImages/',)
    status = models.CharField(max_length=15, choices=ARTICLE_STATUS_CHOICES, default='draft',)
    views = models.PositiveBigIntegerField(default=0)
    users_clapped = models.ManyToManyField(User, related_name='clapped_articles', blank=True,)
    created_on_timestamp = models.DateTimeField(auto_now_add=True,)
    updated_on_timestamp = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.title
    



class CommentOnArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments',)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_comments',)
    parent_comment = models.ForeignKey('self', null = True, blank= True, on_delete=models.CASCADE, related_name='replies',)
    body = models.TextField()
    created_on_timestamp = models.DateTimeField(auto_now_add=True)

