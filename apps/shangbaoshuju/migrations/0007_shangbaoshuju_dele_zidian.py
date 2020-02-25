# Generated by Django 2.0.5 on 2020-02-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shangbaoshuju', '0006_auto_20200223_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='shangbaoshuju',
            name='dele_zidian',
            field=models.CharField(blank=True, default='', help_text='多个条件字段之间以英文半角逗号(,)隔开', max_length=1000, null=True, verbose_name='获取目标数据库中因子值对应表所有字段中需要删除的字段'),
        ),
    ]
