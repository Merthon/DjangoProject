# Generated by Django 5.1.5 on 2025-02-24 12:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='分类名称，必须唯一', max_length=100, unique=True)),
                ('description', models.TextField(blank=True, help_text='分类描述，可选', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='文章标题', max_length=200)),
                ('slug', models.SlugField(help_text='文章唯一标识（用于 URL 中）', max_length=200, unique=True)),
                ('content', models.TextField(help_text='文章正文内容')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='文章创建时间，自动记录')),
                ('updated', models.DateTimeField(auto_now=True, help_text='文章更新时间，自动更新')),
                ('author', models.ForeignKey(help_text='文章作者，关联 Django 内置用户模型', on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, help_text='文章所属分类，可为空', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章列表',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(help_text='评论作者名称', max_length=80)),
                ('email', models.EmailField(help_text='评论作者邮箱', max_length=254)),
                ('body', models.TextField(help_text='评论内容')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='评论创建时间')),
                ('active', models.BooleanField(default=True, help_text='评论是否激活（过滤垃圾评论）')),
                ('post', models.ForeignKey(help_text='关联的文章', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论列表',
                'ordering': ('created',),
            },
        ),
    ]
