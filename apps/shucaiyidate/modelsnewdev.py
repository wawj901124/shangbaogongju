from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING,MEDIA_ROOT
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

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
    config_version = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"版本号",
                                      help_text=u" 版本号配置，每次修改配置都需要更新，一般取配置日期作为版本号,例如：v20180423")
    config_device = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"设备名称",
                                      help_text=u"设备名称，一般取仪器的名称，例如：雪迪龙U23分析仪")
    config_collect_packet_len = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"采集指令_应答包最大长度",
                                      help_text=u"采集指令_应答包长度配置，前端仪器回复包的最大长度，如果不写默认1024")

    local_file = models.FileField(upload_to=upload_local_file_path,  blank=True, null=True,verbose_name="上传的原dev文件")
    dev_file = models.FileField(upload_to=upload_dev_file_path,  blank=True, null=True,verbose_name="生成的dev文件")

    # tag_father = models.ForeignKey('self', null=True, blank=True, verbose_name=u"依赖的父节点", on_delete=models.PROTECT)

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

    # def node_first_attrib(self):   #定义点击后跳转到某一个地方（可以加html代码）
    #     from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     html_all = ""
    #     node_attrib_all = self.tagattrib_set.all().order_by('id')
    #
    #     for node_attrib_one in node_attrib_all:
    #         html_one = "<span>{}：{}</span></br>".format(node_attrib_one.tag_value_name,node_attrib_one.tag_value_text)
    #         html_all = "%s%s" % (html_all, html_one)
    #         # break   #循环一次
    #     return mark_safe(html_all)
    #
    # node_first_attrib.short_description = u"节点属性及其值"  # 为go_to函数名个名字


class ConfigCollectSendCmd(models.Model):
    nodeconfig = models.ForeignKey(NodeConfig,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点配置",on_delete=models.PROTECT)
    config_collect_send_id = models.CharField(max_length=100, default="rtdCollect", null=True, blank=True,
                                              verbose_name=u"采集指令-下发指令_下发指令ID",
                                              help_text=u"采集指令-下发指令_下发指令ID，下发指令ID，可以为空，起到一个说明作用")

    config_collect_send_format = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"采集指令-下发指令_下发指令类型",
                                                  help_text=u"采集指令-下发指令_下发指令类型，下发指令的类型有:"
                                                            u"HEX(十六进制格式)：报文以HEX的形式发送；"
                                                            u"ASCII（字符串格式）：报文以ASCII的形式发送。")

    config_collect_send_cmd = models.CharField(max_length=1000, default="", null=True, blank=True,
                                               verbose_name=u"具体下发指令",
                                               help_text=u"采集指令-下发指令_具体下发指令，"
                                                         u"例如：\"${ID}0375320002${MODBUS_L_CRC16}\"  具体下发指令，中间部分指令内容0375320002根据需求"
                                                         u"确定,各自意思："
                                                         u"${ID}:用宏表示设备ID，表示ID可以再别处配置；"
                                                         u"03：表示功能码，和需求说明的功能码一致；"
                                                         u"7532：表示寄存器起始地址，和需求说明的寄存器起始地址一致；"
                                                         u"0002:表示寄存器个数，和需求说明的寄存器个数一致；"
                                                         u"${MODBUS_L_CRC16}:表示下发指令的CRC校验方式，有四种："
                                                         u"${MODBUS_L_CRC16}：Modbus crc16位校验，低字节在前，用校验结果替换宏；"
                                                         u"${MODBUS_H_CRC16}：Modbus crc16位校验，高字节在前，用校验结果替换宏；"
                                                         u"${HJ212_CRC}：HJ212国标校验，用校验结果替换宏；"
                                                         u"${HJ212_JG_CRC}：聚光校验，用校验结果替换宏；"
                                                         u"一般多用${MODBUS_L_CRC16}，具体用哪一种需要根据需求来定；"
                                                         u"注意：如有新的规则或者校验算法可在动态管控仪的算法库中实现相应的宏。"
                                                         u"下发指令可以附带宏，其中”${}”为一项宏，会用到的宏还有："
                                                         u"${CR}：回车，会在指令会用’\r’替换该宏；"
                                                         u"${LF}：换行，会在指令会用’\n’替换该宏。")
    config_collect_send_acktype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"采集指令-下发指令_数据的回复类型",
                                                   help_text=u"采集指令-下发指令_数据的回复类型，根据下发指令格式确定报文的类型,值有："
                                                             u"R_NO_RULE：没有规则：取走buffer中已存在的所有数据；"
                                                             u"R_HEAD_TAIL：满足指定包头和包尾的数据帧；"
                                                             u"R_HEAD_LEN：满足指定包头和长度的数据帧；"
                                                             u"R_LEN_ONLY：满足指定长度的数据帧；"
                                                             u"R_TAIL_ONLY：满足指定包尾的数据帧；"
                                                             u"R_CUSTOM_RULE：定制规则，由上层定义匹配函数matchFunc；"
                                                             u"NO_ACK：不需要回复，该规则下，不处理串口数据，一般用在反控中；"
                                                             u"R_NO_RULE使用时长去掉R，例如用R_NO_RULE，则可以填写为R_NO_RULE。")
    config_collect_send_ackhead = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"采集指令-下发指令_回复数据的包头",
                                                   help_text=u"采集指令-下发指令_回复数据的包头，支持宏定义，”${}”,"
                                                             u"只有在R_HEAD_TAIL和R_HEAD_LEN这两种报文格式下才有意义，其他为空即可。")
    config_collect_send_acktail = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"采集指令-下发指令_回复报文的包尾",
                                                   help_text=u"采集指令-下发指令_回复报文的包尾，也支持宏定义，"
                                                             u"只有在R_HEAD_TAIL和R_TAIL_ONLY这两种报文格式下才有意义，其他为空即可。")
    config_collect_send_acklen = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"采集指令-下发指令_回复报文的总长度",
                                                  help_text=u"采集指令-下发指令_回复报文的总长度，"
                                                            u"只有在R_HEAD_LEN和R_LEN_ONLY这两种报文格式下才有意义，其他为空即可。")
    config_collect_send_ackgap = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"采集指令-下发指令_回复报文的分包间隔",
                                                  help_text=u"采集指令-下发指令_回复报文的分包间隔，一般为空即可")
    config_collect_send_ackcheckmode = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-下发指令_回复报文的检验",
                                                        help_text=u"采集指令-下发指令_回复报文的检验，用来判断报文的正确性,有："
                                                                  u"MODBUS_L_CRC16：Modbus crc16位校验，低字节在前；"
                                                                  u"MODBUS_H_CRC16：Modbus crc16位校验，高字节在前；"
                                                                  u"FIXED_MARK：固定标识，会在报文中查找固定的标识，固定标识配置在校验参数中；"
                                                                  u"HJ212_CRC：国标CRC校验；"
                                                                  u"HJ212_JG_CRC：聚光CRC检验；")
    config_collect_send_ackcheckarg = models.CharField(max_length=100, default="", null=True, blank=True,
                                                       verbose_name=u"采集指令-下发指令_回复报文的固定标识检验参数",
                                                       help_text=u"采集指令-下发指令_回复报文的固定标识检验参数，只有固定标识才有意义，一般为空。")


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
                                                        help_text=u"采集指令-下发指令_监测因子代码，例如：w01018")

    config_collect_factor_findmode = models.CharField(max_length=100, default="", null=True, blank=True,
                                                      verbose_name=u"采集指令-监测因子_查找模式",
                                                      help_text=u"采集指令-下发指令_查找模式，有："
                                                                u"OFFSET（固定偏移）：相对包头的偏移量；"
                                                                u"MARK（固定标识）：所有的固定标识不能有包含与被包含的关系，否则没法解析；")

    config_collect_factor_offset = models.CharField(max_length=100, default="", null=True, blank=True,
                                                    verbose_name=u"采集指令-监测因子_偏移量",
                                                    help_text=u"采集指令-监测因子_偏移量，相对包头的，只针对固定偏移模式；")

    config_collect_factor_mark = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"采集指令-监测因子_固定标识",
                                                  help_text=u"采集指令-监测因子_固定标识，针对固定标识模式；")

    config_collect_factor_len = models.CharField(max_length=100, default="", null=True, blank=True,
                                                 verbose_name=u"采集指令-监测因子_解析的宽度",
                                                 help_text=u"采集指令-监测因子_解析的宽度；")

    config_collect_factor_decodetype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-监测因子_数据解析算法",
                                                        help_text=u"采集指令-监测因子_数据解析算法，与解析宽度配合使用，有："
                                                                  u"decode1：将IEEE745格式的四字节数据(小端)转换成一个float型数值4321，例如：4855D04545D05548->6666.66；"
                                                                  u"decode2：将IEEE745格式的四字节数据(大端)转换成一个float型数值1234，例如：45D0554845D05548->6666.66；"
                                                                  u"decode3：将IEEE745格式的四字节数据(小端)转换成一个float型数值2143，例如：D045485545D05548->6666.66；"
                                                                  u"decode4：将IEEE745格式的四字节数据(大端)转换成一个float型数值3412，例如：554845D045D05548->6666.66；"
                                                                  u"decode5：字符串转换成浮点数，例如：“12345.3” 12345.3；"
                                                                  u"decode6：字符串转换成整形，转换宽度由上面len（即解析的宽度）决定；"
                                                                  u"decode7：字符数组转换成短整型，例如：十六进制short；，解析时间一般都用这个算法；"
                                                                  u"decode8：将一个字符的十六进制直接转换成对应的十进制，例如：0x0a10；"
                                                                  u"decode9@bit3：取对应字节的比特位，返回0或者1，例如：0x041；0x030；"
                                                                  u"decode10@1234：将十六进制字符串直接转换成4字节浮点数（可配置顺序），例如：3F9DF3B63F9DF3B6->1.234；"
                                                                  u"decode11@12：将十六进制字符串直接转换成2字节短整型（可配置顺序），例如：12351235->4661；"
                                                                  u"decode12@4312：将IEEF745格式的4字节数据转成一个float型数值（可配置顺序），例如：40009a44449A4000->1234.0；"
                                                                  u"decode13@u 字节序 或 decode13@s 字节序：16 进制字节数组转化为 4 字节整型数据 （u 代表无符号数，s 代表有符号数"
                                                                  u"；注：配置时必须指明符号类型，如果不明确是什么符号类型，请使用 s），例如："
                                                                  u"例 1： 规则：decode13@u1234 ，源字节数组（HEX）：45 1C 30 2F ，解析结果：1159475247（即45 1C 30 2F451C302F->1159475247）；"
                                                                  u"例 2： 规则：decode13@s3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果:-245 （即ff 0b ff ffFFFFFF0B->-245）；"
                                                                  u"例 3： 规则：decode13@u3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果: 4294967051（即ff 0b ff ffFFFFFF0B->4294967051；"
                                                                  u"注：对比例 2 和例 3 可观察有符号和无符号的解析差别；"
                                                                  u"decode14@u 字节序 或 decode14@s 字节序：16 进制字节数组转化为 4 字节整型数据 （u 代表无符号数，s 代表有符号数"
                                                                  u"；注：配置时必须指明符号类型，如果不明确是什么符号类型，请使用 s），例如："
                                                                  u"例 1： 规则：decode13@u1234 ，源字节数组（HEX）：45 1C 30 2F ，解析结果：1159475247（即45 1C 30 2F451C302F->1159475247）；"
                                                                  u"例 2： 规则：decode13@s3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果:-245 （即ff 0b ff ffFFFFFF0B->-245）；"
                                                                  u"例 3： 规则：decode13@u3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果: 4294967051（即ff 0b ff ffFFFFFF0B->4294967051）；"
                                                                  u"注：对比例 2 和例 3 可观察有符号和无符号的解析差别；"
                                                                  u"decode13和decode14的算法规则一样；"
                                                                  u"decode15@字节序：16 进制字节数组转化为 8 字节有符号浮点数，"
                                                                  u"例 1： 规则：decode15@12345678 ，源字节数组（HEX）： 40aa4875c28f5c29 ，解析结果：3364.23（即40aa4875c28f5c2940AA4875C28F5C29->3364.23）；"
                                                                  u"decode16：16 进制字节数组转化为 16 进制字符串对应的浮点数，"
                                                                  u"例 1： 规则：decode16 ，源字节数组（HEX）： 12 34 56 78 ，解析结果：12345678.0（即12 34 56 7812345678.0）；"
                                                                  u"注意：改算法由算法库提供当有不满足时可适当进行扩展。")

    config_collect_factor_operator = models.CharField(max_length=100, default="*", null=True, blank=True,
                                                      verbose_name=u"采集指令-监测因子_操作符",
                                                      help_text=u"采集指令-监测因子_操作符，无特殊需求写*即可")
    config_collect_factor_operand = models.CharField(max_length=100, default="1", null=True, blank=True,
                                                     verbose_name=u"采集指令-监测因子_操作数",
                                                     help_text=u"采集指令-监测因子_操作数，无特殊需求写1即可")

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
                                                        help_text=u"采集指令-监测因子_采集的参数或者状态的代码，例如：i1210A；"
                                                                  u"注意：当参数或者状态代码为SampleTime时，为特殊参数或者状态，"
                                                                  u"该参数或者状态代表前端仪器的采样时间，在发送给数据库时该参数或者状态是不发送的，"
                                                                  u"而是在实时数据发送时将该参数的值赋值给采样时间发送。")
    config_collect_receive_pors_factortype=models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态的类型",
                                                        help_text=u"采集指令-监测因子_采集的参数或者状态的类型，有："
                                                                  u"STATE：状态；"
                                                                  u"PARAM:参数。")
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

    config_collect_receive_pors_section_datatype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                    verbose_name=u"采集指令-回复指令_采集的参数或者状态_数据类型",
                                                                    help_text=u"采集指令-回复指令_采集的参数或者状态_数据类型，不写默认为INT,有："
                                                                              u"INT：将解析到的值以整形的形式存储成字符串；"
                                                                              u"FLOAT:将解析到的值以浮点数的形式存储成字符串。")
    config_collect_receive_pors_section_strformat = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                     verbose_name=u"采集指令-回复指令_采集的参数或者状态_数据转换为字符串的格式",
                                                                     help_text=u"采集指令-回复指令_采集的参数或者状态_数据转换为字符串的格式，"
                                                                               u"符合printf函数格式化规则,为空时默认为'%d'或'%f',"
                                                                               u"具体根据dataType（数据类型）决定，"
                                                                               u"数据类型为INT时，则为'%d'；"
                                                                               u"数据类型为FLOAT时，则为'%f'。")
    config_collect_receive_pors_section_findmode = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                    verbose_name=u"采集指令-回复指令_采集的参数或者状态_查找模式",
                                                                    help_text=u"采集指令-回复指令_采集的参数或者状态_查找模式，有："
                                                                              u"OFFSET（固定偏移）：相对包头的偏移量；"
                                                                              u"MARK（固定标识）：所有的固定标识，不能有包含与被包含的关系，否则没法解析")
    config_collect_receive_pors_section_offset = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                  verbose_name=u"采集指令-回复指令_采集的参数或者状态_偏移量",
                                                                  help_text=u"采集指令-回复指令_采集的参数或者状态_偏移量，相对包头的，只针对固定偏移模式；")

    config_collect_receive_pors_section_mark = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                verbose_name=u"采集指令-回复指令_采集的参数或者状态_固定标识",
                                                                help_text=u"采集指令-回复指令_采集的参数或者状态_固定标识，针对固定标识模式；")

    config_collect_receive_pors_section_len = models.CharField(max_length=100, default="", null=True, blank=True,
                                                               verbose_name=u"采集指令-回复指令_采集的参数或者状态_解析的宽度",
                                                               help_text=u"采集指令-回复指令_采集的参数或者状态_解析的宽度；")

    config_collect_receive_pors_section_decodetype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                      verbose_name=u"采集指令-回复指令_采集的参数或者状态_数据解析算法",
                                                                      help_text=u"采集指令-回复指令_采集的参数或者状态_数据解析算法，与解析宽度配合使用，有："
                                                                                u"decode1：将IEEE745格式的四字节数据(小端)转换成一个float型数值4321，例如：4855D04545D05548->6666.66；"
                                                                                u"decode2：将IEEE745格式的四字节数据(大端)转换成一个float型数值1234，例如：45D0554845D05548->6666.66；"
                                                                                u"decode3：将IEEE745格式的四字节数据(小端)转换成一个float型数值2143，例如：D045485545D05548->6666.66；"
                                                                                u"decode4：将IEEE745格式的四字节数据(大端)转换成一个float型数值3412，例如：554845D045D05548->6666.66；"
                                                                                u"decode5：字符串转换成浮点数，例如：“12345.3” 12345.3；"
                                                                                u"decode6：字符串转换成整形，转换宽度由上面len（即解析的宽度）决定；"
                                                                                u"decode7：字符数组转换成短整型，例如：十六进制short；，解析时间一般都用这个算法；"
                                                                                u"decode8：将一个字符的十六进制直接转换成对应的十进制，例如：0x0a10；"
                                                                                u"decode9@bit3：取对应字节的比特位，返回0或者1，例如：0x041；0x030；"
                                                                                u"decode10@1234：将十六进制字符串直接转换成4字节浮点数（可配置顺序），例如：3F9DF3B63F9DF3B6->1.234；"
                                                                                u"decode11@12：将十六进制字符串直接转换成2字节短整型（可配置顺序），例如：12351235->4661；"
                                                                                u"decode12@4312：将IEEF745格式的4字节数据转成一个float型数值（可配置顺序），例如：40009a44449A4000->1234.0；"
                                                                                u"decode13@u 字节序 或 decode13@s 字节序：16 进制字节数组转化为 4 字节整型数据 （u 代表无符号数，s 代表有符号数"
                                                                                u"；注：配置时必须指明符号类型，如果不明确是什么符号类型，请使用 s），例如："
                                                                                u"例 1： 规则：decode13@u1234 ，源字节数组（HEX）：45 1C 30 2F ，解析结果：1159475247（即45 1C 30 2F451C302F->1159475247）；"
                                                                                u"例 2： 规则：decode13@s3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果:-245 （即ff 0b ff ffFFFFFF0B->-245）；"
                                                                                u"例 3： 规则：decode13@u3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果: 4294967051（即ff 0b ff ffFFFFFF0B->4294967051；"
                                                                                u"注：对比例 2 和例 3 可观察有符号和无符号的解析差别；"
                                                                                u"decode14@u 字节序 或 decode14@s 字节序：16 进制字节数组转化为 4 字节整型数据 （u 代表无符号数，s 代表有符号数"
                                                                                u"；注：配置时必须指明符号类型，如果不明确是什么符号类型，请使用 s），例如："
                                                                                u"例 1： 规则：decode13@u1234 ，源字节数组（HEX）：45 1C 30 2F ，解析结果：1159475247（即45 1C 30 2F451C302F->1159475247）；"
                                                                                u"例 2： 规则：decode13@s3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果:-245 （即ff 0b ff ffFFFFFF0B->-245）；"
                                                                                u"例 3： 规则：decode13@u3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果: 4294967051（即ff 0b ff ffFFFFFF0B->4294967051）；"
                                                                                u"注：对比例 2 和例 3 可观察有符号和无符号的解析差别；"
                                                                                u"decode13和decode14的算法规则一样；"
                                                                                u"decode15@字节序：16 进制字节数组转化为 8 字节有符号浮点数，"
                                                                                u"例 1： 规则：decode15@12345678 ，源字节数组（HEX）： 40aa4875c28f5c29 ，解析结果：3364.23（即40aa4875c28f5c2940AA4875C28F5C29->3364.23）；"
                                                                                u"decode16：16 进制字节数组转化为 16 进制字符串对应的浮点数，"
                                                                                u"例 1： 规则：decode16 ，源字节数组（HEX）： 12 34 56 78 ，解析结果：12345678.0（即12 34 56 7812345678.0）；"
                                                                                u"注意：改算法由算法库提供当有不满足时可适当进行扩展。")

    config_collect_receive_pors_section_operator = models.CharField(max_length=100, default="*", null=True, blank=True,
                                                                    verbose_name=u"采集指令-回复指令_采集的参数或者状态_操作符",
                                                                    help_text=u"采集指令-回复指令_采集的参数或者状态_操作符，无特殊需求写*即可")
    config_collect_receive_pors_section_operand = models.CharField(max_length=100, default="1", null=True, blank=True,
                                                                   verbose_name=u"采集指令-回复指令_采集的参数或者状态_操作数",
                                                                   help_text=u"采集指令-回复指令_采集的参数或者状态_操作数，无特殊需求写1即可")


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
                                                        help_text=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_特殊规则类型，有："
                                                                  u"1：枚举类型；"
                                                                  u"2：小于最小值；"
                                                                  u"3：大于最大值；"
                                                                  u"4：最大值最小值之间；"
                                                                  u"注意：当配置多个特殊转换规则时，只要有满足的规则，之后的规则将不再判断，无特殊配置直接去掉convertRule节点。")
    config_collect_receive_pors_convertrule_enumvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_枚举值",
                                                        help_text=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_枚举值，"
                                                                  u"多个值之间用分号隔开，如：2;5;78,只针对特殊规则类型为1（即枚举类型），"
                                                                  u"当取值为枚举值其中之一时，将resultValue的之存起来；")
    config_collect_receive_pors_convertrule_minvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_最小值",
                                                        help_text=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_最小值，"
                                                                  u"针对特殊规则类型为2（即小于最小值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"取值小于最小值时，将resultValue的之存起来；"
                                                                  u"或者取值在最大值和最小值之间，将resultValue的之存起来；")
    config_collect_receive_pors_convertrule_maxvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_最大值",
                                                        help_text=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_最大值，"
                                                                  u"针对特殊规则类型为3（即大于最大值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"取值大于最大值时，将resultValue的之存起来；"
                                                                  u"或者取值在最大值和最小值之间，将resultValue的之存起来；")
    config_collect_receive_pors_convertrule_resultvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_最终保存的值",
                                                        help_text=u"采集指令-回复指令_采集的参数或者状态-特殊转换规则_最终保存的值，"
                                                                  u"与设置的规则和数值相对应的值")


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
                                              help_text=u"反控指令-下发指令_下发指令ID，下发指令ID，有："
                                                        u"zeroAndFull：校零校满；"
                                                        u"adjustTime：校时；"
                                                        u"immediateSample：及时采样；"
                                                        u"remoteQualityCtrl：远程质控；"
                                                        u"startTest：仪器启动测试；"
                                                        u"stopTest：仪器停止测试；"
                                                        u"autoCorrection：仪器自动校准；"
                                                        u"init：仪器初始化；"
                                                        u"checkStdSample：仪器进行标样核查；"
                                                        u"setMeasureMode：仪器修改测量模式；"
                                                        u"setMeasureInterval：仪器修改周期测量间隔；"
                                                        u"setAutoCorrectInterval：仪器修改自动校准间隔；"
                                                        u"setCheckStdSampleInterval：仪器修改自动标样核查间隔；"
                                                        u"setOneLevelPasswd：修改一级密码；"
                                                        u"setTwoLevelPasswd：修改二级密码；"
                                                        u"setThreeLevelPasswd：修改三级密码；"
                                                        u"zeroCorrectRange：零点校准量程校准；"
                                                        u"startClean：启动清洗/反吹；"
                                                        u"compareSample：比对采样；"
                                                        u"overproofSample：超标留样；"
                                                        u"setSampleCycle：设置采样时间周期；"
                                                        u"getSampleCycle：提取采样时间周期；"
                                                        u"getLastSampleTime：提取出样时间；"
                                                        u"getEquipmentId：提取设备唯一标识；"
                                                        u"getEquipmentTime：提取现场机时间；"
                                                        u"setEquipmentTime：设置现场机时间；"
                                                        u"setEquipmentParam：设置现场机参数"
                                                        u"注意：反控指令中的ID不能为空")

    config_control_send_format = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"反控指令-下发指令_下发指令类型",
                                                  help_text=u"反控指令-下发指令_下发指令类型，下发指令的类型有：;"
                                                            u"HEX(十六进制格式)：报文以HEX的形式发送；"
                                                            u"ASCII（字符串格式）：报文以ASCII的形式发送。")

    config_control_send_cmd = models.CharField(max_length=1000, default="", null=True, blank=True,
                                               verbose_name=u"反控指令-下发指令_具体下发指令",
                                               help_text=u"反控指令-下发指令_具体下发指令，"
                                                         u"例如：\"${ID}109C4A00070E0001@{SYSTEMTIME}${MODBUS_L_CRC16}\"  具体下发指令，中间部分指令内容0375320002根据需求"
                                                         u"确定,各自意思："
                                                         u"${ID}:用宏表示设备ID，表示ID可以再别处配置；"
                                                         u"03：表示功能码，和需求说明的功能码一致；"
                                                         u"7532：表示寄存器起始地址，和需求说明的寄存器起始地址一致；"
                                                         u"0002:表示寄存器个数，和需求说明的寄存器个数一致；"
                                                         u"@{SYSTEMTIME}：@{参数名}为参数，该参数的值来源于上报程序，具体的处理方法见反控指令中的参数配置；"
                                                         u"${MODBUS_L_CRC16}:表示下发指令的CRC校验方式，有四种："
                                                         u"${MODBUS_L_CRC16}：Modbus crc16位校验，低字节在前，用校验结果替换宏；"
                                                         u"${MODBUS_H_CRC16}：Modbus crc16位校验，高字节在前，用校验结果替换宏；"
                                                         u"${HJ212_CRC}：HJ212国标校验，用校验结果替换宏；"
                                                         u"${HJ212_JG_CRC}：聚光校验，用校验结果替换宏；"
                                                         u"一般多用${MODBUS_L_CRC16}，具体用哪一种需要根据需求来定；"
                                                         u"注意：如有新的规则或者校验算法可在动态管控仪的算法库中实现相应的宏。"
                                                         u"下发指令可以附带宏，其中”${}”为一项宏，会用到的宏还有："
                                                         u"${CR}：回车，会在指令会用’\r’替换该宏；"
                                                         u"${LF}：换行，会在指令会用’\n’替换该宏。")
    config_control_send_acktype = models.CharField(max_length=100, default="NO_ACK", null=True, blank=True,
                                                   verbose_name=u"反控指令-下发指令_应答包格式",
                                                   help_text=u"反控指令-下发指令_应答包格式，根据下发指令格式确定报文的类型,值有："
                                                             u"R_NO_RULE：没有规则：取走buffer中已存在的所有数据；"
                                                             u"R_HEAD_TAIL：满足指定包头和包尾的数据帧；"
                                                             u"R_HEAD_LEN：满足指定包头和长度的数据帧；"
                                                             u"R_LEN_ONLY：满足指定长度的数据帧；"
                                                             u"R_TAIL_ONLY：满足指定包尾的数据帧；"
                                                             u"R_CUSTOM_RULE：定制规则，由上层定义匹配函数matchFunc；"
                                                             u"NO_ACK：不需要回复，该规则下，不处理串口数据，一般用在反控中；"
                                                             u"R_NO_RULE使用时长去掉R，例如用R_NO_RULE，则可以填写为R_NO_RULE。"
                                                             u"应答包格式，配置为NO_ACK类型时，不需要前端仪器回复或者对回复的报文不做处理。")
    config_control_send_ackhead = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"反控指令-下发指令_回复数据的包头",
                                                   help_text=u"反控指令-下发指令_回复数据的包头，支持宏定义，”${}”,"
                                                             u"只有在R_HEAD_TAIL和R_HEAD_LEN这两种报文格式下才有意义，其他为空即可。")
    config_control_send_acktail = models.CharField(max_length=100, default="", null=True, blank=True,
                                                   verbose_name=u"反控指令-下发指令_回复报文的包尾",
                                                   help_text=u"反控指令-下发指令_回复报文的包尾，也支持宏定义，"
                                                             u"只有在R_HEAD_TAIL和R_TAIL_ONLY这两种报文格式下才有意义，其他为空即可。")
    config_control_send_acklen = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"反控指令-下发指令_回复报文的总长度",
                                                  help_text=u"反控指令-下发指令_回复报文的总长度，"
                                                            u"只有在R_HEAD_LEN和R_LEN_ONLY这两种报文格式下才有意义，其他为空即可。")
    config_control_send_ackgap = models.CharField(max_length=100, default="", null=True, blank=True,
                                                  verbose_name=u"反控指令-下发指令_回复报文的分包间隔",
                                                  help_text=u"反控指令-下发指令_回复报文的分包间隔，一般为空即可")
    config_control_send_ackcheckmode = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"反控指令-下发指令_回复报文的检验",
                                                        help_text=u"反控指令-下发指令_回复报文的检验，用来判断报文的正确性,有："
                                                                  u"MODBUS_L_CRC16：Modbus crc16位校验，低字节在前；"
                                                                  u"MODBUS_H_CRC16：Modbus crc16位校验，高字节在前；"
                                                                  u"FIXED_MARK：固定标识，会在报文中查找固定的标识，固定标识配置在校验参数中；"
                                                                  u"HJ212_CRC：国标CRC校验；"
                                                                  u"HJ212_JG_CRC：聚光CRC检验；")
    config_control_send_ackcheckarg = models.CharField(max_length=100, default="", null=True, blank=True,
                                                       verbose_name=u"反控指令-下发指令_回复报文的固定标识检验参数",
                                                       help_text=u"反控指令-下发指令_回复报文的固定标识检验参数，只有固定标识才有意义，一般为空。")

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
                                                       help_text=u"反控指令-下发指令_下发参数名，"
                                                                 u"反控指令中的参数适用于平台反控前端仪器时有参数需要下发到前端仪器中，"
                                                                 u"此时需要将参数处理并加入反控指令中。"
                                                                 u"paramId='SYSTEMTIME' 参数名，跟上面定义的参数名(即@{}中的参数名)必须一致。")

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

    config_control_send_pors_section_datatype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                 verbose_name=u"反控指令-下发指令_下发参数_数据类型",
                                                                 help_text=u"反控指令-下发指令_下发参数_数据类型，不写默认为INT,有："
                                                                           u"INT：将解析到的值以整形的形式存储成字符串；"
                                                                           u"FLOAT:将解析到的值以浮点数的形式存储成字符串。")
    config_control_send_pors_section_strformat = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                  verbose_name=u"反控指令-下发指令_下发参数_数据转换为字符串的格式",
                                                                  help_text=u"反控指令-下发指令_下发参数_数据转换为字符串的格式，"
                                                                            u"符合printf函数格式化规则,为空时默认为'%d'或'%f',"
                                                                            u"具体根据dataType（数据类型）决定，"
                                                                            u"数据类型为INT时，则为'%d'；"
                                                                            u"数据类型为FLOAT时，则为'%f'。")
    config_control_send_pors_section_findmode = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                 verbose_name=u"反控指令-下发指令_下发参数_查找模式",
                                                                 help_text=u"反控指令-下发指令_下发参数_查找模式，有："
                                                                           u"OFFSET（固定偏移）：相对包头的偏移量；"
                                                                           u"MARK（固定标识）：所有的固定标识，不能有包含与被包含的关系，否则没法解析")
    config_control_send_pors_section_offset = models.CharField(max_length=100, default="", null=True, blank=True,
                                                               verbose_name=u"反控指令-下发指令_下发参数_偏移量",
                                                               help_text=u"反控指令-下发指令_下发参数_偏移量，相对包头的，只针对固定偏移模式；")

    config_control_send_pors_section_mark = models.CharField(max_length=100, default="", null=True, blank=True,
                                                             verbose_name=u"反控指令-下发指令_下发参数_固定标识",
                                                             help_text=u"反控指令-下发指令_下发参数_固定标识，针对固定标识模式；")

    config_control_send_pors_section_len = models.CharField(max_length=100, default="", null=True, blank=True,
                                                            verbose_name=u"反控指令-下发指令_下发参数_解析的宽度",
                                                            help_text=u"反控指令-下发指令_下发参数_解析的宽度；")

    config_control_send_pors_section_decodetype = models.CharField(max_length=100, default="", null=True, blank=True,
                                                                   verbose_name=u"反控指令-下发指令_下发参数_数据解析算法",
                                                                   help_text=u"反控指令-下发指令_下发参数_数据解析算法，与解析宽度配合使用，有："
                                                                             u"decode1：将IEEE745格式的四字节数据(小端)转换成一个float型数值4321，例如：4855D04545D05548->6666.66；"
                                                                             u"decode2：将IEEE745格式的四字节数据(大端)转换成一个float型数值1234，例如：45D0554845D05548->6666.66；"
                                                                             u"decode3：将IEEE745格式的四字节数据(小端)转换成一个float型数值2143，例如：D045485545D05548->6666.66；"
                                                                             u"decode4：将IEEE745格式的四字节数据(大端)转换成一个float型数值3412，例如：554845D045D05548->6666.66；"
                                                                             u"decode5：字符串转换成浮点数，例如：“12345.3” 12345.3；"
                                                                             u"decode6：字符串转换成整形，转换宽度由上面len（即解析的宽度）决定；"
                                                                             u"decode7：字符数组转换成短整型，例如：十六进制short；，解析时间一般都用这个算法；"
                                                                             u"decode8：将一个字符的十六进制直接转换成对应的十进制，例如：0x0a10；"
                                                                             u"decode9@bit3：取对应字节的比特位，返回0或者1，例如：0x041；0x030；"
                                                                             u"decode10@1234：将十六进制字符串直接转换成4字节浮点数（可配置顺序），例如：3F9DF3B63F9DF3B6->1.234；"
                                                                             u"decode11@12：将十六进制字符串直接转换成2字节短整型（可配置顺序），例如：12351235->4661；"
                                                                             u"decode12@4312：将IEEF745格式的4字节数据转成一个float型数值（可配置顺序），例如：40009a44449A4000->1234.0；"
                                                                             u"decode13@u 字节序 或 decode13@s 字节序：16 进制字节数组转化为 4 字节整型数据 （u 代表无符号数，s 代表有符号数"
                                                                             u"；注：配置时必须指明符号类型，如果不明确是什么符号类型，请使用 s），例如："
                                                                             u"例 1： 规则：decode13@u1234 ，源字节数组（HEX）：45 1C 30 2F ，解析结果：1159475247（即45 1C 30 2F451C302F->1159475247）；"
                                                                             u"例 2： 规则：decode13@s3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果:-245 （即ff 0b ff ffFFFFFF0B->-245）；"
                                                                             u"例 3： 规则：decode13@u3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果: 4294967051（即ff 0b ff ffFFFFFF0B->4294967051；"
                                                                             u"注：对比例 2 和例 3 可观察有符号和无符号的解析差别；"
                                                                             u"decode14@u 字节序 或 decode14@s 字节序：16 进制字节数组转化为 4 字节整型数据 （u 代表无符号数，s 代表有符号数"
                                                                             u"；注：配置时必须指明符号类型，如果不明确是什么符号类型，请使用 s），例如："
                                                                             u"例 1： 规则：decode13@u1234 ，源字节数组（HEX）：45 1C 30 2F ，解析结果：1159475247（即45 1C 30 2F451C302F->1159475247）；"
                                                                             u"例 2： 规则：decode13@s3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果:-245 （即ff 0b ff ffFFFFFF0B->-245）；"
                                                                             u"例 3： 规则：decode13@u3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果: 4294967051（即ff 0b ff ffFFFFFF0B->4294967051）；"
                                                                             u"注：对比例 2 和例 3 可观察有符号和无符号的解析差别；"
                                                                             u"decode13和decode14的算法规则一样；"
                                                                             u"decode15@字节序：16 进制字节数组转化为 8 字节有符号浮点数，"
                                                                             u"例 1： 规则：decode15@12345678 ，源字节数组（HEX）： 40aa4875c28f5c29 ，解析结果：3364.23（即40aa4875c28f5c2940AA4875C28F5C29->3364.23）；"
                                                                             u"decode16：16 进制字节数组转化为 16 进制字符串对应的浮点数，"
                                                                             u"例 1： 规则：decode16 ，源字节数组（HEX）： 12 34 56 78 ，解析结果：12345678.0（即12 34 56 7812345678.0）；"
                                                                             u"注意：改算法由算法库提供当有不满足时可适当进行扩展。")

    config_control_send_pors_section_operator = models.CharField(max_length=100, default="*", null=True, blank=True,
                                                                 verbose_name=u"反控指令-下发指令_下发参数_操作符",
                                                                 help_text=u"反控指令-下发指令_下发参数_操作符，无特殊需求写*即可")
    config_control_send_pors_section_operand = models.CharField(max_length=100, default="1", null=True, blank=True,
                                                                verbose_name=u"反控指令-下发指令_下发参数_操作数",
                                                                help_text=u"反控指令-下发指令_下发参数_操作数，无特殊需求写1即可")

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
                                                        help_text=u"反控指令-下发指令_下发参数的状态-特殊转换规则_特殊规则类型，有："
                                                                  u"1：枚举类型；"
                                                                  u"2：小于最小值；"
                                                                  u"3：大于最大值；"
                                                                  u"4：最大值最小值之间；"
                                                                  u"注意：当配置多个特殊转换规则时，只要有满足的规则，之后的规则将不再判断，无特殊配置直接去掉convertRule节点。")
    config_control_send_pors_convertrule_enumvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"反控指令-下发指令_下发参数的状态-特殊转换规则_枚举值",
                                                        help_text=u"反控指令-下发指令_下发参数的状态-特殊转换规则_枚举值，"
                                                                  u"多个值之间用分号隔开，如：2;5;78,只针对特殊规则类型为1（即枚举类型），"
                                                                  u"当取值为枚举值其中之一时，将resultValue的之存起来；")
    config_control_send_pors_convertrule_minvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"反控指令-下发指令_下发参数的状态-特殊转换规则_最小值",
                                                        help_text=u"反控指令-下发指令_下发参数的状态-特殊转换规则_最小值，"
                                                                  u"针对特殊规则类型为2（即小于最小值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"取值小于最小值时，将resultValue的之存起来；"
                                                                  u"或者取值在最大值和最小值之间，将resultValue的之存起来；")
    config_control_send_pors_convertrule_maxvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"反控指令-下发指令_下发参数的状态-特殊转换规则_最大值",
                                                        help_text=u"反控指令-下发指令_下发参数的状态-特殊转换规则_最大值，"
                                                                  u"针对特殊规则类型为3（即大于最大值类型）或特殊规则类型为4(即最大值最小值之间类型)，"
                                                                  u"取值大于最大值时，将resultValue的之存起来；"
                                                                  u"或者取值在最大值和最小值之间，将resultValue的之存起来；")
    config_control_send_pors_convertrule_resultvalue = models.CharField(max_length=100, default="", null=True, blank=True,
                                                        verbose_name=u"反控指令-下发指令_下发参数的状态-特殊转换规则_最终保存的值",
                                                        help_text=u"反控指令-下发指令_下发参数的状态-特殊转换规则_最终保存的值，"
                                                                  u"与设置的规则和数值相对应的值")

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