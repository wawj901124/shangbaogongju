# Generated by Django 2.0.5 on 2020-04-13 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spiderdata', '0005_auto_20200413_0457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spiderdirector',
            options={'verbose_name': '导演', 'verbose_name_plural': '导演'},
        ),
        migrations.AlterModelOptions(
            name='spiderdownload',
            options={'verbose_name': '下载链接', 'verbose_name_plural': '下载链接'},
        ),
        migrations.AlterModelOptions(
            name='spidergenre',
            options={'verbose_name': '类别', 'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='spiderlabel',
            options={'verbose_name': '发行商', 'verbose_name_plural': '发行商'},
        ),
        migrations.AlterModelOptions(
            name='spiderstar',
            options={'verbose_name': '演员', 'verbose_name_plural': '演员'},
        ),
        migrations.AlterModelOptions(
            name='spiderstudio',
            options={'verbose_name': '制作商', 'verbose_name_plural': '制作商'},
        ),
        migrations.AlterModelOptions(
            name='spidervideo',
            options={'verbose_name': '视频链接', 'verbose_name_plural': '视频链接'},
        ),
    ]
