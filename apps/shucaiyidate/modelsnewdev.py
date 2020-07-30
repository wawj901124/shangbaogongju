from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING,MEDIA_ROOT
from django.contrib.auth import  get_user_model  #导入get_user_model

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
                                     choices=(("HEX", "16进制"), ("ASCII", "字符串")),
                                     default="HEX",
                                     verbose_name=u"协议类型")
    config_version = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"版本号配置（version）",
                                      help_text=u" 每次修改配置都需要更新，一般取配置日期作为版本号,例如：v20180423")
    config_device = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"设备型号配置（deviceModel）",
                                      help_text=u"一般取仪器的名称，例如：雪迪龙U23分析仪")
    config_collect_packet_len = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"采集指令配置_应答包长度配置（ackPacketMaxLen）",
                                      help_text=u"前端仪器回复包的最大长度，如果不写默认1024")

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
                                              verbose_name=u"下发指令ID（id）",
                                              help_text=u"可以为空，起到一个说明作用")

    config_collect_send_format = models.CharField(max_length=10,null=True, blank=True,
                                                  choices=(("HEX", "16进制"), ("ASCII", "字符串")),
                                                  default="HEX",
                                                  verbose_name=u"下发指令的类型（format）",
                                                  help_text=definehelptext.config_collect_send_format_help_text)

    config_collect_send_cmd = models.TextField(max_length=1000, default="", null=True, blank=True,
                                               verbose_name=u"具体下发指令（cmd）",
                                               help_text=definehelptext.config_collect_send_cmd_help_text)

    config_collect_send_acktype = models.CharField(max_length=50,null=True, blank=True,
                                                   choices=(("NO_RULE", "没有规则"), ("HEAD_TAIL", "满足指定包头和包尾"),
                                                            ("HEAD_LEN", "满足指定包头和长度"), ("LEN_ONLY", "满足指定长度"),
                                                            ("TAIL_ONLY", "满足指定包尾"), ("CUSTOM_RULE", "定制规则"),
                                                            ("NO_ACK", "不需要回复"),
                                                            ),
                                                   default="HEAD_LEN",
                                                   verbose_name=u"数据的回复类型（ackType）",
                                                   help_text=definehelptext.config_collect_send_acktype_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                            verbose_name=u"采集指令-下发指令_数据的回复类型",
        #                                            help_text=definehelptext.config_collect_send_acktype_help_text)

    config_collect_send_ackhead = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"回复数据的包头（ackHead）",
                                                   help_text=u"支持宏定义，”${}”,</br>"
                                                             u"只有在R_HEAD_TAIL和R_HEAD_LEN这两种报文格式下才有意义，</br>"
                                                             u"其他为空即可。")
    config_collect_send_acktail = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"回复报文的包尾（ackTail）",
                                                   help_text=u"也支持宏定义，</br>"
                                                             u"只有在R_HEAD_TAIL和R_TAIL_ONLY这两种报文格式下才有意义，</br>"
                                                             u"其他为空即可。")
    config_collect_send_acklen = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"报文的长度（ackLen）",
                                                  help_text=u"只有在R_HEAD_LEN和R_LEN_ONLY这两种报文格式下才有意义，</br>"
                                                            u"其他为空即可。")
    config_collect_send_ackgap = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"回复报文的分包间隔（ackGap）",
                                                  help_text=u"一般为空即可")
    config_collect_send_ackcheckmode = models.CharField(max_length=50,null=True, blank=True,
                                                        choices=(("MODBUS_L_CRC16", "Modbus crc16位校验(低字节在前)"),
                                                                 ("MODBUS_H_CRC16", "Modbus crc16位校验(高字节在前)"),
                                                                 ("FIXED_MARK", "固定标识"),
                                                                 ("HJ212_CRC", "国标CRC校验"),
                                                                 ("HJ212_JG_CRC", "聚光CRC检验")),
                                                        default="MODBUS_L_CRC16",
                                                        verbose_name=u"回复报文的检验（ackCheckMode）",
                                                        help_text=definehelptext.config_collect_send_ackcheckmode_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                 verbose_name=u"回复报文的检验（ackCheckMode）",
        #                                                 help_text=definehelptext.config_collect_send_ackcheckmode_help_text)

    config_collect_send_ackcheckarg = models.CharField(max_length=100, default="", null=True, blank=True,
                                                       verbose_name=u"校验参数（ackCheckArg）",
                                                       help_text=u"只有固定标识才有意义，一般为空。")


    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"下发指令&回复指令配置（cmd）"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}".format(self.nodeconfig,self.config_collect_send_cmd)

    # #model的save函数，关联保存用户
    # def save(self, *args, **kwargs):
    #     self.write_user_id = self.nodeconfig.write_user_id
    #     super().save(*args, **kwargs)

class ConfigCollectFactor(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    configcollectsendcmd = models.ForeignKey(ConfigCollectSendCmd,default="", null=True, blank=True,
                                   verbose_name=u"依赖的采集下发指令",on_delete=models.PROTECT)

    config_collect_factor_factorcode = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"监测因子代码（factorCode）",
                                                        help_text=u"例如：w01018")

    config_collect_factor_findmode = models.CharField(max_length=10,null=True, blank=True,
                                                      choices=(("OFFSET", "固定偏移"), ("MARK", "固定标识")),
                                                      default="OFFSET",
                                                      verbose_name=u"查找模式（findMode）",
                                                      help_text=definehelptext.config_collect_factor_findmode_help_text)


    config_collect_factor_offset = models.CharField(max_length=100, default="", null=True, blank=True,
                                                    verbose_name=u"偏移量（offset）",
                                                    help_text=u"相对包头的，只针对固定偏移模式；</br>例如:</br>收到的数据为：01 02 03 04 05，01 为包头，04 为需要解析的数据，那么 offset 应该为 3 ")

    config_collect_factor_mark = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"固定标识（mark）",
                                                  help_text=u"只针对固定标识模式；")

    config_collect_factor_len = models.CharField(max_length=100, default="", null=True, blank=True,
                                                 verbose_name=u"解析的宽度（len）")

    config_collect_factor_decodetype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"数据解析算法（decodeType）",
                                                        help_text= definehelptext.config_collect_factor_decodetype_help_text)

    config_collect_factor_operator =models.CharField(max_length=10,null=True, blank=True,
                                                     choices=(("+", "+"), ("-", "-"),("*", "*"), ("/", "/")),
                                                     default="*",
                                                     verbose_name=u"操作符（operator）",
                                                     help_text=u"无特殊需求写*即可")
        # models.CharField(max_length=100, default="*", null=True, blank=True,
        #                                               verbose_name=u"采集指令-监测因子_操作符",
        #                                               help_text=u"无特殊需求写*即可")
    config_collect_factor_operand = models.CharField(max_length=100, default="1", null=True, blank=True,
                                                     verbose_name=u"操作数（operand）",
                                                     help_text=u"无特殊需求写1即可")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"监测因子配置（factor）"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.config_collect_factor_factorcode

    # #model的save函数，关联保存用户
    # def save(self, *args, **kwargs):
    #     self.write_user_id = self.nodeconfig.write_user_id
    #     super().save(*args, **kwargs)

class ConfigCollectReceivePors(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    configcollectsendcmd = models.ForeignKey(ConfigCollectSendCmd,default="", null=True, blank=True,
                                   verbose_name=u"依赖的采集下发指令",on_delete=models.PROTECT)

    config_collect_receive_pors_factorcode=models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集的参数或者状态的代码（factorCode）",
                                                        help_text=u"例如：i1210A；"
                                                                  u"<br/>注意：当参数或者状态代码为SampleTime时，为特殊参数或者状态，</br>"
                                                                  u"该参数或者状态代表前端仪器的采样时间，在发送给数据库时该参数或者状态是不发送的，</br>"
                                                                  u"而是在实时数据发送时将该参数的值赋值给采样时间发送。")
    config_collect_receive_pors_factortype= models.CharField(max_length=10,null=True, blank=True,
                                                             choices=(("PARAM", "参数因子"), ("STATE", "状态因子")),
                                                             default="PARAM",
                                                             verbose_name=u"参数或者状态类型（factorType）",
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
        verbose_name = u"参数&状态配置（stateFactor）"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}".format(self.configcollectsendcmd,self.config_collect_receive_pors_factorcode)

    # #model的save函数，关联保存用户
    # def save(self, *args, **kwargs):
    #     self.write_user_id = self.nodeconfig.write_user_id
    #     super().save(*args, **kwargs)

class ConfigCollectReceivePorsSection(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)

    configcollectreceivepors = models.ForeignKey( ConfigCollectReceivePors,default="", null=True, blank=True,
                                   verbose_name=u"依赖的参数&状态配置",on_delete=models.PROTECT)

    config_collect_receive_pors_section_datatype = models.CharField(max_length=10,null=True, blank=True,
                                                                    choices=(("FLOAT", "浮点型"), ("INT", "整型")),
                                                                    default="FLOAT",
                                                                    verbose_name=u"数据类型（dataType）",
                                                                    help_text=definehelptext.config_collect_receive_pors_section_datatype_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                             verbose_name=u"采集指令-回复指令_采集的参数或者状态_数据类型",
        #                                                             help_text=definehelptext.config_collect_receive_pors_section_datatype_help_text)

    config_collect_receive_pors_section_strformat = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                     verbose_name=u"转换为字符串的格式（strFormat）",
                                                                     help_text=definehelptext.config_collect_receive_pors_section_strformat_help_text)
    config_collect_receive_pors_section_findmode = models.CharField(max_length=10,null=True, blank=True,
                                                                    choices=(("OFFSET", "固定偏移"), ("MARK", "固定标识")),
                                                                    default="OFFSET",
                                                                    verbose_name=u"查找模式（findMode）",
                                                                    help_text=definehelptext.config_collect_receive_pors_section_findmode_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                             verbose_name=u"采集指令-回复指令_采集的参数或者状态_查找模式",
        #                                                             help_text=definehelptext.config_collect_receive_pors_section_findmode_help_text)

    config_collect_receive_pors_section_offset = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                  verbose_name=u"偏移量（offset）",
                                                                  help_text=u"相对包头的，只针对固定偏移模式；")

    config_collect_receive_pors_section_mark = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                verbose_name=u"固定标识（mark）",
                                                                help_text=u"只针对固定标识模式；")

    config_collect_receive_pors_section_len = models.CharField(max_length=100, default="", null=True, blank=True,
                                                               verbose_name=u"解析的宽度（len）")

    config_collect_receive_pors_section_decodetype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                      verbose_name=u"数据解析算法（decodeType）",
                                                                      help_text=definehelptext.config_collect_receive_pors_section_decodetype_help_text)

    config_collect_receive_pors_section_operator = models.CharField(max_length=10,null=True, blank=True,
                                                                    choices=(("+", "+"), ("-", "-"),("*", "*"), ("/", "/")),
                                                                    default="*",
                                                                    verbose_name=u"操作符（operator）",
                                                                    help_text=u"无特殊需求写*即可")
        # models.CharField(max_length=100, default="*", null=True, blank=True,
        #                                                             verbose_name=u"采集指令-回复指令_采集的参数或者状态_操作符",
        #                                                             help_text=u"无特殊需求写*即可")
    config_collect_receive_pors_section_operand = models.CharField(max_length=100, default="1", null=True, blank=True,
                                                                   verbose_name=u"操作数（operand）",
                                                                   help_text=u"无特殊需求写1即可")


    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"参数&状态配置之section"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.configcollectreceivepors,self.configcollectreceivepors.config_collect_receive_pors_factorcode,
                                    self.config_collect_receive_pors_section_findmode,
                                    self.config_collect_receive_pors_section_offset,
                                    self.config_collect_receive_pors_section_mark)
    # #model的save函数，关联保存用户
    # def save(self, *args, **kwargs):
    #     self.write_user_id = self.nodeconfig.write_user_id
    #     super().save(*args, **kwargs)

class ConfigCollectReceivePorsConvertrule(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)

    configcollectreceiveporssection = models.ForeignKey( ConfigCollectReceivePorsSection,default="", null=True, blank=True,
                                   verbose_name=u"依赖的参数&状态配置之section",on_delete=models.PROTECT)

    config_collect_receive_pors_convertrule_ruletype = models.CharField(max_length=2,null=True, blank=True,
                                                                        choices=(("1", "枚举类型"),
                                                                                 ("2", "小于最小值"),
                                                                                 ("3", "大于最大值"),
                                                                                 ("4", "最大值最小值之间"),),
                                                                        default="",
                                                                        verbose_name=u"特殊规则类型（ruleType）",
                                                                        help_text=definehelptext.config_collect_receive_pors_convertrule_ruletype_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                 verbose_name=u"特殊规则类型（ruleType）",
        #                                                 help_text=definehelptext.config_collect_receive_pors_convertrule_ruletype_help_text)

    config_collect_receive_pors_convertrule_enumvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"枚举值（enumValue）",
                                                        help_text=u"多个值之间用分号隔开，如：2;5;78,只针对特殊规则类型为1（即枚举类型），"
                                                                  u"<br/>当取值为枚举值其中之一时，将resultValue的值存起来；")
    config_collect_receive_pors_convertrule_minvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"最小值（minValue）",
                                                        help_text=u"针对特殊规则类型为2（即小于最小值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"<br/>取值小于最小值时，将resultValue的值存起来；"
                                                                  u"<br/>或者取值在最大值和最小值之间，将resultValue的值存起来；")
    config_collect_receive_pors_convertrule_maxvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"最大值（maxValue）",
                                                        help_text=u"针对特殊规则类型为3（即大于最大值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"<br/>取值大于最大值时，将resultValue的值存起来；"
                                                                  u"<br/>或者取值在最大值和最小值之间，将resultValue的值存起来；")
    config_collect_receive_pors_convertrule_resultvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"最终保存的值（resultValue）",
                                                        help_text=u"与设置的规则和数值相对应的值")


    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"特殊转换规则（convertRule） "
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.config_collect_receive_pors_convertrule_resultvalue

    # #model的save函数，关联保存用户
    # def save(self, *args, **kwargs):
    #     self.write_user_id = self.nodeconfig.write_user_id
    #     super().save(*args, **kwargs)

class ConfigControlSendCmd(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)

    config_control_send_id = models.CharField(max_length=50,null=True, blank=True,
                                              choices=(('zeroAndFull', '校零校满'), ('adjustTime', '校时'), ('immediateSample', '及时采样'), ('remoteQualityCtrl', '远程质控'), ('startTest', '仪器启动测试'), ('stopTest', '仪器停止测试'), ('autoCorrection', '仪器自动校准'), ('init', '仪器初始化'), ('checkStdSample', '仪器进行标样核查'), ('setMeasureMode', '仪器修改测量模式'), ('setMeasureInterval', '仪器修改周期测量间隔'), ('setAutoCorrectInterval', '仪器修改自动校准间隔'), ('setCheckStdSampleInterval', '仪器修改自动标样核查间隔'), ('setOneLevelPasswd', '修改一级密码'), ('setTwoLevelPasswd', '修改二级密码'), ('setThreeLevelPasswd', '修改三级密码'), ('zeroCorrectRange', '零点校准量程校准'), ('startClean', '启动清洗/反吹'), ('compareSample', '比对采样'), ('overproofSample', '超标留样'), ('setSampleCycle', '设置采样时间周期'), ('getSampleCycle', '提取采样时间周期'), ('getLastSampleTime', '提取出样时间'), ('getEquipmentId', '提取设备唯一标识'), ('getEquipmentTime', '提取现场机时间'), ('setEquipmentTime', '设置现场机时间'), ('setEquipmentParam', '设置现场机参数')),
                                              default="zeroAndFull",
                                              verbose_name=u"反控指令的 ID（id）",
                                              help_text=definehelptext.config_control_send_id_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                       verbose_name=u"反控指令-下发指令_下发指令ID",
        #                                       help_text=definehelptext.config_control_send_id_help_text)

    config_control_send_format = models.CharField(max_length=10,null=True, blank=True,
                                                  choices=(("HEX", "16进制"), ("ASCII", "字符串")),
                                                  default="HEX",
                                                  verbose_name=u"命令类型（format）",
                                                  help_text=definehelptext.config_control_send_format_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                           verbose_name=u"反控指令-下发指令_下发指令类型",
        #                                           help_text=definehelptext.config_control_send_format_help_text)

    # config_control_send_cmd = models.CharField(max_length=1000, default="", null=True, blank=True,
    #                                            verbose_name=u"反控指令-下发指令_具体下发指令",
    #                                            help_text=definehelptext.config_control_send_cmd_help_text)
    config_control_send_cmd = models.TextField(max_length=1000,default="", null=True, blank=True,
                                               verbose_name=u"反控指令的配置（cmd）",
                                               help_text=definehelptext.config_control_send_cmd_help_text)

    config_control_send_acktype = models.CharField(max_length=50,null=True, blank=True,
                                                   choices=(("NO_RULE", "没有规则"), ("HEAD_TAIL", "满足指定包头和包尾"),
                                                            ("HEAD_LEN", "满足指定包头和长度"), ("LEN_ONLY", "满足指定长度"),
                                                            ("TAIL_ONLY", "满足指定包尾"), ("CUSTOM_RULE", "定制规则"),
                                                            ("NO_ACK", "不需要回复"),
                                                            ),
                                                   default="NO_ACK",
                                                   verbose_name=u"应答包格式（ackType）",
                                                   help_text=definehelptext.config_control_send_acktype_help_text)
        # models.CharField(max_length=100, default="NO_ACK", null=True, blank=True,
        #                                            verbose_name=u"反控指令-下发指令_应答包格式",
        #                                            help_text=definehelptext.config_control_send_acktype_help_text)

    config_control_send_ackhead = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"回复数据的包头（ackHead）",
                                                   help_text=u"支持宏定义，”${}”,</br>"
                                                             u"只有在R_HEAD_TAIL和R_HEAD_LEN这两种报文格式下才有意义，</br>"
                                                             u"其他为空即可。")
    config_control_send_acktail = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"回复报文的包尾（ackTail）",
                                                   help_text=u"也支持宏定义，</br>"
                                                             u"只有在R_HEAD_TAIL和R_TAIL_ONLY这两种报文格式下才有意义，</br>"
                                                             u"其他为空即可。")
    config_control_send_acklen = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"回复报文的总长度（ackLen）",
                                                  help_text=u"只有在R_HEAD_LEN和R_LEN_ONLY这两种报文格式下才有意义，</br>"
                                                            u"其他为空即可。")
    config_control_send_ackgap = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"回复报文的分包间隔（ackGap）",
                                                  help_text=u"一般为空即可")
    config_control_send_ackcheckmode = models.CharField(max_length=50,null=True, blank=True,
                                                        choices=(("MODBUS_L_CRC16", "Modbus crc16位校验(低字节在前)"),
                                                                 ("MODBUS_H_CRC16", "Modbus crc16位校验(高字节在前)"),
                                                                 ("FIXED_MARK", "固定标识"),
                                                                 ("HJ212_CRC", "国标CRC校验"),
                                                                 ("HJ212_JG_CRC", "聚光CRC检验")),
                                                        default="",
                                                        verbose_name=u"回复报文的检验（ackCheckMode）",
                                                        help_text=definehelptext.config_control_send_ackcheckmode__help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                 verbose_name=u"回复报文的检验（ackCheckMode）",
        #                                                 help_text=definehelptext.config_control_send_ackcheckmode__help_text)

    config_control_send_ackcheckarg = models.CharField(max_length=100, default="", null=True, blank=True,
                                                       verbose_name=u"检验参数（ackCheckArg）",
                                                       help_text=u"只有固定标识才有意义，一般为空。")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"反控指令配置（cmd） "
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}".format(self.nodeconfig,self.get_config_control_send_id_display())

    # #model的save函数，关联保存用户
    # def save(self, *args, **kwargs):
    #     self.write_user_id = self.nodeconfig.write_user_id
    #     super().save(*args, **kwargs)

class ConfigControlSendParamid(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    configcontrolsendcmd = models.ForeignKey(ConfigControlSendCmd,default="", null=True, blank=True,
                                   verbose_name=u"依赖的反控下发指令",on_delete=models.PROTECT)

    config_control_send_paramid = models.CharField(max_length=100, default="", null=True, blank=True,
                                                       verbose_name=u"参数名（paramId）",
                                                       help_text=u"反控指令中的参数适用于平台反控前端仪器时有参数需要下发到前端仪器中，"
                                                                 u"<br/>此时需要将参数处理并加入反控指令中。"
                                                                 u"<br/>paramId='SYSTEMTIME' 参数名，跟上面定义的参数名(即@{}中的参数名)必须一致。")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"反控指令_参数"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}".format(self.configcontrolsendcmd,self.config_control_send_paramid)

    # #model的save函数，关联保存用户
    # def save(self, *args, **kwargs):
    #     self.write_user_id = self.nodeconfig.write_user_id
    #     super().save(*args, **kwargs)

class ConfigControlSendPorsSection(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    configcontrolsendparamid = models.ForeignKey(ConfigControlSendParamid,default="", null=True, blank=True,
                                   verbose_name=u"依赖的反控指令_参数",on_delete=models.PROTECT)

    config_control_send_pors_section_datatype = models.CharField(max_length=10,null=True, blank=True,
                                                                 choices=(("FLOAT", "浮点型"), ("INT", "整型")),
                                                                 default="FLOAT",
                                                                 verbose_name=u"数据类型（dataType）",
                                                                 help_text=definehelptext.config_control_send_pors_section_datatype_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                          verbose_name=u"反控指令-下发指令_下发参数_数据类型",
        #                                                          help_text=definehelptext.config_control_send_pors_section_datatype_help_text)
    config_control_send_pors_section_strformat = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                  verbose_name=u"数据转换为字符串的格式（strFormat）",
                                                                  help_text= definehelptext.config_collect_receive_pors_section_strformat_help_text)
    config_control_send_pors_section_findmode = models.CharField(max_length=10,null=True, blank=True,
                                                                 choices=(("OFFSET", "固定偏移"), ("MARK", "固定标识")),
                                                                 default="OFFSET",
                                                                 verbose_name=u"查找模式（findMode）",
                                                                 help_text=definehelptext.config_control_send_pors_section_findmode_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                          verbose_name=u"反控指令-下发指令_下发参数_查找模式",
        #                                                          help_text=definehelptext.config_control_send_pors_section_findmode_help_text)
    config_control_send_pors_section_offset = models.CharField(max_length=100, default="", null=True, blank=True,
                                                               verbose_name=u"偏移量（offset）",
                                                               help_text=u"相对包头的，只针对固定偏移模式；")

    config_control_send_pors_section_mark = models.CharField(max_length=100, default="", null=True, blank=True,
                                                             verbose_name=u"固定标识（mark）",
                                                             help_text=u"只针对固定标识模式；")

    config_control_send_pors_section_len = models.CharField(max_length=100, default="", null=True, blank=True,
                                                            verbose_name=u"解析的宽度（len）")

    config_control_send_pors_section_decodetype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                   verbose_name=u"数据解析算法（decodeType）",
                                                                   help_text=definehelptext.config_control_send_pors_section_decodetype_help_text)

    config_control_send_pors_section_operator = models.CharField(max_length=10,null=True, blank=True,
                                                                 choices=(("+", "+"), ("-", "-"),("*", "*"), ("/", "/")),
                                                                 default="*",
                                                                 verbose_name=u"操作符（operator）",
                                                                 help_text=u"无特殊需求写*即可")
        # models.CharField(max_length=100, default="*", null=True, blank=True,
        #                                                          verbose_name=u"反控指令-下发指令_下发参数_操作符",
        #                                                          help_text=u"无特殊需求写*即可")
    config_control_send_pors_section_operand = models.CharField(max_length=100, default="1", null=True, blank=True,
                                                                verbose_name=u"操作数（operand）",
                                                                help_text=u"无特殊需求写1即可")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"反控指令_参数的处理（section）"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.configcontrolsendparamid,self.configcontrolsendparamid.config_control_send_paramid,
                             self.config_control_send_pors_section_findmode,
                             self.config_control_send_pors_section_offset,
                             self.config_control_send_pors_section_mark)
    # #model的save函数，关联保存用户
    # def save(self, *args, **kwargs):
    #     self.write_user_id = self.nodeconfig.write_user_id
    #     super().save(*args, **kwargs)

class ConfigControlSendPorsConvertrule(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    configcontrolsendporssection = models.ForeignKey(ConfigControlSendPorsSection,default="", null=True, blank=True,
                                   verbose_name=u"依赖的反控指令_参数的处理（section）",on_delete=models.PROTECT)

    config_control_send_pors_convertrule_ruletype = models.CharField(max_length=2,null=True, blank=True,
                                                                     choices=(("1", "枚举类型"),
                                                                              ("2", "小于最小值"),
                                                                              ("3", "大于最大值"),
                                                                              ("4", "最大值最小值之间"),),
                                                                     default="",
                                                                     verbose_name=u"特殊规则类型（ruleType）",
                                                                     help_text=definehelptext.config_control_send_pors_convertrule_ruletype_help_text)
        # models.CharField(max_length=100, default="", null=True, blank=True,
        #                                                              verbose_name=u"特殊规则类型（ruleType）",
        #                                                              help_text=definehelptext.config_control_send_pors_convertrule_ruletype_help_text)

    config_control_send_pors_convertrule_enumvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"枚举值（enumValue）",
                                                        help_text=u"多个值之间用分号隔开，如：2;5;78,只针对特殊规则类型为1（即枚举类型），"
                                                                  u"<br/>当取值为枚举值其中之一时，将resultValue的值存起来；")
    config_control_send_pors_convertrule_minvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"最小值（minValue）",
                                                        help_text=u"针对特殊规则类型为2（即小于最小值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"<br/>取值小于最小值时，将resultValue的之存起来；"
                                                                  u"<br/>或者取值在最大值和最小值之间，将resultValue的值存起来；")
    config_control_send_pors_convertrule_maxvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"最大值（maxValue）",
                                                        help_text=u"针对特殊规则类型为3（即大于最大值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"<br/>取值大于最大值时，将resultValue的值存起来；"
                                                                  u"<br/>或者取值在最大值和最小值之间，将resultValue的值存起来；")
    config_control_send_pors_convertrule_resultvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"最终保存的值（resultValue）",
                                                        help_text=u"与设置的规则和数值相对应的值")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)

    # user_name = models.ManyToManyField(User, verbose_name=u"名称")  #满足同一功能谋一跳数据可以多个用户访问和操作

    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间



    class ConfigControlSendPorsConvertruleXadmin(object):

        ## 需要重写instance_forms方法，此方法作用是生成表单实例
        def instance_forms(self):
            super().instance_forms()
            # 判断是否为新建操作，新建操作才会设置write_user的默认值
            if not self.org_obj:
                self.form_obj.initial['write_user'] = self.request.user.id


    class Meta:
        verbose_name = u"反控指令_参数的处理（convertRule）"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.config_control_send_pors_convertrule_resultvalue

    #model的save函数，关联保存用户
    def save(self, *args, **kwargs):
        self.write_user_id = self.nodeconfig.write_user_id
        super().save(*args, **kwargs)





