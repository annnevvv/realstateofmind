# Generated by Django 4.2.5 on 2023-09-14 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postscomments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostsComments',
            new_name='PostComment',
        ),
        migrations.RenameIndex(
            model_name='postcomment',
            new_name='blog_postco_created_0241eb_idx',
            old_name='blog_postsc_created_d993ec_idx',
        ),
    ]
