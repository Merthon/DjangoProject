# Generated by Django 5.1.5 on 2025-02-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FateAnalysisRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(help_text='微信用户唯一标识', max_length=64)),
                ('birth_datetime', models.DateTimeField(help_text='出生日期和时间，格式应为 YYYY-MM-DD HH:MM:SS')),
                ('birth_place', models.CharField(help_text='出生地点', max_length=100)),
                ('analysis_result', models.TextField(help_text='命理分析详细报告')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='记录创建时间')),
            ],
        ),
    ]
