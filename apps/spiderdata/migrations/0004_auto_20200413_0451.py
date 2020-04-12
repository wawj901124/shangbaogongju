# Generated by Django 2.0.5 on 2020-04-13 04:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spiderdata', '0003_spiderdate_prenum'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpiderData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('splider_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='爬取数据URL')),
                ('splider_title', models.CharField(blank=True, default='爬取数据', max_length=1000, null=True, verbose_name='数据标题')),
                ('img_height', models.CharField(blank=True, default=75, max_length=100, null=True, verbose_name='封面图高度')),
                ('img_width', models.CharField(blank=True, default=75, max_length=100, null=True, verbose_name='封面图宽度')),
                ('front_cover_img', models.CharField(blank=True, max_length=1500, null=True, verbose_name='封面图片')),
                ('prenum', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='编号')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '爬取数据查询',
                'verbose_name_plural': '爬取数据查询',
            },
        ),
        migrations.CreateModel(
            name='SpiderDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='导演')),
                ('director_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='制作商外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='SpiderDownLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('down_load', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='下载连接')),
                ('director_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='制作商外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('spiderdata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='spiderdata.SpiderData', verbose_name='作品')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='SpiderGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='类别')),
                ('genre_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='类别外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='SpiderLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='发行商')),
                ('label_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='发行商外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='SpiderStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='演员')),
                ('star_photo', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='演员头像')),
                ('star_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='演员外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='SpiderStudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='制作商')),
                ('studio_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='制作商外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='SpiderVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='视频连接')),
                ('director_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='制作商外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('spiderdata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='spiderdata.SpiderData', verbose_name='作品')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
        ),
        migrations.RemoveField(
            model_name='spiderdate',
            name='write_user',
        ),
        migrations.DeleteModel(
            name='SpiderDate',
        ),
        migrations.AddField(
            model_name='spiderdata',
            name='director',
            field=models.ManyToManyField(blank=True, default='', null=True, to='spiderdata.SpiderDirector', verbose_name='导演'),
        ),
        migrations.AddField(
            model_name='spiderdata',
            name='genre',
            field=models.ManyToManyField(blank=True, default='', null=True, to='spiderdata.SpiderGenre', verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='spiderdata',
            name='label',
            field=models.ManyToManyField(blank=True, default='', null=True, to='spiderdata.SpiderLabel', verbose_name='发行商'),
        ),
        migrations.AddField(
            model_name='spiderdata',
            name='star',
            field=models.ManyToManyField(blank=True, default='', null=True, to='spiderdata.SpiderStar', verbose_name='演员'),
        ),
        migrations.AddField(
            model_name='spiderdata',
            name='studio',
            field=models.ManyToManyField(blank=True, default='', null=True, to='spiderdata.SpiderStudio', verbose_name='制作商'),
        ),
        migrations.AddField(
            model_name='spiderdata',
            name='write_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
    ]
