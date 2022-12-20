# Generated by Django 3.2.13 on 2022-10-13 04:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='folowers', to=settings.AUTH_USER_MODEL),
        ),
    ]
