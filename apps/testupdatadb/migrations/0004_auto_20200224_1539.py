# Generated by Django 2.0.5 on 2020-02-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testupdatadb', '0003_auto_20200224_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatedbdata',
            name='db_ziduan',
            field=models.CharField(blank=True, default='current_page_click_ele_find_value', help_text='多个字段之间以英文半角逗号(,)隔开，全部字段请输入*', max_length=1000, null=True, verbose_name='数据库中的表的字段名'),
        ),
    ]
