# Generated by Django 2.0.5 on 2020-07-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportdatas', '0007_auto_20200716_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdmautostatic',
            name='all_task_desc',
            field=models.TextField(blank=True, default='', null=True, verbose_name='所有任务详情'),
        ),
        migrations.AlterField(
            model_name='rdmautostatic',
            name='all_task_name',
            field=models.TextField(blank=True, default='', null=True, verbose_name='所有任务名称'),
        ),
        migrations.AlterField(
            model_name='rdmautostatic',
            name='all_task_quse',
            field=models.TextField(blank=True, default='', null=True, verbose_name='所有问题详情'),
        ),
    ]
