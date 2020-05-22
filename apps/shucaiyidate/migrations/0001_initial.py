# Generated by Django 2.0.5 on 2020-05-21 10:02

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
            name='TagAttrib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_value_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='节点属性名字')),
                ('tag_value_text', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='节点属性值')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '节点属性',
                'verbose_name_plural': '节点属性',
            },
        ),
        migrations.CreateModel(
            name='TagContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='节点名字')),
                ('is_root', models.BooleanField(default=False, verbose_name='是否根节点')),
                ('tag_level', models.CharField(blank=True, default='', help_text='节点层数，根目录层数为1，根目录下层数为2，依次往下为3、4、5等等', max_length=100, null=True, verbose_name='节点层数')),
                ('tag_text', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='节点文本内容')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('tag_father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shucaiyidate.TagContent', verbose_name='依赖父节点')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '节点配置',
                'verbose_name_plural': '节点配置',
            },
        ),
        migrations.CreateModel(
            name='XieyiConfigDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_project', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('test_module', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='测试模块')),
                ('test_page', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('case_priority', models.CharField(blank=True, choices=[('P0', '冒烟用例'), ('P1', '系统的重要功能用例'), ('P2', '系统的一般功能用例'), ('P3', '极低级别的用例')], default='P1', max_length=10, null=True, verbose_name='用例优先级')),
                ('test_case_title', models.CharField(default='', max_length=200, verbose_name='测试内容的名称')),
                ('is_run_case', models.BooleanField(default=True, verbose_name='是否运行')),
                ('telnet_host_ip', models.CharField(default='192.168.101.133', max_length=100, verbose_name='数采仪IP地址')),
                ('telnet_username', models.CharField(default='root', max_length=100, verbose_name='登录数采仪的用户名')),
                ('telnet_password', models.CharField(default='wwyc8888', max_length=100, verbose_name='登录数采仪的密码')),
                ('xieyi_bin_dir', models.CharField(default='/usr/app_install/collect/bin', max_length=100, verbose_name='数采仪存放协议二进制文件的bin目录')),
                ('xieyi_name', models.CharField(default='11020', max_length=100, verbose_name='协议二进制文件的名字')),
                ('xieyi_test_port', models.CharField(default='4', help_text='请填写数字，例如串口为COM4，则填写4', max_length=100, verbose_name='数采仪协议串口号')),
                ('xieyi_db', models.CharField(default='real.db', max_length=100, verbose_name='协议实时数据存放的数据库名字')),
                ('xieyi_db_remote_path', models.CharField(default='/tmp/real.db', help_text="如数据库路径为'/tmp/real.db',则填写'/tmp/real.db'", max_length=100, verbose_name='协议实时数据存放的数据库在数采仪中的路径')),
                ('xieyi_db_table_name', models.CharField(default='rttable', max_length=100, verbose_name='协议实时数据存放的数据的数据表')),
                ('com_port', models.CharField(default='COM3', help_text='电脑与数采仪连接的USB口，例如USB口为COM4，则填写COM4', max_length=100, verbose_name='电脑与数采仪连接的USB口')),
                ('com_baudrate', models.CharField(default='9600', help_text='协议波特率，一般有4800/9600/19200/38400bps，如协议使用波特率为9600bps，则此处填写9600', max_length=100, verbose_name='协议波特率')),
                ('com_bytesize', models.CharField(default='8', help_text='协议数据位，一般有6、7、8，如协议使用数据位为8，则此处填写8', max_length=100, verbose_name='协议数据位')),
                ('com_parity', models.CharField(default='N', help_text='协议校验位，一般有N(无校验)、O（奇校验）、E（偶校验）0、1，若协议使用无校验，则此处填写大写的N；若协议使用奇校验，则此处填写大写的O；若协议使用偶校验，则此处填写大写的E；', max_length=100, verbose_name='协议校验位')),
                ('com_stopbits', models.CharField(default='1', help_text='协议停止位，一般有1、1.5、2，如协议使用停止位为1，则此处填写1', max_length=100, verbose_name='协议停止位')),
                ('com_send_date', models.CharField(default='01 03 02 00 EA 39 CB', help_text='回复指令中的全部内容，如回复的全部数据为：01 03 02 00 EA 39 CB，则此处填写01 03 02 00 EA 39 CB；如需要发送多条指令，则每条指令之间以半角逗号隔开，', max_length=1000, verbose_name='回复指令中的全部内容')),
                ('com_expect_date', models.CharField(default='01 03 12 2D 00 01 11 7B', help_text='预期接收指令的全部内容，如预期接收的全部内容为：01 03 12 2D 00 01 11 7B，则此处填写01 03 12 2D 00 01 11 7B', max_length=100, verbose_name='预期接收指令的全部内容')),
                ('xieyi_jiexi_expect_result_list', models.CharField(default='0.234', help_text='协议解析预期结果，如预期结果为0.234，则此处填写0.234，如有多个预期结果，每个结果之间以半角逗号隔开，如:0.234,9.55', max_length=1000, verbose_name='协议解析预期结果')),
                ('tcp_server_ip', models.CharField(default='192.168.101.123', max_length=100, verbose_name='数据上报平台的IP地址')),
                ('tcp_server_port', models.CharField(default='63503', max_length=100, verbose_name='数据上报平台的端口号')),
                ('is_ftp_upload', models.BooleanField(default=False, verbose_name='是否上传配置文件')),
                ('is_close_xieyi', models.BooleanField(default=False, verbose_name='是否关闭自启动时启动的协议')),
                ('is_restart_xieyi', models.BooleanField(default=False, verbose_name='是否重新启动协议')),
                ('is_com_recive_and_send', models.BooleanField(default=False, verbose_name='是否进行数据接收和发送')),
                ('is_ftp_down_xieyi_file', models.BooleanField(default=False, verbose_name='是否ftp下载获取解析文件')),
                ('is_assert_file_success', models.BooleanField(default=False, verbose_name='是否断言协议预期解析结果在协议解析文件中')),
                ('is_ftp_get_remote_db_file', models.BooleanField(default=False, verbose_name='是否ftp下载远程数据库文件')),
                ('is_assert_real_db_success', models.BooleanField(default=False, verbose_name='是否断言协议预期解析结果在实时数据库的表中')),
                ('is_tcp_server_receive', models.BooleanField(default=False, verbose_name='是否接收平台报文')),
                ('is_assert_tcp_server_receive_success', models.BooleanField(default=False, verbose_name='是否断言协议预期解析结果在接收的报文中')),
                ('case_counts', models.IntegerField(default='1', help_text='循环次数，请填写数字，例如：1、2、3', verbose_name='循环次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('write_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '协议测试用例',
                'verbose_name_plural': '协议测试用例',
            },
        ),
        migrations.AddField(
            model_name='tagattrib',
            name='tagcontent',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='shucaiyidate.TagContent', verbose_name='依赖的节点'),
        ),
        migrations.AddField(
            model_name='tagattrib',
            name='write_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
    ]
