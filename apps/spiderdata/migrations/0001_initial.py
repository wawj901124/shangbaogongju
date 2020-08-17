# Generated by Django 2.0.5 on 2020-05-06 13:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('back_front_cover_img', models.ImageField(blank=True, height_field='img_height', max_length=2000, null=True, upload_to='', verbose_name='补传封面图片', width_field='img_width')),
                ('front_cover_img', models.CharField(blank=True, max_length=1500, null=True, verbose_name='封面图片')),
                ('prenum', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='编号')),
                ('long_time', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='时长（分钟）')),
                ('is_love', models.BooleanField(default=False, verbose_name='喜爱')),
                ('is_check', models.BooleanField(default=False, verbose_name='检查封面')),
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
            ],
            options={
                'verbose_name': '导演',
                'verbose_name_plural': '导演',
            },
        ),
        migrations.CreateModel(
            name='SpiderDownLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('down_load', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='下载连接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '下载链接',
                'verbose_name_plural': '下载链接',
            },
        ),
        migrations.CreateModel(
            name='SpiderGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='类别')),
                ('genre_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='类别外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
            },
        ),
        migrations.CreateModel(
            name='SpiderHMArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hm_area', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='地区')),
                ('hm_area_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='地区外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '地区',
                'verbose_name_plural': '地区',
            },
        ),
        migrations.CreateModel(
            name='SpiderHMBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('splider_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='爬取数据URL')),
                ('splider_title', models.CharField(blank=True, default='爬取漫画数据', max_length=1000, null=True, verbose_name='数据标题')),
                ('img_height', models.CharField(blank=True, default=75, max_length=100, null=True, verbose_name='封面图高度')),
                ('img_width', models.CharField(blank=True, default=75, max_length=100, null=True, verbose_name='封面图宽度')),
                ('front_cover_img', models.ImageField(blank=True, height_field='img_height', max_length=2000, null=True, upload_to='hanman/fengmian/', verbose_name='封面图片', width_field='img_width')),
                ('chapter_count', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='章节数')),
                ('is_love', models.BooleanField(default=False, verbose_name='喜爱')),
                ('is_check', models.BooleanField(default=False, verbose_name='检查封面')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '爬取的漫画书',
                'verbose_name_plural': '爬取的漫画书',
            },
        ),
        migrations.CreateModel(
            name='SpiderHMChapterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('splider_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='爬取数据URL')),
                ('splider_title', models.CharField(blank=True, default='爬取漫画数据', max_length=1000, null=True, verbose_name='数据标题')),
                ('chapter_num', models.IntegerField(blank=True, null=True, verbose_name='章节数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '爬取漫画数据查询',
                'verbose_name_plural': '爬取漫画数据查询',
            },
        ),
        migrations.CreateModel(
            name='SpiderHMChapterImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_title', models.CharField(blank=True, default=75, max_length=1000, null=True, verbose_name='图片标题')),
                ('img_height', models.CharField(blank=True, default=75, max_length=100, null=True, verbose_name='图片高度')),
                ('img_width', models.CharField(blank=True, default=75, max_length=100, null=True, verbose_name='图片宽度')),
                ('content_img', models.ImageField(blank=True, height_field='img_height', max_length=2000, null=True, upload_to='hanman/content/', verbose_name='图片', width_field='img_width')),
                ('chapter_image_num', models.IntegerField(blank=True, null=True, verbose_name='图片编号')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '漫画内容',
                'verbose_name_plural': '漫画内容',
            },
        ),
        migrations.CreateModel(
            name='SpiderHMTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hm_tag', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='类型')),
                ('hm_tag_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='类型外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '类型',
                'verbose_name_plural': '类型',
            },
        ),
        migrations.CreateModel(
            name='SpiderLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='发行商')),
                ('label_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='发行商外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '发行商',
                'verbose_name_plural': '发行商',
            },
        ),
        migrations.CreateModel(
            name='SpiderSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='系列')),
                ('series_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='系列外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '系列',
                'verbose_name_plural': '系列',
            },
        ),
        migrations.CreateModel(
            name='SpiderStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='演员')),
                ('star_photo', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='演员头像')),
                ('img_height', models.CharField(blank=True, default=75, max_length=100, null=True, verbose_name='封面图高度')),
                ('img_width', models.CharField(blank=True, default=75, max_length=100, null=True, verbose_name='封面图宽度')),
                ('back_start_photo', models.ImageField(blank=True, height_field='img_height', max_length=2000, null=True, upload_to='', verbose_name='补传演员头像', width_field='img_width')),
                ('star_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='演员外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '演员',
                'verbose_name_plural': '演员',
            },
        ),
        migrations.CreateModel(
            name='SpiderStudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='制作商')),
                ('studio_url', models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='制作商外部链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '制作商',
                'verbose_name_plural': '制作商',
            },
        ),
        migrations.CreateModel(
            name='SpiderVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='视频连接')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('spiderdata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='spiderdata.SpiderData', verbose_name='作品')),
            ],
            options={
                'verbose_name': '视频链接',
                'verbose_name_plural': '视频链接',
            },
        ),
    ]
