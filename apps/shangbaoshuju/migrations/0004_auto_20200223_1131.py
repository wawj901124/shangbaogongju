# Generated by Django 2.0.5 on 2020-02-23 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shangbaoshuju', '0003_auto_20200223_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shangbaoshuju',
            name='mn_sql',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='testupdatadb.UpdateDbData', verbose_name='获取MN依赖的数据库SQL语句场景'),
        ),
    ]
