from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING,MEDIA_ROOT
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

from .definehelptext import definehelptext


#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值

#让上传的文件路径动态地与config_project的名字有关
def upload_dev_file_path(instance, filename):  #instance代表模式示例，filename代表上传文件的名字
    file_path = '/'.join(["Dev", "{}_{}".format(instance.id, instance.config_project), filename])
    print(file_path)
    return  file_path
    # return '/'.join([MEDIA_ROOT, "Dev","%s_%s".format(instance.id,instance.config_project), filename])

#让上传的文件路径动态地与config_project的名字有关
def upload_local_file_path(instance, filename):  #instance代表模式示例，filename代表上传文件的名字
    file_path = '/'.join(["Local", "{}_{}".format(instance.id, instance.config_project), filename])
    print(file_path)
    return  file_path
    # return '/'.join([MEDIA_ROOT, "Dev","%s_%s".format(instance.id,instance.config_project), filename])

class NodeConfig(models.Model):
    config_project = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"项目名称")
    config_file_name = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"文件名称")
    config_xieyi_num = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"协议编号")
    config_xieyi_type = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("HEX", "HEX"), ("ASCII", "ASCII")),
                                     default="HEX",
                                     verbose_name=u"协议类型")
    config_version = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"版本号",
                                      help_text=u" 版本号配置，每次修改配置都需要更新，一般取配置日期作为版本号,例如：v20180423")
    config_device = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"设备名称",
                                      help_text=u"设备名称，一般取仪器的名称，例如：雪迪龙U23分析仪")
    config_collect_packet_len = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"采集指令_应答包最大长度",
                                      help_text=u"采集指令_应答包长度配置，前端仪器回复包的最大长度，如果不写默认1024")

    local_file = models.FileField(upload_to=upload_local_file_path,  blank=True, null=True,verbose_name="上传的原dev文件")
    dev_file = models.FileField(upload_to=upload_dev_file_path,  blank=True, null=True,verbose_name="生成的dev文件")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"Dev配置"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-【{}】".format(self.id,self.config_project)

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        save_local_to_db_html = "<a href='{}/shucaiyidate/nodeconfigreadandsave/{}/'>入库原上传Dev文件</a>&nbsp;&nbsp;</br>".format(DJANGO_SERVER_YUMING, self.id)
        if self.local_file:   #如果有则显示
            open_local_html = "<a href='{}{}'>下载原上传Dev文件</a>&nbsp;&nbsp;</br>".format(DJANGO_SERVER_YUMING,self.local_file.url)
        else:  #否则不显示
            open_local_html = ""
        make_dev_from_db_html = "<a href='{}/shucaiyidate/nodeconfigmakedev/{}/'>生成新Dev文件</a>&nbsp;&nbsp;</br>".format(DJANGO_SERVER_YUMING,self.id)
        if self.dev_file:   #如果有则显示
            open_dev_html = "<a href='{}{}'>下载新Dev文件</a>&nbsp;&nbsp;</br>".format(DJANGO_SERVER_YUMING,self.dev_file.url)
        else:  #否则不显示
            open_dev_html = ""
        copy_html = "<a href='{}/shucaiyidate/nodeconfigallcopy/{}/'>复制新加当前数据</a>&nbsp;&nbsp;</br>".format(DJANGO_SERVER_YUMING,self.id)

        all_html =save_local_to_db_html+open_local_html+make_dev_from_db_html+open_dev_html+copy_html
        return mark_safe(all_html)
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"操作"   #为go_to函数名个名字


class ConfigCollectSendCmd(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    config_collect_send_id = models.CharField(max_length=100, default="rtdCollect", null=True, blank=True,
                                              verbose_name=u"采集指令-下发指令_下发指令ID",
                                              help_text=u"可以为空，起到一个说明作用")

    config_collect_send_format = models.CharField(max_length=10,null=True, blank=True,
                                                  choices=(("HEX", "HEX"), ("ASCII", "ASCII")),
                                                  default="HEX",
                                                  verbose_name=u"采集指令-下发指令_下发指令类型",
                                                  help_text=definehelptext.config_collect_send_format_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                           verbose_name=u"采集指令-下发指令_下发指令类型",
        #                                           help_text=definehelptext.config_collect_send_format_help_text)

    # config_collect_send_cmd = models.CharField(max_length=1000, default="", null=True, blank=True,
    #                                            verbose_name=u"具体下发指令",
    #                                            help_text=definehelptext.config_collect_send_cmd_help_text)
    config_collect_send_cmd = models.TextField(max_length=1000, default="", null=True, blank=True,
                                               verbose_name=u"具体下发指令",
                                               help_text=definehelptext.config_collect_send_cmd_help_text)

    config_collect_send_acktype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"采集指令-下发指令_数据的回复类型",
                                                   help_text=definehelptext.config_collect_send_acktype_help_text)

    config_collect_send_ackhead = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"采集指令-下发指令_回复数据的包头",
                                                   help_text=u"支持宏定义，”${}”,</br>"
                                                             u"只有在R_HEAD_TAIL和R_HEAD_LEN这两种报文格式下才有意义，</br>"
                                                             u"其他为空即可。")
    config_collect_send_acktail = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"采集指令-下发指令_回复报文的包尾",
                                                   help_text=u"也支持宏定义，</br>"
                                                             u"只有在R_HEAD_TAIL和R_TAIL_ONLY这两种报文格式下才有意义，</br>"
                                                             u"其他为空即可。")
    config_collect_send_acklen = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"采集指令-下发指令_回复报文的总长度",
                                                  help_text=u"只有在R_HEAD_LEN和R_LEN_ONLY这两种报文格式下才有意义，</br>"
                                                            u"其他为空即可。")
    config_collect_send_ackgap = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"采集指令-下发指令_回复报文的分包间隔",
                                                  help_text=u"一般为空即可")
    config_collect_send_ackcheckmode = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-下发指令_回复报文的检验",
                                                        help_text=definehelptext.config_collect_send_ackcheckmode_help_text)

    config_collect_send_ackcheckarg = models.CharField(max_length=100, default="", null=True, blank=True,
                                                       verbose_name=u"采集指令-下发指令_回复报文的固定标识检验参数",
                                                       help_text=u"只有固定标识才有意义，一般为空。")


    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"采集指令_下发指令"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}".format(self.nodeconfig,self.config_collect_send_cmd)

class ConfigCollectFactor(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    configcollectsendcmd = models.ForeignKey(ConfigCollectSendCmd,default="", null=True, blank=True,
                                   verbose_name=u"依赖的采集下发指令",on_delete=models.PROTECT)

    config_collect_factor_factorcode = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-监测因子_监测因子代码",
                                                        help_text=u"例如：w01018")

    config_collect_factor_findmode = models.CharField(max_length=10,null=True, blank=True,
                                                      choices=(("OFFSET", "OFFSET"), ("MARK", "MARK")),
                                                      default="OFFSET",
                                                      verbose_name=u"采集指令-监测因子_查找模式",
                                                      help_text=definehelptext.config_collect_factor_findmode_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                               verbose_name=u"采集指令-监测因子_查找模式",
        #                                               help_text=definehelptext.config_collect_factor_findmode_help_text)


    config_collect_factor_offset = models.CharField(max_length=100, default="", null=True, blank=True,
                                                    verbose_name=u"采集指令-监测因子_偏移量",
                                                    help_text=u"相对包头的，只针对固定偏移模式；")

    config_collect_factor_mark = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"采集指令-监测因子_固定标识",
                                                  help_text=u"针对固定标识模式；")

    config_collect_factor_len = models.CharField(max_length=100, default="", null=True, blank=True,
                                                 verbose_name=u"采集指令-监测因子_解析的宽度")

    config_collect_factor_decodetype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-监测因子_数据解析算法",
                                                        help_text= definehelptext.config_collect_factor_decodetype_help_text)

    config_collect_factor_operator = models.CharField(max_length=100, default="*", null=True, blank=True,
                                                      verbose_name=u"采集指令-监测因子_操作符",
                                                      help_text=u"无特殊需求写*即可")
    config_collect_factor_operand = models.CharField(max_length=100, default="1", null=True, blank=True,
                                                     verbose_name=u"采集指令-监测因子_操作数",
                                                     help_text=u"无特殊需求写1即可")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"采集指令_监测因子"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.config_collect_factor_factorcode

class ConfigCollectReceivePors(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    configcollectsendcmd = models.ForeignKey(ConfigCollectSendCmd,default="", null=True, blank=True,
                                   verbose_name=u"依赖的采集下发指令",on_delete=models.PROTECT)

    config_collect_receive_pors_factorcode=models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态的代码",
                                                        help_text=u"例如：i1210A；"
                                                                  u"<br/>注意：当参数或者状态代码为SampleTime时，为特殊参数或者状态，</br>"
                                                                  u"该参数或者状态代表前端仪器的采样时间，在发送给数据库时该参数或者状态是不发送的，</br>"
                                                                  u"而是在实时数据发送时将该参数的值赋值给采样时间发送。")
    config_collect_receive_pors_factortype= models.CharField(max_length=10,null=True, blank=True,
                                                             choices=(("PARAM", "PARAM"), ("STATE", "STATE")),
                                                             default="PARAM",
                                                             verbose_name=u"采集指令-回复指令_采集的参数或者状态的类型",
                                                             help_text=definehelptext.config_collect_receive_pors_factortype_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                 verbose_name=u"采集指令-回复指令_采集的参数或者状态的类型",
        #                                                 help_text=definehelptext.config_collect_receive_pors_factortype_help_text)

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"采集指令_回复指令中的参数或状态"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}".format(self.configcollectsendcmd,self.config_collect_receive_pors_factorcode)

class ConfigCollectReceivePorsSection(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)

    configcollectreceivepors = models.ForeignKey( ConfigCollectReceivePors,default="", null=True, blank=True,
                                   verbose_name=u"依赖的采集指令之回复指令中的参数或状态",on_delete=models.PROTECT)

    config_collect_receive_pors_section_datatype = models.CharField(max_length=10,null=True, blank=True,
                                                                    choices=(("FLOAT", "FLOAT"), ("INT", "INT")),
                                                                    default="FLOAT",
                                                                    verbose_name=u"采集指令-回复指令_采集的参数或者状态_数据类型",
                                                                    help_text=definehelptext.config_collect_receive_pors_section_datatype_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                             verbose_name=u"采集指令-回复指令_采集的参数或者状态_数据类型",
        #                                                             help_text=definehelptext.config_collect_receive_pors_section_datatype_help_text)

    config_collect_receive_pors_section_strformat = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                     verbose_name=u"采集指令-回复指令_采集的参数或者状态_数据转换为字符串的格式",
                                                                     help_text=definehelptext.config_collect_receive_pors_section_strformat_help_text)
    config_collect_receive_pors_section_findmode = models.CharField(max_length=10,null=True, blank=True,
                                                                    choices=(("OFFSET", "OFFSET"), ("MARK", "MARK")),
                                                                    default="OFFSET",
                                                                    verbose_name=u"采集指令-回复指令_采集的参数或者状态_查找模式",
                                                                    help_text=definehelptext.config_collect_receive_pors_section_findmode_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                             verbose_name=u"采集指令-回复指令_采集的参数或者状态_查找模式",
        #                                                             help_text=definehelptext.config_collect_receive_pors_section_findmode_help_text)

    config_collect_receive_pors_section_offset = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                  verbose_name=u"采集指令-回复指令_采集的参数或者状态_偏移量",
                                                                  help_text=u"相对包头的，只针对固定偏移模式；")

    config_collect_receive_pors_section_mark = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                verbose_name=u"采集指令-回复指令_采集的参数或者状态_固定标识",
                                                                help_text=u"针对固定标识模式；")

    config_collect_receive_pors_section_len = models.CharField(max_length=100, default="", null=True, blank=True,
                                                               verbose_name=u"采集指令-回复指令_采集的参数或者状态_解析的宽度")

    config_collect_receive_pors_section_decodetype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                      verbose_name=u"采集指令-回复指令_采集的参数或者状态_数据解析算法",
                                                                      help_text=definehelptext.config_collect_receive_pors_section_decodetype_help_text)

    config_collect_receive_pors_section_operator = models.CharField(max_length=100, default="*", null=True, blank=True,
                                                                    verbose_name=u"采集指令-回复指令_采集的参数或者状态_操作符",
                                                                    help_text=u"无特殊需求写*即可")
    config_collect_receive_pors_section_operand = models.CharField(max_length=100, default="1", null=True, blank=True,
                                                                   verbose_name=u"采集指令-回复指令_采集的参数或者状态_操作数",
                                                                   help_text=u"无特殊需求写1即可")


    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"采集指令_回复指令中的参数或状态_数据解析配置"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.configcollectreceivepors,self.configcollectreceivepors.config_collect_receive_pors_factorcode,
                                    self.config_collect_receive_pors_section_findmode,
                                    self.config_collect_receive_pors_section_offset,
                                    self.config_collect_receive_pors_section_mark)

class ConfigCollectReceivePorsConvertrule(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)

    configcollectreceiveporssection = models.ForeignKey( ConfigCollectReceivePorsSection,default="", null=True, blank=True,
                                   verbose_name=u"依赖的采集指令之回复指令中的参数或状态之数据解析配置",on_delete=models.PROTECT)

    config_collect_receive_pors_convertrule_ruletype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_特殊规则类型",
                                                        help_text=definehelptext.config_collect_receive_pors_convertrule_ruletype_help_text)

    config_collect_receive_pors_convertrule_enumvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_枚举值",
                                                        help_text=u"多个值之间用分号隔开，如：2;5;78,只针对特殊规则类型为1（即枚举类型），"
                                                                  u"<br/>当取值为枚举值其中之一时，将resultValue的值存起来；")
    config_collect_receive_pors_convertrule_minvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_最小值",
                                                        help_text=u"针对特殊规则类型为2（即小于最小值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"<br/>取值小于最小值时，将resultValue的值存起来；"
                                                                  u"<br/>或者取值在最大值和最小值之间，将resultValue的值存起来；")
    config_collect_receive_pors_convertrule_maxvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_最大值",
                                                        help_text=u"针对特殊规则类型为3（即大于最大值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"<br/>取值大于最大值时，将resultValue的值存起来；"
                                                                  u"<br/>或者取值在最大值和最小值之间，将resultValue的值存起来；")
    config_collect_receive_pors_convertrule_resultvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_最终保存的值",
                                                        help_text=u"与设置的规则和数值相对应的值")


    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"采集指令_回复指令中的参数或状态_数据解析配置_特殊规则"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.config_collect_receive_pors_convertrule_resultvalue

class ConfigControlSendCmd(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)

    config_control_send_id = models.CharField(max_length=100, default="", null=True, blank=True,
                                              verbose_name=u"反控指令-下发指令_下发指令ID",
                                              help_text=definehelptext.config_control_send_id_help_text)

    config_control_send_format = models.CharField(max_length=10,null=True, blank=True,
                                                  choices=(("HEX", "HEX"), ("ASCII", "ASCII")),
                                                  default="HEX",
                                                  verbose_name=u"反控指令-下发指令_下发指令类型",
                                                  help_text=definehelptext.config_control_send_format_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                           verbose_name=u"反控指令-下发指令_下发指令类型",
        #                                           help_text=definehelptext.config_control_send_format_help_text)

    # config_control_send_cmd = models.CharField(max_length=1000, default="", null=True, blank=True,
    #                                            verbose_name=u"反控指令-下发指令_具体下发指令",
    #                                            help_text=definehelptext.config_control_send_cmd_help_text)
    config_control_send_cmd = models.TextField(max_length=1000,default="", null=True, blank=True,
                                               verbose_name=u"反控指令-下发指令_具体下发指令",
                                               help_text=definehelptext.config_control_send_cmd_help_text)

    config_control_send_acktype = models.CharField(max_length=100, default="NO_ACK", null=True, blank=True,
                                                   verbose_name=u"反控指令-下发指令_应答包格式",
                                                   help_text=definehelptext.config_control_send_acktype_help_text)

    config_control_send_ackhead = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"反控指令-下发指令_回复数据的包头",
                                                   help_text=u"支持宏定义，”${}”,</br>"
                                                             u"只有在R_HEAD_TAIL和R_HEAD_LEN这两种报文格式下才有意义，</br>"
                                                             u"其他为空即可。")
    config_control_send_acktail = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"反控指令-下发指令_回复报文的包尾",
                                                   help_text=u"也支持宏定义，</br>"
                                                             u"只有在R_HEAD_TAIL和R_TAIL_ONLY这两种报文格式下才有意义，</br>"
                                                             u"其他为空即可。")
    config_control_send_acklen = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"反控指令-下发指令_回复报文的总长度",
                                                  help_text=u"只有在R_HEAD_LEN和R_LEN_ONLY这两种报文格式下才有意义，</br>"
                                                            u"其他为空即可。")
    config_control_send_ackgap = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"反控指令-下发指令_回复报文的分包间隔",
                                                  help_text=u"一般为空即可")
    config_control_send_ackcheckmode = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"反控指令-下发指令_回复报文的检验",
                                                        help_text=definehelptext.config_control_send_ackcheckmode__help_text)

    config_control_send_ackcheckarg = models.CharField(max_length=100, default="", null=True, blank=True,
                                                       verbose_name=u"反控指令-下发指令_回复报文的固定标识检验参数",
                                                       help_text=u"只有固定标识才有意义，一般为空。")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"反控指令_下发指令"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}".format(self.nodeconfig,self.config_control_send_cmd)

class ConfigControlSendParamid(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    configcontrolsendcmd = models.ForeignKey(ConfigControlSendCmd,default="", null=True, blank=True,
                                   verbose_name=u"依赖的反控下发指令",on_delete=models.PROTECT)

    config_control_send_paramid = models.CharField(max_length=100, default="", null=True, blank=True,
                                                       verbose_name=u"反控指令-下发指令_下发参数名",
                                                       help_text=u"反控指令中的参数适用于平台反控前端仪器时有参数需要下发到前端仪器中，"
                                                                 u"<br/>此时需要将参数处理并加入反控指令中。"
                                                                 u"<br/>paramId='SYSTEMTIME' 参数名，跟上面定义的参数名(即@{}中的参数名)必须一致。")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"反控指令_下发指令_参数"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}".format(self.configcontrolsendcmd,self.config_control_send_paramid)

class ConfigControlSendPorsSection(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    configcontrolsendparamid = models.ForeignKey(ConfigControlSendParamid,default="", null=True, blank=True,
                                   verbose_name=u"依赖的反控下发指令参数",on_delete=models.PROTECT)

    config_control_send_pors_section_datatype = models.CharField(max_length=10,null=True, blank=True,
                                                                 choices=(("FLOAT", "FLOAT"), ("INT", "INT")),
                                                                 default="FLOAT",
                                                                 verbose_name=u"反控指令-下发指令_下发参数_数据类型",
                                                                 help_text=definehelptext.config_control_send_pors_section_datatype_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                          verbose_name=u"反控指令-下发指令_下发参数_数据类型",
        #                                                          help_text=definehelptext.config_control_send_pors_section_datatype_help_text)
    config_control_send_pors_section_strformat = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                  verbose_name=u"反控指令-下发指令_下发参数_数据转换为字符串的格式",
                                                                  help_text= definehelptext.config_collect_receive_pors_section_strformat_help_text)
    config_control_send_pors_section_findmode = models.CharField(max_length=10,null=True, blank=True,
                                                                 choices=(("OFFSET", "OFFSET"), ("MARK", "MARK")),
                                                                 default="OFFSET",
                                                                 verbose_name=u"反控指令-下发指令_下发参数_查找模式",
                                                                 help_text=definehelptext.config_control_send_pors_section_findmode_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                          verbose_name=u"反控指令-下发指令_下发参数_查找模式",
        #                                                          help_text=definehelptext.config_control_send_pors_section_findmode_help_text)
    config_control_send_pors_section_offset = models.CharField(max_length=100, default="", null=True, blank=True,
                                                               verbose_name=u"反控指令-下发指令_下发参数_偏移量",
                                                               help_text=u"相对包头的，只针对固定偏移模式；")

    config_control_send_pors_section_mark = models.CharField(max_length=100, default="", null=True, blank=True,
                                                             verbose_name=u"反控指令-下发指令_下发参数_固定标识",
                                                             help_text=u"针对固定标识模式；")

    config_control_send_pors_section_len = models.CharField(max_length=100, default="", null=True, blank=True,
                                                            verbose_name=u"反控指令-下发指令_下发参数_解析的宽度")

    config_control_send_pors_section_decodetype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                   verbose_name=u"反控指令-下发指令_下发参数_数据解析算法",
                                                                   help_text=definehelptext.config_control_send_pors_section_decodetype_help_text)

    config_control_send_pors_section_operator = models.CharField(max_length=100, default="*", null=True, blank=True,
                                                                 verbose_name=u"反控指令-下发指令_下发参数_操作符",
                                                                 help_text=u"无特殊需求写*即可")
    config_control_send_pors_section_operand = models.CharField(max_length=100, default="1", null=True, blank=True,
                                                                verbose_name=u"反控指令-下发指令_下发参数_操作数",
                                                                help_text=u"无特殊需求写1即可")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"反控指令_下发指令_参数_配置"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.configcontrolsendparamid,self.configcontrolsendparamid.config_control_send_paramid,
                             self.config_control_send_pors_section_findmode,
                             self.config_control_send_pors_section_offset,
                             self.config_control_send_pors_section_mark)

class ConfigControlSendPorsConvertrule(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    configcontrolsendporssection = models.ForeignKey(ConfigControlSendPorsSection,default="", null=True, blank=True,
                                   verbose_name=u"依赖的反控下发指令参数配置",on_delete=models.PROTECT)

    config_control_send_pors_convertrule_ruletype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                     verbose_name=u"反控指令-下发指令_下发参数的状态-特殊转换规则_特殊规则类型",
                                                                     help_text=definehelptext.config_control_send_pors_convertrule_ruletype_help_text)

    config_control_send_pors_convertrule_enumvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"反控指令-下发指令_下发参数的状态-特殊转换规则_枚举值",
                                                        help_text=u"多个值之间用分号隔开，如：2;5;78,只针对特殊规则类型为1（即枚举类型），"
                                                                  u"<br/>当取值为枚举值其中之一时，将resultValue的值存起来；")
    config_control_send_pors_convertrule_minvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"反控指令-下发指令_下发参数的状态-特殊转换规则_最小值",
                                                        help_text=u"针对特殊规则类型为2（即小于最小值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"<br/>取值小于最小值时，将resultValue的之存起来；"
                                                                  u"<br/>或者取值在最大值和最小值之间，将resultValue的值存起来；")
    config_control_send_pors_convertrule_maxvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"反控指令-下发指令_下发参数的状态-特殊转换规则_最大值",
                                                        help_text=u"针对特殊规则类型为3（即大于最大值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"<br/>取值大于最大值时，将resultValue的值存起来；"
                                                                  u"<br/>或者取值在最大值和最小值之间，将resultValue的值存起来；")
    config_control_send_pors_convertrule_resultvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"反控指令-下发指令_下发参数的状态-特殊转换规则_最终保存的值",
                                                        help_text=u"与设置的规则和数值相对应的值")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"反控指令_下发指令_参数_配置_特殊规则"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.config_control_send_pors_convertrule_resultvalue