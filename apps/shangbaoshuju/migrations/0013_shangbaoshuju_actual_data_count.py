# Generated by Django 2.0.5 on 2020-03-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shangbaoshuju', '0012_remove_shangbaoshuju_test_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='shangbaoshuju',
            name='actual_data_count',
            field=models.CharField(default='2', help_text='例如上报一条数据，则目标数据库中会出现上报的报文，此处应该填写1；若上报一条数据后需要再上报一条数据，然后目标数据库中才会出现第一次上报的报文，则此处应该填写2；依次类推...', max_length=100, verbose_name='目标数据库中接受到报文需要进行报文的次数'),
        ),
    ]
