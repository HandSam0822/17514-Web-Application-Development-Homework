# Generated by Django 4.0.2 on 2022-02-26 15:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialnetwork', '0010_remove_comment_user_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ManyToManyField(related_name='commenter', to=settings.AUTH_USER_MODEL),
        ),
    ]
