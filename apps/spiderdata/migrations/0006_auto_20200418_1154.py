# Generated by Django 2.0.5 on 2020-04-18 11:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spiderdata', '0005_auto_20200418_1148'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SpiderHMData',
            new_name='SpiderHMChapterData',
        ),
    ]
