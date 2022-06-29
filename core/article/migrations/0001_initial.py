# Generated by Django 3.1.7 on 2022-06-29 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('body', models.TextField()),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to='articles/coverImages/')),
                ('status', models.CharField(choices=[('published', 'Publish'), ('draft', 'draft')], default='draft', max_length=15)),
                ('views', models.PositiveBigIntegerField(default=0)),
                ('created_on_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_on_timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
                ('users_clapped', models.ManyToManyField(blank=True, related_name='clapped_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentOnArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on_timestamp', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='article.article')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='article.commentonarticle')),
            ],
        ),
    ]