# Generated by Django 2.0.5 on 2020-02-16 14:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssertTipText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='验证元素查找风格')),
                ('tip_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='验证元素查找风格的确切值')),
                ('tip_text', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='验证元素文本信息内容')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '验证元素相关内容',
                'verbose_name_plural': '验证元素相关内容',
            },
        ),
        migrations.CreateModel(
            name='ClickAndBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_project', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('test_module', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='测试模块')),
                ('test_page', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('test_case_title', models.CharField(default='', max_length=200, verbose_name='测试内容的名称')),
                ('is_run_case', models.BooleanField(default=True, verbose_name='是否运行')),
                ('is_static_load_page_time', models.BooleanField(default=False, verbose_name='是否统计页面加载时间')),
                ('current_page_click_ele_find', models.CharField(default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, verbose_name='当前页面要点击元素查找风格')),
                ('current_page_click_ele_find_value', models.CharField(default='', max_length=1000, verbose_name='当前页面要点击元素查找风格的确切值')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新窗口')),
                ('next_page_check_ele_find', models.CharField(default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, verbose_name='下一页面标识元素查找风格')),
                ('next_page_check_ele_find_value', models.CharField(default='', max_length=1000, verbose_name='下一页面标识元素查找风格的确切值')),
                ('case_counts', models.IntegerField(default='1', help_text='用例循环次数，请填写数字，例如：1、2、3', verbose_name='用例循环次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '点击场景',
                'verbose_name_plural': '点击场景',
            },
        ),
        migrations.CreateModel(
            name='DeleteAndCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_project', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('test_module', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='测试模块')),
                ('test_page', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('case_priority', models.CharField(blank=True, choices=[('P0', '冒烟用例'), ('P1', '系统的重要功能用例'), ('P2', '系统的一般功能用例'), ('P3', '极低级别的用例')], default='P1', max_length=10, null=True, verbose_name='用例优先级')),
                ('test_case_title', models.CharField(default='', max_length=200, verbose_name='测试内容的名称')),
                ('is_run_case', models.BooleanField(default=True, verbose_name='是否运行')),
                ('delete_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='被删除元素查找风格')),
                ('delete_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='被删除元素查找风格的确切值')),
                ('delete_button_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='删除按钮查找风格')),
                ('delete_button_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='删除按钮查找风格的确切值')),
                ('confirm_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='删除弹框确定按钮查找风格')),
                ('confirm_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='删除弹框确定按钮查找风格的确切值')),
                ('click_confirm_delay_time', models.CharField(blank=True, default='3', help_text='点击确定按钮后的延时时长（单位秒），请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击确定按钮后的延时时长（单位秒）')),
                ('is_click_cancel', models.BooleanField(default=False, verbose_name='是否点击取消按钮')),
                ('cancel_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='删除弹框取消按钮查找风格')),
                ('cancel_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='删除弹框取消按钮查找风格的确切值')),
                ('is_submit_success', models.BooleanField(default=True, verbose_name='是否删除成功')),
                ('popup_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='删除成功弹框中的某个元素查找风格')),
                ('popup_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='删除成功弹框中的某个元素查找风格的确切值')),
                ('popup_text', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='删除成功弹框中的某个元素文本信息内容')),
                ('is_signel_page', models.BooleanField(default=True, verbose_name='是否单页面')),
                ('page_number_xpath', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='页数层xpath路径值')),
                ('result_table_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='结果表格查找风格')),
                ('result_table_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='结果表格查找风格的确切值')),
                ('table_colnum_counts', models.CharField(blank=True, default='', help_text='结果表格总列数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='结果表格总列数')),
                ('case_counts', models.IntegerField(default='1', help_text='循环次数，请填写数字，例如：1、2、3', verbose_name='循环次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '删除场景',
                'verbose_name_plural': '删除场景',
            },
        ),
        migrations.CreateModel(
            name='EditAndCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_project', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('test_module', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='测试模块')),
                ('test_page', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('case_priority', models.CharField(blank=True, choices=[('P0', '冒烟用例'), ('P1', '系统的重要功能用例'), ('P2', '系统的一般功能用例'), ('P3', '极低级别的用例')], default='P1', max_length=10, null=True, verbose_name='用例优先级')),
                ('test_case_title', models.CharField(default='', max_length=200, verbose_name='测试内容的名称')),
                ('is_run_case', models.BooleanField(default=True, verbose_name='是否运行')),
                ('edit_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='被修改元素查找风格')),
                ('edit_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='被修改元素查找风格的确切值')),
                ('edit_button_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='修改按钮查找风格')),
                ('edit_button_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='修改按钮查找风格的确切值')),
                ('confirm_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='确定按钮查找风格')),
                ('confirm_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='确定按钮查找风格的确切值')),
                ('click_confirm_delay_time', models.CharField(blank=True, default='3', help_text='点击确定按钮后的延时时长（单位秒），请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击确定按钮后的延时时长（单位秒）')),
                ('is_click_cancel', models.BooleanField(default=False, verbose_name='是否点击取消按钮')),
                ('cancel_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='取消按钮查找风格')),
                ('cancel_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='取消按钮查找风格的确切值')),
                ('is_submit_success', models.BooleanField(default=True, verbose_name='是否添加成功')),
                ('is_signel_page', models.BooleanField(default=True, verbose_name='是否单页面')),
                ('page_number_xpath', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='页数层xpath路径值')),
                ('result_table_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='结果表格查找风格')),
                ('result_table_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='结果表格查找风格的确切值')),
                ('table_colnum_counts', models.CharField(blank=True, default='', help_text='结果表格总列数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='结果表格总列数')),
                ('case_counts', models.IntegerField(default='1', help_text='循环次数，请填写数字，例如：1、2、3', verbose_name='循环次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '修改场景',
                'verbose_name_plural': '修改场景',
            },
        ),
        migrations.CreateModel(
            name='IframeBodyInputText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iframe_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='iframe查找风格')),
                ('iframe_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='iframe查找风格的确切值')),
                ('input_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='输入框查找风格')),
                ('input_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='输入框查找风格的确切值')),
                ('is_auto_input', models.BooleanField(default=False, verbose_name='是否自动输入')),
                ('auto_input_type', models.CharField(blank=True, choices=[('1', '数字'), ('2', '字母（小写）'), ('3', '字母（大写）'), ('4', '特殊符号'), ('5', '数字和字母（小写）'), ('6', '数字和字母（大写）'), ('7', '字母（大小写）'), ('8', '数字和字母（大小写）'), ('9', '数字和字母和特殊符号'), ('10', '数字和字母和特殊符号和空白字符'), ('11', '汉字'), ('12', '手机号'), ('13', '身份证号')], default='11', max_length=10, null=True, verbose_name='自动输入字符的类型')),
                ('auto_input_long', models.CharField(blank=True, default='300', help_text='字符的个数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='自动输入的字符的个数')),
                ('input_text', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='输入框中要输入的内容')),
                ('is_with_time', models.BooleanField(default=True, verbose_name='是否带时间串')),
                ('is_check', models.BooleanField(default=True, verbose_name='是否进行验证')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '富文本输入框相关内容',
                'verbose_name_plural': '富文本输入框相关内容',
            },
        ),
        migrations.CreateModel(
            name='InputTapInputDateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='时间输入框查找风格')),
                ('input_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='时间输入框查找风格的确切值')),
                ('date_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='日期元素查找风格')),
                ('date_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='日期元素查找风格的确切值')),
                ('last_month_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='上一月按钮查找风格')),
                ('last_month_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='上一月按钮查找风格的确切值')),
                ('click_last_month_counts', models.CharField(blank=True, default='', help_text='点击上一月按钮的次数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击上一月按钮的次数')),
                ('next_month_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='下一月按钮查找风格')),
                ('next_month_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='下一月按钮查找风格的确切值')),
                ('click_next_month_counts', models.CharField(blank=True, default='', help_text='点击下一月按钮的次数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击下一月按钮的次数')),
                ('last_year_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='上一年按钮查找风格')),
                ('last_year_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='上一年按钮查找风格的确切值')),
                ('click_last_year_counts', models.CharField(blank=True, default='', help_text='点击上一年按钮的次数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击上一年按钮的次数')),
                ('next_year_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='下一年按钮查找风格')),
                ('next_year_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='下一年按钮查找风格的确切值')),
                ('click_next_year_counts', models.CharField(blank=True, default='', help_text='点击下一年按钮的次数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击下一年按钮的次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '时间输入框相关内容',
                'verbose_name_plural': '时间输入框相关内容',
            },
        ),
        migrations.CreateModel(
            name='InputTapInputFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='输入框查找风格')),
                ('input_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='输入框查找风格的确切值')),
                ('input_file', models.CharField(blank=True, default='', help_text='多个文件路径之间以半角逗号隔开,例如“D:\\timg.jpg,/root/timg.jpg”，会获取第一个有效路径', max_length=300, null=True, verbose_name='输入框中要输入的文件路径')),
                ('input_class_name', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='隐藏输入框的类名')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '文件输入框相关内容',
                'verbose_name_plural': '文件输入框相关内容',
            },
        ),
        migrations.CreateModel(
            name='InputTapInputText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='输入框查找风格')),
                ('input_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='输入框查找风格的确切值')),
                ('is_auto_input', models.BooleanField(default=False, verbose_name='是否自动输入')),
                ('auto_input_type', models.CharField(blank=True, choices=[('1', '数字'), ('2', '字母（小写）'), ('3', '字母（大写）'), ('4', '特殊符号'), ('5', '数字和字母（小写）'), ('6', '数字和字母（大写）'), ('7', '字母（大小写）'), ('8', '数字和字母（大小写）'), ('9', '数字和字母和特殊符号'), ('10', '数字和字母和特殊符号和空白字符'), ('11', '汉字'), ('12', '手机号'), ('13', '身份证号')], default='11', max_length=10, null=True, verbose_name='自动输入字符的类型')),
                ('auto_input_long', models.CharField(blank=True, default='300', help_text='字符的个数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='自动输入的字符的个数')),
                ('input_text', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='输入框中要输入的内容')),
                ('is_with_time', models.BooleanField(default=True, verbose_name='是否带时间串')),
                ('is_click_clear_icon', models.BooleanField(default=False, verbose_name='是否点击清空图标')),
                ('clear_icon_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='清空图标查找风格')),
                ('clear_icon_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='清空图标查找风格的确切值')),
                ('is_check', models.BooleanField(default=True, verbose_name='是否进行验证')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '文本输入框相关内容',
                'verbose_name_plural': '文本输入框相关内容',
            },
        ),
        migrations.CreateModel(
            name='LoginAndCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_project', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('test_module', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='测试模块')),
                ('test_page', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('case_priority', models.CharField(blank=True, choices=[('P0', '冒烟用例'), ('P1', '系统的重要功能用例'), ('P2', '系统的一般功能用例'), ('P3', '极低级别的用例')], default='P1', max_length=10, null=True, verbose_name='用例优先级')),
                ('test_case_title', models.CharField(default='', max_length=200, verbose_name='测试内容的名称')),
                ('is_run_case', models.BooleanField(default=True, verbose_name='是否运行')),
                ('login_url', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='登录页的url')),
                ('is_auto_input_code', models.BooleanField(default=False, verbose_name='是否自动输入验证码')),
                ('code_image_xpath', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='验证码xpath路径')),
                ('code_type', models.CharField(blank=True, default='n4', help_text='验证码类型：n4(4位纯数字)、n5(5位纯数字)、n6（6位纯数字）、e4（4位纯英文）、e5（5位纯英文）、e6（6位纯英文）、ne4（4位英文数字）、ne5（5位英文数字）、ne6（6位英文数字)', max_length=10, null=True, verbose_name='验证码类型')),
                ('code_input_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='验证码输入框查找风格')),
                ('code_input_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='验证码输入框查找风格的确切值')),
                ('login_button_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='登录按钮查找风格')),
                ('login_button_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='登录按钮查找风格的确切值')),
                ('click_login_button_delay_time', models.CharField(blank=True, default='3', help_text='点击登录按钮后的延时时长（单位秒），请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击登录按钮后的延时时长（单位秒）')),
                ('case_counts', models.IntegerField(default='1', help_text='循环次数，请填写数字，例如：1、2、3', verbose_name='循环次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '登录场景',
                'verbose_name_plural': '登录场景',
            },
        ),
        migrations.CreateModel(
            name='NewAddAndCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_project', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('test_module', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='测试模块')),
                ('test_page', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('case_priority', models.CharField(blank=True, choices=[('P0', '冒烟用例'), ('P1', '系统的重要功能用例'), ('P2', '系统的一般功能用例'), ('P3', '极低级别的用例')], default='P1', max_length=10, null=True, verbose_name='用例优先级')),
                ('test_case_title', models.CharField(default='', max_length=200, verbose_name='测试内容的名称')),
                ('is_run_case', models.BooleanField(default=True, verbose_name='是否运行')),
                ('confirm_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='确定按钮查找风格')),
                ('confirm_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='确定按钮查找风格的确切值')),
                ('click_confirm_delay_time', models.CharField(blank=True, default='3', help_text='点击确定按钮后的延时时长（单位秒），请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击确定按钮后的延时时长（单位秒）')),
                ('is_click_cancel', models.BooleanField(default=False, verbose_name='是否点击取消按钮')),
                ('cancel_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='取消按钮查找风格')),
                ('cancel_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='取消按钮查找风格的确切值')),
                ('is_submit_success', models.BooleanField(default=True, verbose_name='是否添加成功')),
                ('is_signel_page', models.BooleanField(default=False, verbose_name='是否单页面')),
                ('page_number_xpath', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='页数层xpath路径值')),
                ('result_table_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='结果表格查找风格')),
                ('result_table_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='结果表格查找风格的确切值')),
                ('table_colnum_counts', models.CharField(blank=True, default='', help_text='结果表格总列数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='结果表格总列数')),
                ('case_counts', models.IntegerField(default='1', help_text='循环次数，请填写数字，例如：1、2、3', verbose_name='循环次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '新增场景',
                'verbose_name_plural': '新增场景',
            },
        ),
        migrations.CreateModel(
            name='RadioAndReelectionLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='选项标签查找风格')),
                ('label_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='选项标签查找风格的确切值')),
                ('is_check', models.BooleanField(default=True, verbose_name='是否选中')),
                ('checked_add_attribute', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='元素被选中后新增的属性')),
                ('checked_add_attribute_value', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='元素被选中后新增的属性的值')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '单选项和复选项相关内容',
                'verbose_name_plural': '单选项和复选项相关内容',
            },
        ),
        migrations.CreateModel(
            name='SearchAndCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_project', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('test_module', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='测试模块')),
                ('test_page', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('case_priority', models.CharField(blank=True, choices=[('P0', '冒烟用例'), ('P1', '系统的重要功能用例'), ('P2', '系统的一般功能用例'), ('P3', '极低级别的用例')], default='P1', max_length=10, null=True, verbose_name='用例优先级')),
                ('test_case_title', models.CharField(default='', max_length=200, verbose_name='测试内容的名称')),
                ('is_run_case', models.BooleanField(default=True, verbose_name='是否运行')),
                ('search_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='查询按钮查找风格')),
                ('search_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='查询按钮查找风格的确切值')),
                ('is_with_date', models.BooleanField(default=True, verbose_name='是否查询到数据')),
                ('result_table_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='结果表格查找风格')),
                ('result_table_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='结果表格查找风格的确切值')),
                ('case_counts', models.IntegerField(default='1', help_text='循环次数，请填写数字，例如：1、2、3', verbose_name='循环次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('depend_click_case', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='testdatas.ClickAndBack', verbose_name='依赖的点击场景的用例')),
            ],
            options={
                'verbose_name': '查询场景',
                'verbose_name_plural': '查询场景',
            },
        ),
        migrations.CreateModel(
            name='SearchInputTapInputText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='输入框查找风格')),
                ('input_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='输入框查找风格的确切值')),
                ('input_text', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='输入框中要输入的内容')),
                ('search_result_colnum', models.CharField(blank=True, default='', help_text='在搜索结果表格中对应的列数，请填写数字，例如：1、2、3;如果是多列，列数之间以半角逗号隔开，例如：3,4', max_length=100, null=True, verbose_name='在搜索结果表格中对应的列数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('searchandcheck', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='testdatas.SearchAndCheck', verbose_name='依赖的搜素场景')),
            ],
            options={
                'verbose_name': '文本输入框相关内容',
                'verbose_name_plural': '文本输入框相关内容',
            },
        ),
        migrations.CreateModel(
            name='SearchSelectTapSelectOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='选项框的查找风格')),
                ('select_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='选项框查找风格的确切值')),
                ('select_option_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='选项的查找风格')),
                ('select_option_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='选项查找风格的确切值')),
                ('search_result_colnum', models.CharField(blank=True, default='', help_text='在搜索结果表格中对应的列数，请填写数字，例如：1、2、3...', max_length=100, null=True, verbose_name='在搜索结果表格中对应的列数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('searchandcheck', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='testdatas.SearchAndCheck', verbose_name='依赖的搜素场景')),
            ],
            options={
                'verbose_name': '选项框相关内容',
                'verbose_name_plural': '选项框相关内容',
            },
        ),
        migrations.CreateModel(
            name='SelectTapSelectOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_multiple_choices', models.BooleanField(default=False, verbose_name='是否多选')),
                ('select_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='选项框的查找风格')),
                ('select_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='选项框查找风格的确切值')),
                ('select_option_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='选项的查找风格')),
                ('select_option_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='选项查找风格的确切值')),
                ('is_click_clear_icon', models.BooleanField(default=False, verbose_name='是否点击清空图标')),
                ('clear_icon_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='清空图标查找风格')),
                ('clear_icon_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='清空图标查找风格的确切值')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('editandcheck', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='testdatas.EditAndCheck', verbose_name='依赖的修改场景')),
                ('newaddandcheck', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='testdatas.NewAddAndCheck', verbose_name='依赖的添加场景')),
            ],
            options={
                'verbose_name': '选项框相关内容',
                'verbose_name_plural': '选项框相关内容',
            },
        ),
        migrations.CreateModel(
            name='SelectTapSelectText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='选项框的查找风格')),
                ('select_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='选项框查找风格的确切值')),
                ('select_option_text', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='选项的文本的内容')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('editandcheck', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='testdatas.EditAndCheck', verbose_name='依赖的修改场景')),
                ('newaddandcheck', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='testdatas.NewAddAndCheck', verbose_name='依赖的添加场景')),
            ],
            options={
                'verbose_name': '选项框及选项文本内容',
                'verbose_name_plural': '选项框及选项文本内容',
            },
        ),
    ]
