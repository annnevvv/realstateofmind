# Generated by Django 4.2.5 on 2023-09-13 12:01

import datetime
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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('content', models.TextField(max_length=3000)),
                ('publictiondate', models.DateTimeField(default=datetime.datetime(2023, 9, 13, 12, 1, 45, 324923, tzinfo=datetime.timezone.utc))),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
                ('visible', models.BooleanField(default=1)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Public')], default='DF', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['publictiondate'],
                'indexes': [models.Index(fields=['publictiondate'], name='blog_post_publict_75c1c4_idx')],
            },
        ),
    ]
