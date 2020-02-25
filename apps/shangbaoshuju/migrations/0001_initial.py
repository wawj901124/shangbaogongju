# Generated by Django 2.0.5 on 2020-02-23 10:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShangBaoShuJu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_project', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('test_module', models.CharField(default='', max_length=100, verbose_name='测试模块')),
                ('test_page', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('test_case_title', models.CharField(default='', max_length=100, verbose_name='测试内容的名称')),
                ('test_start_time', models.CharField(default='', max_length=100, verbose_name='开始运行时间')),
                ('forcount', models.CharField(default='', max_length=100, verbose_name='循环次数')),
                ('time_delay', models.CharField(default='', max_length=100, verbose_name='次数间上报间隔（单位：秒）')),
                ('is_check_crc', models.BooleanField(default=True, verbose_name='是否进行CRC校验')),
                ('shujuduan_st', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='数据段_系统编码ST')),
                ('shujuduan_cn', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='数据段_命令编码CN')),
                ('shujuduan_pw', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='数据段_访问密码PW')),
                ('shujuduan_mn', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='数据段_站点唯一标识MN')),
                ('shujuduan_flag', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='数据段_应答标志Flag')),
                ('shujuduan_cp_datatime_type', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='数据段_指令参数CP的DataTime类型')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '模拟上报数据工具',
                'verbose_name_plural': '模拟上报数据工具',
            },
        ),
        migrations.CreateModel(
            name='ShuJuYinZi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yinzi_code', models.CharField(default='', max_length=100, verbose_name='因子编码')),
                ('yinzi_rtd_up', models.CharField(default='', max_length=100, verbose_name='因子数值_上限')),
                ('yinzi_rtd_down', models.CharField(default='', max_length=100, verbose_name='因子数值_下限')),
                ('yinzi_rtd_xiaoshuwei', models.CharField(default='1', max_length=100, verbose_name='因子数值_小数位数')),
                ('yinzi_rtd_count', models.CharField(default='1', max_length=100, verbose_name='因子数值个数')),
                ('yinzi_flag', models.CharField(default='', max_length=100, verbose_name='因子标识')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('shangbaoshuju', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shangbaoshuju.ShangBaoShuJu', verbose_name='依赖的模拟上报数据工具')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '数据段_指令参数CP的因子',
                'verbose_name_plural': '数据段_指令参数CP的因子',
            },
        ),
        migrations.CreateModel(
            name='StoreSBShuJu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_project', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('test_module', models.CharField(default='', max_length=100, verbose_name='测试模块')),
                ('test_page', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('test_case_title', models.CharField(default='', max_length=100, verbose_name='测试内容的名称')),
                ('test_start_time', models.CharField(default='', max_length=100, verbose_name='开始运行时间')),
                ('forcount', models.CharField(default='', max_length=100, verbose_name='循环次数')),
                ('time_delay', models.CharField(default='', max_length=100, verbose_name='次数间上报间隔（单位：秒）')),
                ('is_check_crc', models.BooleanField(default=True, verbose_name='是否进行CRC校验')),
                ('sb_yinzi', models.CharField(default='', max_length=5000, verbose_name='上报因子字符串')),
                ('sb_shuju', models.CharField(default='', max_length=5000, verbose_name='上报数据字符串')),
                ('sb_ret', models.CharField(default='', max_length=5000, verbose_name='tcp响应数据')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '模拟上报数据记录',
                'verbose_name_plural': '模拟上报数据记录',
            },
        ),
    ]
