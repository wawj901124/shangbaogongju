# Generated by Django 2.0.5 on 2020-07-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportdatas', '0006_copyrdmstatic'),
    ]

    operations = [
        migrations.CreateModel(
            name='RdmAutoStatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people_name', models.CharField(default='', max_length=50, verbose_name='人员')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='起始日期')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='结束日期')),
                ('all_task_name', models.TextField(default='', verbose_name='所有任务名称')),
                ('all_task_desc', models.TextField(default='', verbose_name='所有任务详情')),
                ('all_task_quse', models.TextField(default='', verbose_name='所有问题详情')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'RDM日志自动统计某个时段间的任务',
                'verbose_name_plural': 'RDM日志自动统计某个时段间的任务',
            },
        ),
        migrations.AlterField(
            model_name='rdmstatic',
            name='day_task_name',
            field=models.CharField(default='', max_length=1000, verbose_name='日志任务名称'),
        ),
    ]