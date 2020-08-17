# Generated by Django 2.0.5 on 2020-05-06 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reportpageloadtime', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pageloadtimereporttwosecond',
            name='write_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='pageloadtimereporttheresecond',
            name='write_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='pageloadtimereportonesecond',
            name='write_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='pageloadtimereportfoursecond',
            name='write_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='pageloadtimereportfivesecond',
            name='write_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
    ]