# Generated by Django 2.0.5 on 2020-08-30 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapidatas', '0004_auto_20200830_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestdatas',
            name='depend_response_ziduan',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='依赖接口的响应的字段'),
        ),
    ]