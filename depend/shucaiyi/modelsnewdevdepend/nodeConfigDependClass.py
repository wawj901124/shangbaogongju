# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from xml.etree import ElementTree as ET
import time

from threading import Thread


def async_call(fn):    #给执行python 程序新建一个线程
    def wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapper

#读取数据库数据内容并生成新的dev文件
class MakeNodeConfig(object):
    def __init__(self,caseId):
        self.case_id = caseId
        self.node_config_object = self.getNodeConfigObject()

    def getNodeConfigObject(self):
        from shucaiyidate.modelsnewdev import NodeConfig
        NodeConfig_list = NodeConfig.objects.filter(id=int(self.case_id))
        NodeConfig_list_count = NodeConfig_list.count()
        if NodeConfig_list_count==0:
            # print("没有找到caseId：%s对应的数据，请查看是否存在相应的数据"% str(self.case_id))
            NodeConfigObject = None
        else:
            for NodeConfig_one in NodeConfig_list:
                time.sleep(1)
                NodeConfigObject = NodeConfig_one
                break
        return NodeConfigObject

    def makeDingBuXml(self):
        file_content_dingbu = """<?xml version="1.0" encoding="UTF-8"?>\n<root>\n"""
        print(file_content_dingbu)
        return file_content_dingbu

    def makeDibuXml(self):
        file_content_dibu = """</root>"""
        print(file_content_dibu)
        return file_content_dibu

    def makeVersionXml(self):
        version = self.node_config_object.config_version
        version_xml = """\t<version>%s</version>\n""" % str(version)
        print(version_xml)
        return version_xml

    def makeDeviceXml(self):
        device = self.node_config_object.config_device
        device_xml = """\t<deviceModel>%s</deviceModel>\n""" % str(device)
        print(device_xml)
        return device_xml

    def makeCollectXml(self):
        # 获取采集命令开始
        # 获取采集命令
        # 获得collect中的cmd
        from shucaiyidate.modelsnewdev import ConfigCollectSendCmd
        ConfigCollectSendCmd_list = ConfigCollectSendCmd.objects.filter(nodeconfig_id=int(self.case_id))
        ConfigCollectSendCmd_list_count = ConfigCollectSendCmd_list.count()
        if ConfigCollectSendCmd_list_count == 0:
            collect_xml = ""
        else:
            if self.node_config_object.config_collect_packet_len == None:
                ackPacketMaxLen = ""
            else:
                ackPacketMaxLen = self.node_config_object.config_collect_packet_len
            collect_xml_tou = """\t<collectCmds ackPacketMaxLen="%s">\n""" % ackPacketMaxLen

            collect_xml_content = ""
            for ConfigCollectSendCmd_one in ConfigCollectSendCmd_list:
                time.sleep(1)
                config_collect_send_id = ConfigCollectSendCmd_one.config_collect_send_id
                config_collect_send_format = ConfigCollectSendCmd_one.config_collect_send_format
                config_collect_send_cmd = ConfigCollectSendCmd_one.config_collect_send_cmd
                config_collect_send_acktype = ConfigCollectSendCmd_one.config_collect_send_acktype
                config_collect_send_ackhead = ConfigCollectSendCmd_one.config_collect_send_ackhead
                config_collect_send_acktail = ConfigCollectSendCmd_one.config_collect_send_acktail
                config_collect_send_acklen = ConfigCollectSendCmd_one.config_collect_send_acklen
                config_collect_send_ackgap = ConfigCollectSendCmd_one.config_collect_send_ackgap
                config_collect_send_ackcheckmode = ConfigCollectSendCmd_one.config_collect_send_ackcheckmode
                config_collect_send_ackcheckarg = ConfigCollectSendCmd_one.config_collect_send_ackcheckarg

                if config_collect_send_id == None:
                    config_collect_send_id = ''
                else:
                    config_collect_send_id = config_collect_send_id

                if config_collect_send_format == None:
                    config_collect_send_format = ''
                else:
                    config_collect_send_format = config_collect_send_format

                if config_collect_send_cmd == None:
                    config_collect_send_cmd = ''
                else:
                    config_collect_send_cmd = config_collect_send_cmd

                if config_collect_send_acktype == None:
                    config_collect_send_acktype = ''
                else:
                    config_collect_send_acktype = config_collect_send_acktype

                if config_collect_send_ackhead == None:
                    config_collect_send_ackhead = ''
                else:
                    config_collect_send_ackhead = config_collect_send_ackhead

                if config_collect_send_acktail == None:
                    config_collect_send_acktail = ''
                else:
                    config_collect_send_acktail = config_collect_send_acktail

                if config_collect_send_acklen == None:
                    config_collect_send_acklen = ''
                else:
                    config_collect_send_acklen = config_collect_send_acklen

                if config_collect_send_ackgap == None:
                    config_collect_send_ackgap = ''
                else:
                    config_collect_send_ackgap = config_collect_send_ackgap

                if config_collect_send_ackcheckmode == None:
                    config_collect_send_ackcheckmode = ''
                else:
                    config_collect_send_ackcheckmode = config_collect_send_ackcheckmode

                if config_collect_send_ackcheckarg == None:
                    config_collect_send_ackcheckarg = ''
                else:
                    config_collect_send_ackcheckarg = config_collect_send_ackcheckarg

                collect_cmd_xml_tou = """\t\t<cmd id="%s" format="%s" cmd="%s" ackType="%s" ackHead="%s" ackTail="%s" ackLen="%s" ackGap="%s" ackCheckMode="%s" ackCheckArg="%s">\n""" % (
                    config_collect_send_id, config_collect_send_format, config_collect_send_cmd,
                    config_collect_send_acktype, config_collect_send_ackhead,
                    config_collect_send_acktail, config_collect_send_acklen, config_collect_send_ackgap,
                    config_collect_send_ackcheckmode, config_collect_send_ackcheckarg)

                # 查看是否存在污染因子
                pollutant_xml_tol = "\t\t\t<pollutantFactor>\n"
                pollutant_xml_content = ""
                from shucaiyidate.modelsnewdev import ConfigCollectFactor
                ConfigCollectFactor_list = ConfigCollectFactor.objects.filter(
                    configcollectsendcmd_id=ConfigCollectSendCmd_one.id)
                ConfigCollectFactor_list_count = ConfigCollectFactor_list.count()
                if ConfigCollectFactor_list_count == 0:
                    pollutant_xml = ""
                else:
                    for ConfigCollectFactor_one in ConfigCollectFactor_list:
                        time.sleep(1)
                        config_collect_factor_factorcode = ConfigCollectFactor_one.config_collect_factor_factorcode
                        config_collect_factor_findmode = ConfigCollectFactor_one.config_collect_factor_findmode
                        config_collect_factor_offset = ConfigCollectFactor_one.config_collect_factor_offset
                        config_collect_factor_mark = ConfigCollectFactor_one.config_collect_factor_mark
                        config_collect_factor_len = ConfigCollectFactor_one.config_collect_factor_len
                        config_collect_factor_decodetype = ConfigCollectFactor_one.config_collect_factor_decodetype
                        config_collect_factor_operator = ConfigCollectFactor_one.config_collect_factor_operator
                        config_collect_factor_operand = ConfigCollectFactor_one.config_collect_factor_operand

                        if config_collect_factor_factorcode == None:
                            config_collect_factor_factorcode = ''
                        else:
                            config_collect_factor_factorcode = config_collect_factor_factorcode

                        if config_collect_factor_findmode == None:
                            config_collect_factor_findmode = ''
                        else:
                            config_collect_factor_findmode = config_collect_factor_findmode

                        if config_collect_factor_offset == None:
                            config_collect_factor_offset = ''
                        else:
                            config_collect_factor_offset = config_collect_factor_offset

                        if config_collect_factor_mark == None:
                            config_collect_factor_mark = ''
                        else:
                            config_collect_factor_mark = config_collect_factor_mark

                        if config_collect_factor_len == None:
                            config_collect_factor_len = ''
                        else:
                            config_collect_factor_len = config_collect_factor_len

                        if config_collect_factor_decodetype == None:
                            config_collect_factor_decodetype = ''
                        else:
                            config_collect_factor_decodetype = config_collect_factor_decodetype

                        if config_collect_factor_operator == None:
                            config_collect_factor_operator = ''
                        else:
                            config_collect_factor_operator = config_collect_factor_operator

                        if config_collect_factor_operand == None:
                            config_collect_factor_operand = ''
                        else:
                            config_collect_factor_operand = config_collect_factor_operand


                        pollutant_factor_xml = """\t\t\t\t<factor factorCode="%s" findMode="%s" offset="%s" mark="%s" len="%s" decodeType="%s" operator="%s" operand="%s"/>\n""" % (
                            config_collect_factor_factorcode, config_collect_factor_findmode,
                            config_collect_factor_offset, config_collect_factor_mark,
                            config_collect_factor_len, config_collect_factor_decodetype, config_collect_factor_operator,
                            config_collect_factor_operand)
                        pollutant_xml_content = pollutant_xml_content + pollutant_factor_xml

                    print("pollutant_xml_content:")
                    print(pollutant_xml_content)
                    pollutant_xml_wei = "\t\t\t</pollutantFactor>\n"

                    pollutant_xml = pollutant_xml_tol + pollutant_xml_content + pollutant_xml_wei

                print("pollutant_xml:")
                print(pollutant_xml)

                # 查看是否存在就收指令的参数或状态设置
                # collect_state_xml = ""
                collect_state_xml_tou = "\t\t\t<stateFactor>\n"
                from shucaiyidate.modelsnewdev import ConfigCollectReceivePors
                ConfigCollectReceivePors_list = ConfigCollectReceivePors.objects.filter(
                    configcollectsendcmd_id=ConfigCollectSendCmd_one.id)
                ConfigCollectReceivePors_list_count = ConfigCollectReceivePors_list.count()
                if ConfigCollectReceivePors_list_count == 0:
                    collect_state_xml = ""
                else:
                    collect_state_xml_content = ""
                    for ConfigCollectReceivePors_one in ConfigCollectReceivePors_list:
                        time.sleep(1)
                        config_collect_receive_pors_factorcode = ConfigCollectReceivePors_one.config_collect_receive_pors_factorcode
                        config_collect_receive_pors_factortype = ConfigCollectReceivePors_one.config_collect_receive_pors_factortype

                        if config_collect_receive_pors_factorcode == None:
                            config_collect_receive_pors_factorcode = ''
                        else:
                            config_collect_receive_pors_factorcode = config_collect_receive_pors_factorcode

                        if config_collect_receive_pors_factortype == None:
                            config_collect_receive_pors_factortype = ''
                        else:
                            config_collect_receive_pors_factortype = config_collect_receive_pors_factortype


                        collect_state_factor_xml_tou = """\t\t\t\t<factor factorCode="%s" factorType="%s">\n""" % (
                            config_collect_receive_pors_factorcode, config_collect_receive_pors_factortype)

                        # 获取factor下的section
                        from shucaiyidate.modelsnewdev import ConfigCollectReceivePorsSection
                        ConfigCollectReceivePorsSection_list = ConfigCollectReceivePorsSection.objects.filter(
                            configcollectreceivepors_id=ConfigCollectReceivePors_one.id)
                        ConfigCollectReceivePorsSection_list_count = ConfigCollectReceivePorsSection_list.count()
                        if ConfigCollectReceivePorsSection_list_count == 0:
                            collect_state_factor_xml_content = ""
                        else:
                            collect_state_factor_xml_content = ""
                            for ConfigCollectReceivePorsSection_one in ConfigCollectReceivePorsSection_list:
                                time.sleep(1)
                                config_collect_receive_pors_section_datatype = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_datatype
                                config_collect_receive_pors_section_strformat = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_strformat
                                config_collect_receive_pors_section_findmode = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_findmode
                                config_collect_receive_pors_section_offset = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_offset
                                config_collect_receive_pors_section_mark = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_mark
                                config_collect_receive_pors_section_len = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_len
                                config_collect_receive_pors_section_decodetype = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_decodetype
                                config_collect_receive_pors_section_operator = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_operator
                                config_collect_receive_pors_section_operand = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_operand

                                if config_collect_receive_pors_section_datatype == None:
                                    config_collect_receive_pors_section_datatype = ''
                                else:
                                    config_collect_receive_pors_section_datatype = config_collect_receive_pors_section_datatype

                                if config_collect_receive_pors_section_strformat == None:
                                    config_collect_receive_pors_section_strformat = ''
                                else:
                                    config_collect_receive_pors_section_strformat = config_collect_receive_pors_section_strformat

                                if config_collect_receive_pors_section_findmode == None:
                                    config_collect_receive_pors_section_findmode = ''
                                else:
                                    config_collect_receive_pors_section_findmode = config_collect_receive_pors_section_findmode

                                if config_collect_receive_pors_section_offset == None:
                                    config_collect_receive_pors_section_offset = ''
                                else:
                                    config_collect_receive_pors_section_offset = config_collect_receive_pors_section_offset

                                if config_collect_receive_pors_section_mark == None:
                                    config_collect_receive_pors_section_mark = ''
                                else:
                                    config_collect_receive_pors_section_mark = config_collect_receive_pors_section_mark

                                if config_collect_receive_pors_section_len == None:
                                    config_collect_receive_pors_section_len = ''
                                else:
                                    config_collect_receive_pors_section_len = config_collect_receive_pors_section_len

                                if config_collect_receive_pors_section_decodetype == None:
                                    config_collect_receive_pors_section_decodetype = ''
                                else:
                                    config_collect_receive_pors_section_decodetype = config_collect_receive_pors_section_decodetype

                                if config_collect_receive_pors_section_operator == None:
                                    config_collect_receive_pors_section_operator = ''
                                else:
                                    config_collect_receive_pors_section_operator = config_collect_receive_pors_section_operator

                                if config_collect_receive_pors_section_operand == None:
                                    config_collect_receive_pors_section_operand = ''
                                else:
                                    config_collect_receive_pors_section_operand = config_collect_receive_pors_section_operand


                                collect_state_factor_session_xml_tou = """\t\t\t\t\t<section dataType="%s" strFormat="%s" findMode="%s" offset="%s" mark="%s" len="%s" decodeType="%s" operator="%s" operand="%s">\n""" % (
                                    config_collect_receive_pors_section_datatype,
                                    config_collect_receive_pors_section_strformat,
                                    config_collect_receive_pors_section_findmode,
                                    config_collect_receive_pors_section_offset,
                                    config_collect_receive_pors_section_mark,
                                    config_collect_receive_pors_section_len,
                                    config_collect_receive_pors_section_decodetype,
                                    config_collect_receive_pors_section_operator,
                                    config_collect_receive_pors_section_operand)

                                # 查看是否存在特殊规则
                                from shucaiyidate.modelsnewdev import ConfigCollectReceivePorsConvertrule
                                ConfigCollectReceivePorsConvertrule_list = ConfigCollectReceivePorsConvertrule.objects.filter(
                                    configcollectreceiveporssection_id=ConfigCollectReceivePorsSection_one.id)
                                ConfigCollectReceivePorsConvertrule_list_count = ConfigCollectReceivePorsConvertrule_list.count()
                                if ConfigCollectReceivePorsConvertrule_list_count == 0:
                                    collect_state_factor_session_xml_content = ""
                                else:
                                    collect_state_factor_session_xml_content = ""
                                    for ConfigCollectReceivePorsConvertrule_one in ConfigCollectReceivePorsConvertrule_list:
                                        time.sleep(1)
                                        config_collect_receive_pors_convertrule_ruletype = ConfigCollectReceivePorsConvertrule_one.config_collect_receive_pors_convertrule_ruletype
                                        config_collect_receive_pors_convertrule_enumvalue = ConfigCollectReceivePorsConvertrule_one.config_collect_receive_pors_convertrule_enumvalue
                                        config_collect_receive_pors_convertrule_minvalue = ConfigCollectReceivePorsConvertrule_one.config_collect_receive_pors_convertrule_minvalue
                                        config_collect_receive_pors_convertrule_maxvalue = ConfigCollectReceivePorsConvertrule_one.config_collect_receive_pors_convertrule_maxvalue
                                        config_collect_receive_pors_convertrule_resultvalue = ConfigCollectReceivePorsConvertrule_one.config_collect_receive_pors_convertrule_resultvalue

                                        if config_collect_receive_pors_convertrule_ruletype == None:
                                            config_collect_receive_pors_convertrule_ruletype = ''
                                        else:
                                            config_collect_receive_pors_convertrule_ruletype = config_collect_receive_pors_convertrule_ruletype

                                        if config_collect_receive_pors_convertrule_enumvalue == None:
                                            config_collect_receive_pors_convertrule_enumvalue = ''
                                        else:
                                            config_collect_receive_pors_convertrule_enumvalue = config_collect_receive_pors_convertrule_enumvalue

                                        if config_collect_receive_pors_convertrule_minvalue == None:
                                            config_collect_receive_pors_convertrule_minvalue = ''
                                        else:
                                            config_collect_receive_pors_convertrule_minvalue = config_collect_receive_pors_convertrule_minvalue

                                        if config_collect_receive_pors_convertrule_maxvalue == None:
                                            config_collect_receive_pors_convertrule_maxvalue = ''
                                        else:
                                            config_collect_receive_pors_convertrule_maxvalue = config_collect_receive_pors_convertrule_maxvalue

                                        if config_collect_receive_pors_convertrule_resultvalue == None:
                                            config_collect_receive_pors_convertrule_resultvalue = ''
                                        else:
                                            config_collect_receive_pors_convertrule_resultvalue = config_collect_receive_pors_convertrule_resultvalue

                                        collect_convertrule_one_xml = """\t\t\t\t\t<convertRule ruleType="%s" enumValue="%s" minValue="%s" maxValue="%s" resultValue="%s"/>\n""" % (
                                            config_collect_receive_pors_convertrule_ruletype,
                                            config_collect_receive_pors_convertrule_enumvalue,
                                            config_collect_receive_pors_convertrule_minvalue,
                                            config_collect_receive_pors_convertrule_maxvalue,
                                            config_collect_receive_pors_convertrule_resultvalue)
                                        collect_state_factor_session_xml_content = collect_state_factor_session_xml_content + collect_convertrule_one_xml

                                print("collect_state_factor_session_xml_content:")
                                print(collect_state_factor_session_xml_content)

                                collect_state_factor_session_xml_wei = """\t\t\t\t\t</section>\n"""

                                collect_state_factor_session_xml = collect_state_factor_session_xml_tou + collect_state_factor_session_xml_content + collect_state_factor_session_xml_wei

                                collect_state_factor_xml_content = collect_state_factor_xml_content + collect_state_factor_session_xml
                            print("collect_state_factor_xml_content:")
                            print(collect_state_factor_xml_content)
                        collect_state_factor_xml_wei = """\t\t\t\t</factor>\n"""
                        collect_state_factor_xml = collect_state_factor_xml_tou + collect_state_factor_xml_content + collect_state_factor_xml_wei
                        collect_state_xml_content = collect_state_xml_content + collect_state_factor_xml
                    print("collect_state_xml_content:")
                    print(collect_state_xml_content)
                    collect_state_xml_wei = "\t\t\t</stateFactor>\n"
                    collect_state_xml = collect_state_xml_tou + collect_state_xml_content + collect_state_xml_wei
                print("collect_state_xml:")
                print(collect_state_xml)
                collect_cmd_xml_wei = """\t\t</cmd>\n"""

                collect_cmd_xml = collect_cmd_xml_tou + pollutant_xml + collect_state_xml + collect_cmd_xml_wei
                collect_xml_content = collect_xml_content + collect_cmd_xml

            print("collect_xml_content:")
            print(collect_xml_content)
            collect_xml_wei = """\t</collectCmds>\n"""
            collect_xml = collect_xml_tou + collect_xml_content + collect_xml_wei
        print("collect_xml:")
        print(collect_xml)
        # 获取采集命令结束
        return collect_xml

    def makeControlXml(self):
        # 获取反控命令开始
        # 获取反控命令
        # 获得control中的cmd
        from shucaiyidate.modelsnewdev import ConfigControlSendCmd
        ConfigControlSendCmd_list = ConfigControlSendCmd.objects.filter(nodeconfig_id=int(self.case_id))
        ConfigControlSendCmd_list_count = ConfigControlSendCmd_list.count()
        if ConfigControlSendCmd_list_count == 0:
            control_xml = ""
        else:
            control_xml_tou = """\t<controlCmds>\n"""
            control_xml_content = ""
            for ConfigControlSendCmd_one in ConfigControlSendCmd_list:
                time.sleep(1)
                # 建立反控指令的cmd
                config_control_send_id = ConfigControlSendCmd_one.config_control_send_id
                config_control_send_format = ConfigControlSendCmd_one.config_control_send_format
                config_control_send_cmd = ConfigControlSendCmd_one.config_control_send_cmd
                config_control_send_acktype = ConfigControlSendCmd_one.config_control_send_acktype
                config_control_send_ackhead = ConfigControlSendCmd_one.config_control_send_ackhead
                config_control_send_acktail = ConfigControlSendCmd_one.config_control_send_acktail
                config_control_send_acklen = ConfigControlSendCmd_one.config_control_send_acklen
                config_control_send_ackgap = ConfigControlSendCmd_one.config_control_send_ackgap
                config_control_send_ackcheckmode = ConfigControlSendCmd_one.config_control_send_ackcheckmode
                config_control_send_ackcheckarg = ConfigControlSendCmd_one.config_control_send_ackcheckarg

                if config_control_send_id == None:
                    config_control_send_id = ''
                else:
                    config_control_send_id = config_control_send_id

                if config_control_send_format == None:
                    config_control_send_format = ''
                else:
                    config_control_send_format = config_control_send_format

                if config_control_send_cmd == None:
                    config_control_send_cmd = ''
                else:
                    config_control_send_cmd = config_control_send_cmd

                if config_control_send_acktype == None:
                    config_control_send_acktype = ''
                else:
                    config_control_send_acktype = config_control_send_acktype

                if config_control_send_ackhead == None:
                    config_control_send_ackhead = ''
                else:
                    config_control_send_ackhead = config_control_send_ackhead

                if config_control_send_acktail == None:
                    config_control_send_acktail = ''
                else:
                    config_control_send_acktail = config_control_send_acktail

                if config_control_send_acklen == None:
                    config_control_send_acklen = ''
                else:
                    config_control_send_acklen = config_control_send_acklen

                if config_control_send_ackgap == None:
                    config_control_send_ackgap = ''
                else:
                    config_control_send_ackgap = config_control_send_ackgap

                if config_control_send_ackcheckmode == None:
                    config_control_send_ackcheckmode = ''
                else:
                    config_control_send_ackcheckmode = config_control_send_ackcheckmode

                if config_control_send_ackcheckarg == None:
                    config_control_send_ackcheckarg = ''
                else:
                    config_control_send_ackcheckarg = config_control_send_ackcheckarg


                control_cmd_xml_tou = """\t\t<cmd id="%s" format="%s" cmd="%s" ackType="%s" ackHead="%s" ackTail="%s" ackLen="%s" ackGap="%s" ackCheckMode="%s" ackCheckArg="%s">\n""" % (
                    config_control_send_id, config_control_send_format, config_control_send_cmd,
                    config_control_send_acktype, config_control_send_ackhead,
                    config_control_send_acktail, config_control_send_acklen, config_control_send_ackgap,
                    config_control_send_ackcheckmode,
                    config_control_send_ackcheckarg)

                control_cmd_xml_content = ""
                # 查看是否存在反控指令的参数或状态设置
                from shucaiyidate.modelsnewdev import ConfigControlSendParamid
                ConfigControlSendParamid_list = ConfigControlSendParamid.objects.filter(
                    configcontrolsendcmd_id=ConfigControlSendCmd_one.id)
                ConfigControlSendParamid_list_count = ConfigControlSendParamid_list.count()
                if ConfigControlSendParamid_list_count == 0:
                    control_cmd_xml_content = ""
                else:
                    control_cmd_xml_content = ""
                    for ConfigControlSendParamid_one in ConfigControlSendParamid_list:
                        time.sleep(1)
                        config_control_send_paramid = ConfigControlSendParamid_one.config_control_send_paramid

                        if config_control_send_paramid == None:
                            config_control_send_paramid = ''
                        else:
                            config_control_send_paramid = config_control_send_paramid

                        control_param_xml_tou = """\t\t\t<cmdParam paramId="%s">\n""" % config_control_send_paramid
                        # 获取cmdParam下的section
                        from shucaiyidate.modelsnewdev import ConfigControlSendPorsSection
                        ConfigControlSendPorsSection_list = ConfigControlSendPorsSection.objects.filter(
                            configcontrolsendparamid_id=ConfigControlSendParamid_one.id)
                        ConfigControlSendPorsSection_list_count = ConfigControlSendPorsSection_list.count()
                        if ConfigControlSendPorsSection_list_count == 0:
                            control_param_xml_content = ""
                        else:
                            control_param_xml_content = ""
                            control_param_factor_xml_content = ""
                            for ConfigControlSendPorsSection_one in ConfigControlSendPorsSection_list:
                                time.sleep(1)
                                config_control_send_pors_section_datatype = ConfigControlSendPorsSection_one.config_control_send_pors_section_datatype
                                config_control_send_pors_section_strformat = ConfigControlSendPorsSection_one.config_control_send_pors_section_strformat
                                config_control_send_pors_section_findmode = ConfigControlSendPorsSection_one.config_control_send_pors_section_findmode
                                config_control_send_pors_section_offset = ConfigControlSendPorsSection_one.config_control_send_pors_section_offset
                                config_control_send_pors_section_mark = ConfigControlSendPorsSection_one.config_control_send_pors_section_mark
                                config_control_send_pors_section_len = ConfigControlSendPorsSection_one.config_control_send_pors_section_len
                                config_control_send_pors_section_decodetype = ConfigControlSendPorsSection_one.config_control_send_pors_section_decodetype
                                config_control_send_pors_section_operator = ConfigControlSendPorsSection_one.config_control_send_pors_section_operator
                                config_control_send_pors_section_operand = ConfigControlSendPorsSection_one.config_control_send_pors_section_operand

                                if config_control_send_pors_section_datatype == None:
                                    config_control_send_pors_section_datatype = ''
                                else:
                                    config_control_send_pors_section_datatype = config_control_send_pors_section_datatype

                                if config_control_send_pors_section_strformat == None:
                                    config_control_send_pors_section_strformat = ''
                                else:
                                    config_control_send_pors_section_strformat = config_control_send_pors_section_strformat

                                if config_control_send_pors_section_findmode == None:
                                    config_control_send_pors_section_findmode = ''
                                else:
                                    config_control_send_pors_section_findmode = config_control_send_pors_section_findmode

                                if config_control_send_pors_section_offset == None:
                                    config_control_send_pors_section_offset = ''
                                else:
                                    config_control_send_pors_section_offset = config_control_send_pors_section_offset

                                if config_control_send_pors_section_mark == None:
                                    config_control_send_pors_section_mark = ''
                                else:
                                    config_control_send_pors_section_mark = config_control_send_pors_section_mark

                                if config_control_send_pors_section_len == None:
                                    config_control_send_pors_section_len = ''
                                else:
                                    config_control_send_pors_section_len = config_control_send_pors_section_len

                                if config_control_send_pors_section_decodetype == None:
                                    config_control_send_pors_section_decodetype = ''
                                else:
                                    config_control_send_pors_section_decodetype = config_control_send_pors_section_decodetype

                                if config_control_send_pors_section_operator == None:
                                    config_control_send_pors_section_operator = ''
                                else:
                                    config_control_send_pors_section_operator = config_control_send_pors_section_operator

                                if config_control_send_pors_section_operand == None:
                                    config_control_send_pors_section_operand = ''
                                else:
                                    config_control_send_pors_section_operand = config_control_send_pors_section_operand

                                control_param_session_xml_tou = """\t\t\t\t<section dataType="%s" strFormat="%s" findMode="%s" offset="%s" mark="%s" len="%s" decodeType="%s" operator="%s" operand="%s">\n""" % (
                                    config_control_send_pors_section_datatype,
                                    config_control_send_pors_section_strformat,
                                    config_control_send_pors_section_findmode,
                                    config_control_send_pors_section_offset,
                                    config_control_send_pors_section_mark,
                                    config_control_send_pors_section_len,
                                    config_control_send_pors_section_decodetype,
                                    config_control_send_pors_section_operator,
                                    config_control_send_pors_section_operand
                                )

                                # 查看是否存在特殊规则
                                from shucaiyidate.modelsnewdev import ConfigControlSendPorsConvertrule
                                ConfigControlSendPorsConvertrule_list = ConfigControlSendPorsConvertrule.objects.filter(
                                    configcontrolsendporssection_id=ConfigControlSendPorsSection_one.id)
                                ConfigControlSendPorsConvertrule_list_count = ConfigControlSendPorsConvertrule_list.count()
                                if ConfigControlSendPorsConvertrule_list_count == 0:
                                    control_param_session_xml_content = ""
                                else:
                                    control_param_session_xml_content = ""
                                    for ConfigControlSendPorsConvertrule_one in ConfigControlSendPorsConvertrule_list:
                                        time.sleep(1)
                                        config_control_send_pors_convertrule_ruletype = ConfigControlSendPorsConvertrule_one.config_control_send_pors_convertrule_ruletype
                                        config_control_send_pors_convertrule_enumvalue = ConfigControlSendPorsConvertrule_one.config_control_send_pors_convertrule_enumvalue
                                        config_control_send_pors_convertrule_minvalue = ConfigControlSendPorsConvertrule_one.config_control_send_pors_convertrule_minvalue
                                        config_control_send_pors_convertrule_maxvalue = ConfigControlSendPorsConvertrule_one.config_control_send_pors_convertrule_maxvalue
                                        config_control_send_pors_convertrule_resultvalue = ConfigControlSendPorsConvertrule_one.config_control_send_pors_convertrule_resultvalue

                                        if config_control_send_pors_convertrule_ruletype == None:
                                            config_control_send_pors_convertrule_ruletype = ''
                                        else:
                                            config_control_send_pors_convertrule_ruletype = config_control_send_pors_convertrule_ruletype

                                        if config_control_send_pors_convertrule_enumvalue == None:
                                            config_control_send_pors_convertrule_enumvalue = ''
                                        else:
                                            config_control_send_pors_convertrule_enumvalue = config_control_send_pors_convertrule_enumvalue

                                        if config_control_send_pors_convertrule_minvalue == None:
                                            config_control_send_pors_convertrule_minvalue = ''
                                        else:
                                            config_control_send_pors_convertrule_minvalue = config_control_send_pors_convertrule_minvalue

                                        if config_control_send_pors_convertrule_maxvalue == None:
                                            config_control_send_pors_convertrule_maxvalue = ''
                                        else:
                                            config_control_send_pors_convertrule_maxvalue = config_control_send_pors_convertrule_maxvalue

                                        if config_control_send_pors_convertrule_resultvalue == None:
                                            config_control_send_pors_convertrule_resultvalue = ''
                                        else:
                                            config_control_send_pors_convertrule_resultvalue = config_control_send_pors_convertrule_resultvalue


                                        control_convertrule_xml = """\t\t\t\t\t<convertRule ruleType="%s" enumValue="%s" minValue="%s" maxValue="%s" resultValue="%s"/>\n""" % (
                                            config_control_send_pors_convertrule_ruletype,
                                            config_control_send_pors_convertrule_enumvalue,
                                            config_control_send_pors_convertrule_minvalue,
                                            config_control_send_pors_convertrule_maxvalue,
                                            config_control_send_pors_convertrule_resultvalue)

                                        control_param_session_xml_content = control_param_session_xml_content + control_convertrule_xml

                                print("control_param_session_xml_content:")
                                print(control_param_session_xml_content)

                                control_param_session_xml_wei = """\t\t\t\t</section>\n"""

                                control_param_section_xml = control_param_session_xml_tou + control_param_session_xml_content + control_param_session_xml_wei
                                control_param_xml_content = control_param_xml_content + control_param_section_xml

                        print("control_param_xml_content:")
                        print(control_param_xml_content)

                        control_param_xml_wei = "\t\t\t</cmdParam>\n"
                        control_param_xml = control_param_xml_tou + control_param_xml_content + control_param_xml_wei

                        control_cmd_xml_content = control_cmd_xml_content + control_param_xml

                # cmd命令
                print("control_cmd_xml_content:")
                print(control_cmd_xml_content)
                control_cmd_xml_wei = """\t\t</cmd>\n """

                control_cmd_xml = control_cmd_xml_tou + control_cmd_xml_content + control_cmd_xml_wei
                control_xml_content = control_xml_content + control_cmd_xml

            print("control_xml_content:")
            print(control_xml_content)
            control_xml_wei = """\t</controlCmds>\n"""
            control_xml = control_xml_tou + control_xml_content + control_xml_wei

        # 将control加入到file_content中
        print("control_xml:")
        print(control_xml)
        # 获取反控命令结束
        return control_xml

    # #调用函数，启用新线程
    # @async_call
    def makeAllXml(self):
        if self.node_config_object != None:
            file_dingbu_xml = self.makeDingBuXml()
            file_version_xml = self.makeVersionXml()
            file_device_xml = self.makeDeviceXml()
            file_collect_xml = self.makeCollectXml()
            file_control_xml = self.makeControlXml()
            file_dibu_xml = self.makeDibuXml()
            file_content = file_dingbu_xml+file_version_xml+file_device_xml\
                           +file_collect_xml+file_control_xml+file_dibu_xml
            print("异步调用生成")
            return file_content
        else:
            print("没有找到caseId：%s 对应的数据，请查看是否存在相应的数据!!!" % self.case_id)
            return ""

    #生成新的dev并保存到数据库中
    # 使用async_call装饰起一个新线程运行
    @async_call
    def saveMakeAllXmlContentToDB(self):
        nodeconfig = self.node_config_object
        print("nodeconfig.config_file_name:")
        print(nodeconfig.config_file_name)
        print("nodeconfig.config_project:")
        print(nodeconfig.config_project)

        if nodeconfig.config_file_name == None or nodeconfig.config_file_name == "":
            file_name = str(nodeconfig.config_project) + ".dev"
            print("进入if")
        else:
            file_name = str(nodeconfig.config_file_name) + ".dev"
            print("进入else")
        print("得出的DEV文件的名字：")
        print(file_name)
        file_content = self.makeAllXml()

        # 判断文件是否存在，如果存在，则删除原有文件
        import os

        from wanwenyc.settings import MEDIA_ROOT
        from shucaiyidate.modelsnewdev import upload_dev_file_path
        u_p = upload_dev_file_path(nodeconfig, file_name)
        print("上传文件路径：")
        print(u_p)
        print("MEDIA_ROOT:")
        print(MEDIA_ROOT)

        file_name_full_path = "{}/{}".format(MEDIA_ROOT, u_p)
        print("上传文件全路径：")
        print(file_name_full_path)
        is_exist = os.path.exists(file_name_full_path)
        if is_exist:  # 如果存在，则删除文件
            os.remove(file_name_full_path)
            print("删除文件")

        from django.core.files import File  # 导入File
        from django.core.files.base import ContentFile  # 导入ContentFile
        # 使用ContentFile保存内容
        nodeconfig.dev_file.save(name=file_name, content=ContentFile(
            file_content))  # 使用ContentFile保存  #学习网址：https://www.jianshu.com/p/5c05eb437e08
        file_name_no_dev = file_name.split(".dev")[0]
        nodeconfig.config_file_name = file_name_no_dev
        nodeconfig.save()  # 保存文件名字

        with open(file_name_full_path, "w", encoding='utf-8') as f:  # 保存到文件中，以utf-8编码
            f.write(file_content)

        print("异步调用ID为【%s】的数据生成新的dev文件【%s】函数已经完成."%(str(self.case_id),str(file_name)))

    def makeDev(self):
        if self.node_config_object != None:
            file_content = self.makeAllXml()
            print("file_content:")
            print(file_content)
            # 保存内容到文件夹
            file_name = self.node_config_object.config_project + ".dev"
            # 打开文件
            with open(file_name, "w", encoding="utf-8") as f:
                # 写入内容
                f.write(file_content)
            return file_name
        else:
            print("没有找到caseId：%s 对应的数据，请查看是否存在相应的数据!!!" % self.case_id)
            return ""



    def makeDevConfig(self,caseId):
        file_content = """<?xml version="1.0" encoding="UTF-8"?>\n<root>\n"""
        from shucaiyidate.modelsnewdev import NodeConfig
        NodeConfig_list = NodeConfig.objects.filter(id=int(caseId))
        NodeConfig_list_count = NodeConfig_list.count()
        if NodeConfig_list_count==0:
            print("没有找到caseId：%s对应的数据，请查看是否存在相应的数据"% str(caseId))
            pass
        else:
            for NodeConfig_one in NodeConfig_list:
                time.sleep(1)
                #版本
                version = NodeConfig_one.config_version
                version_xml = """\t<version>%s</version>\n""" % str(version)
                file_content = file_content+version_xml
                #设备
                device = NodeConfig_one.config_device
                device_xml = """\t<deviceModel>%s</deviceModel>\n""" % str(device)
                file_content = file_content+device_xml

                #获取采集命令开始
                #获取采集命令
                #获得collect中的cmd
                from shucaiyidate.modelsnewdev import ConfigCollectSendCmd
                ConfigCollectSendCmd_list = ConfigCollectSendCmd.objects.filter(nodeconfig_id=int(caseId))
                ConfigCollectSendCmd_list_count =ConfigCollectSendCmd_list.count()
                if ConfigCollectSendCmd_list_count == 0:
                    collect_xml = ""
                else:
                    if NodeConfig_one.config_collect_packet_len == None:
                        ackPacketMaxLen = ""
                    else:
                        ackPacketMaxLen = NodeConfig_one.config_collect_packet_len
                    collect_xml_tou = """\t<collectCmds ackPacketMaxLen="%s">\n""" % ackPacketMaxLen

                    collect_xml_content = ""
                    for ConfigCollectSendCmd_one in ConfigCollectSendCmd_list:
                        time.sleep(1)
                        config_collect_send_id = ConfigCollectSendCmd_one.config_collect_send_id
                        config_collect_send_format = ConfigCollectSendCmd_one.config_collect_send_format
                        config_collect_send_cmd = ConfigCollectSendCmd_one.config_collect_send_cmd
                        config_collect_send_acktype = ConfigCollectSendCmd_one.config_collect_send_acktype
                        config_collect_send_ackhead = ConfigCollectSendCmd_one.config_collect_send_ackhead
                        config_collect_send_acktail = ConfigCollectSendCmd_one.config_collect_send_acktail
                        config_collect_send_acklen = ConfigCollectSendCmd_one.config_collect_send_acklen
                        config_collect_send_ackgap = ConfigCollectSendCmd_one.config_collect_send_ackgap
                        config_collect_send_ackcheckmode = ConfigCollectSendCmd_one.config_collect_send_ackcheckmode
                        config_collect_send_ackcheckarg = ConfigCollectSendCmd_one.config_collect_send_ackcheckarg

                        if config_collect_send_id == None:
                            config_collect_send_id = ''
                        else:
                            config_collect_send_id = config_collect_send_id

                        if config_collect_send_format == None:
                            config_collect_send_format = ''
                        else:
                            config_collect_send_format = config_collect_send_format

                        if config_collect_send_cmd == None:
                            config_collect_send_cmd = ''
                        else:
                            config_collect_send_cmd = config_collect_send_cmd

                        if config_collect_send_acktype == None:
                            config_collect_send_acktype = ''
                        else:
                            config_collect_send_acktype = config_collect_send_acktype

                        if config_collect_send_ackhead == None:
                            config_collect_send_ackhead = ''
                        else:
                            config_collect_send_ackhead = config_collect_send_ackhead

                        if config_collect_send_acktail == None:
                            config_collect_send_acktail = ''
                        else:
                            config_collect_send_acktail = config_collect_send_acktail

                        if config_collect_send_acklen == None:
                            config_collect_send_acklen = ''
                        else:
                            config_collect_send_acklen = config_collect_send_acklen

                        if config_collect_send_ackgap == None:
                            config_collect_send_ackgap = ''
                        else:
                            config_collect_send_ackgap = config_collect_send_ackgap

                        if config_collect_send_ackcheckmode == None:
                            config_collect_send_ackcheckmode = ''
                        else:
                            config_collect_send_ackcheckmode = config_collect_send_ackcheckmode

                        if config_collect_send_ackcheckarg == None:
                            config_collect_send_ackcheckarg = ''
                        else:
                            config_collect_send_ackcheckarg = config_collect_send_ackcheckarg

                        collect_cmd_xml_tou =  """\t\t<cmd id="%s" format="%s" cmd="%s" ackType="%s" ackHead="%s" ackTail="%s" ackLen="%s" ackGap="%s" ackCheckMode="%s" ackCheckArg="%s">\n""" %(
                            config_collect_send_id,config_collect_send_format,config_collect_send_cmd,config_collect_send_acktype,config_collect_send_ackhead,
                            config_collect_send_acktail,config_collect_send_acklen,config_collect_send_ackgap,config_collect_send_ackcheckmode,config_collect_send_ackcheckarg)

                        #查看是否存在污染因子
                        pollutant_xml_tol = "\t\t\t<pollutantFactor>\n"
                        pollutant_xml_content = ""
                        from shucaiyidate.modelsnewdev import ConfigCollectFactor
                        ConfigCollectFactor_list = ConfigCollectFactor.objects.filter(configcollectsendcmd_id=ConfigCollectSendCmd_one.id)
                        ConfigCollectFactor_list_count = ConfigCollectFactor_list.count()
                        if ConfigCollectFactor_list_count == 0:
                            pollutant_xml = ""
                        else:
                            for ConfigCollectFactor_one in ConfigCollectFactor_list:
                                time.sleep(1)
                                config_collect_factor_factorcode = ConfigCollectFactor_one.config_collect_factor_factorcode
                                config_collect_factor_findmode = ConfigCollectFactor_one.config_collect_factor_findmode
                                config_collect_factor_offset = ConfigCollectFactor_one.config_collect_factor_offset
                                config_collect_factor_mark = ConfigCollectFactor_one.config_collect_factor_mark
                                config_collect_factor_len = ConfigCollectFactor_one.config_collect_factor_len
                                config_collect_factor_decodetype = ConfigCollectFactor_one.config_collect_factor_decodetype
                                config_collect_factor_operator = ConfigCollectFactor_one.config_collect_factor_operator
                                config_collect_factor_operand = ConfigCollectFactor_one.config_collect_factor_operand

                                pollutant_factor_xml = """\t\t\t\t<factor factorCode="%s" findMode="%s" offset="%s" mark="%s" len="%s" decodeType="%s" operator="%s" operand="%s"/>\n"""%(
                                    config_collect_factor_factorcode,config_collect_factor_findmode,config_collect_factor_offset,config_collect_factor_mark,
                                    config_collect_factor_len,config_collect_factor_decodetype,config_collect_factor_operator,config_collect_factor_operand)
                                pollutant_xml_content = pollutant_xml_content+pollutant_factor_xml

                            print("pollutant_xml_content:")
                            print(pollutant_xml_content)
                            pollutant_xml_wei = "\t\t\t<pollutantFactor>\n"

                            pollutant_xml = pollutant_xml_tol+pollutant_xml_content+pollutant_xml_wei

                        print("pollutant_xml:")
                        print(pollutant_xml)

                        # 查看是否存在就收指令的参数或状态设置
                        # collect_state_xml = ""
                        collect_state_xml_tou =  "\t\t\t<stateFactor>\n"
                        from shucaiyidate.modelsnewdev import ConfigCollectReceivePors
                        ConfigCollectReceivePors_list = ConfigCollectReceivePors.objects.filter(configcollectsendcmd_id=ConfigCollectSendCmd_one.id)
                        ConfigCollectReceivePors_list_count = ConfigCollectReceivePors_list.count()
                        if ConfigCollectReceivePors_list_count == 0:
                            collect_state_xml = ""
                        else:
                            collect_state_xml_content = ""
                            for ConfigCollectReceivePors_one in ConfigCollectReceivePors_list:
                                time.sleep(1)
                                config_collect_receive_pors_factorcode = ConfigCollectReceivePors_one.config_collect_receive_pors_factorcode
                                config_collect_receive_pors_factortype = ConfigCollectReceivePors_one.config_collect_receive_pors_factortype
                                collect_state_factor_xml_tou ="""\t\t\t\t<factor factorCode="%s" factorType="%s">\n""" %(
                                    config_collect_receive_pors_factorcode,config_collect_receive_pors_factortype)

                                #获取factor下的section
                                from shucaiyidate.modelsnewdev import  ConfigCollectReceivePorsSection
                                ConfigCollectReceivePorsSection_list =  ConfigCollectReceivePorsSection.objects.filter(configcollectreceivepors_id=ConfigCollectReceivePors_one.id)
                                ConfigCollectReceivePorsSection_list_count = ConfigCollectReceivePorsSection_list.count()
                                if ConfigCollectReceivePorsSection_list_count == 0:
                                    collect_state_factor_xml_content = ""
                                else:
                                    collect_state_factor_xml_content = ""
                                    for ConfigCollectReceivePorsSection_one in ConfigCollectReceivePorsSection_list:
                                        time.sleep(1)
                                        config_collect_receive_pors_section_datatype = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_datatype
                                        config_collect_receive_pors_section_strformat = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_strformat
                                        config_collect_receive_pors_section_findmode = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_findmode
                                        config_collect_receive_pors_section_offset = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_offset
                                        config_collect_receive_pors_section_mark = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_mark
                                        config_collect_receive_pors_section_len = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_len
                                        config_collect_receive_pors_section_decodetype = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_decodetype
                                        config_collect_receive_pors_section_operator = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_operator
                                        config_collect_receive_pors_section_operand = ConfigCollectReceivePorsSection_one.config_collect_receive_pors_section_operand

                                        collect_state_factor_session_xml_tou = """\t\t\t\t\t<section dataType="%s" strFormat="%s" findMode="%s" offset="%s" mark="%s" len="%s" decodeType="%s" operator="%s" operand="%s">\n"""%(
                                            config_collect_receive_pors_section_datatype,config_collect_receive_pors_section_strformat,
                                            config_collect_receive_pors_section_findmode,
                                            config_collect_receive_pors_section_offset,
                                            config_collect_receive_pors_section_mark,
                                            config_collect_receive_pors_section_len,
                                            config_collect_receive_pors_section_decodetype,
                                            config_collect_receive_pors_section_operator,
                                            config_collect_receive_pors_section_operand)

                                        #查看是否存在特殊规则
                                        from shucaiyidate.modelsnewdev import ConfigCollectReceivePorsConvertrule
                                        ConfigCollectReceivePorsConvertrule_list =ConfigCollectReceivePorsConvertrule.objects.filter(configcollectreceiveporssection_id=ConfigCollectReceivePorsSection_one.id)
                                        ConfigCollectReceivePorsConvertrule_list_count = ConfigCollectReceivePorsConvertrule_list.count()
                                        if ConfigCollectReceivePorsConvertrule_list_count == 0:
                                            collect_state_factor_session_xml_content = ""
                                        else:
                                            collect_state_factor_session_xml_content = ""
                                            for ConfigCollectReceivePorsConvertrule_one in ConfigCollectReceivePorsConvertrule_list:
                                                time.sleep(1)
                                                config_collect_receive_pors_convertrule_ruletype = ConfigCollectReceivePorsConvertrule_one.config_collect_receive_pors_convertrule_ruletype
                                                config_collect_receive_pors_convertrule_enumvalue = ConfigCollectReceivePorsConvertrule_one.config_collect_receive_pors_convertrule_enumvalue
                                                config_collect_receive_pors_convertrule_minvalue = ConfigCollectReceivePorsConvertrule_one.config_collect_receive_pors_convertrule_minvalue
                                                config_collect_receive_pors_convertrule_maxvalue = ConfigCollectReceivePorsConvertrule_one.config_collect_receive_pors_convertrule_maxvalue
                                                config_collect_receive_pors_convertrule_resultvalue = ConfigCollectReceivePorsConvertrule_one.config_collect_receive_pors_convertrule_resultvalue
                                                collect_convertrule_one_xml = """\t\t\t\t\t\t<convertRule ruleType="%s" enumValue="%s" minValue="%s" maxValue="%s" resultValue="%s"/>\n"""%(
                                                    config_collect_receive_pors_convertrule_ruletype,
                                                    config_collect_receive_pors_convertrule_enumvalue,
                                                    config_collect_receive_pors_convertrule_minvalue,
                                                    config_collect_receive_pors_convertrule_maxvalue,
                                                    config_collect_receive_pors_convertrule_resultvalue)
                                                collect_state_factor_session_xml_content = collect_state_factor_session_xml_content+collect_convertrule_one_xml

                                        print("collect_state_factor_session_xml_content:")
                                        print(collect_state_factor_session_xml_content)

                                        collect_state_factor_session_xml_wei ="""\t\t\t\t\t</section>\n"""

                                        collect_state_factor_session_xml = collect_state_factor_session_xml_tou+collect_state_factor_session_xml_content+collect_state_factor_session_xml_wei

                                        collect_state_factor_xml_content = collect_state_factor_xml_content + collect_state_factor_session_xml
                                    print("collect_state_factor_xml_content:")
                                    print(collect_state_factor_xml_content)
                                collect_state_factor_xml_wei = """\t\t\t\t</factor>\n"""
                                collect_state_factor_xml = collect_state_factor_xml_tou+collect_state_factor_xml_content+collect_state_factor_xml_wei
                                collect_state_xml_content = collect_state_xml_content+collect_state_factor_xml
                            print("collect_state_xml_content:")
                            print(collect_state_xml_content)
                            collect_state_xml_wei ="\t\t\t</stateFactor>\n"
                            collect_state_xml = collect_state_xml_tou+collect_state_xml_content+collect_state_xml_wei
                        print("collect_state_xml:")
                        print(collect_state_xml)
                        collect_cmd_xml_wei = """\t\t</cmd>\n"""

                        collect_cmd_xml = collect_cmd_xml_tou+pollutant_xml+collect_state_xml+collect_cmd_xml_wei
                        collect_xml_content = collect_xml_content + collect_cmd_xml

                    print("collect_xml_content:")
                    print(collect_xml_content)
                    collect_xml_wei = """\t</collectCmds>\n"""
                    collect_xml = collect_xml_tou + collect_xml_content + collect_xml_wei
                print("collect_xml:")
                print(collect_xml)
                file_content = file_content + collect_xml
                print("file_content:")
                print(file_content)
                #获取采集命令结束

                #获取反控命令开始
                #获取反控命令
                #获得control中的cmd
                from shucaiyidate.modelsnewdev import ConfigControlSendCmd
                ConfigControlSendCmd_list = ConfigControlSendCmd.objects.filter(nodeconfig_id=int(caseId))
                ConfigControlSendCmd_list_count =ConfigControlSendCmd_list.count()
                if ConfigControlSendCmd_list_count == 0:
                    control_xml = ""
                else:
                    control_xml_tou = """\t<controlCmds>\n"""
                    control_xml_content = ""
                    for ConfigControlSendCmd_one in ConfigControlSendCmd_list:
                        time.sleep(1)
                        #建立反控指令的cmd
                        config_control_send_id = ConfigControlSendCmd_one.config_control_send_id
                        config_control_send_format = ConfigControlSendCmd_one.config_control_send_format
                        config_control_send_cmd = ConfigControlSendCmd_one.config_control_send_cmd
                        config_control_send_acktype = ConfigControlSendCmd_one.config_control_send_acktype
                        config_control_send_ackhead = ConfigControlSendCmd_one.config_control_send_ackhead
                        config_control_send_acktail = ConfigControlSendCmd_one.config_control_send_acktail
                        config_control_send_acklen = ConfigControlSendCmd_one.config_control_send_acklen
                        config_control_send_ackgap = ConfigControlSendCmd_one.config_control_send_ackgap
                        config_control_send_ackcheckmode = ConfigControlSendCmd_one.config_control_send_ackcheckmode
                        config_control_send_ackcheckarg = ConfigControlSendCmd_one.config_control_send_ackcheckarg

                        control_cmd_xml_tou =  """\t\t<cmd id="%s" format="%s" cmd="%s" ackType="%s" ackHead="%s" ackTail="%s" ackLen="%s" ackGap="%s" ackCheckMode="%s" ackCheckArg="%s">\n""" %(
                            config_control_send_id,config_control_send_format,config_control_send_cmd,config_control_send_acktype,config_control_send_ackhead,
                            config_control_send_acktail,config_control_send_acklen,config_control_send_ackgap,config_control_send_ackcheckmode,
                            config_control_send_ackcheckarg)

                        control_cmd_xml_content = ""
                        # 查看是否存在反控指令的参数或状态设置
                        from shucaiyidate.modelsnewdev import ConfigControlSendParamid
                        ConfigControlSendParamid_list = ConfigControlSendParamid.objects.filter(configcontrolsendcmd_id=ConfigControlSendCmd_one.id)
                        ConfigControlSendParamid_list_count = ConfigControlSendParamid_list.count()
                        if ConfigControlSendParamid_list_count == 0:
                            control_cmd_xml_content = ""
                        else:
                            control_cmd_xml_content = ""
                            for ConfigControlSendParamid_one in ConfigControlSendParamid_list:
                                time.sleep(1)
                                config_control_send_paramid = ConfigControlSendParamid_one.config_control_send_paramid
                                control_param_xml_tou ="""\t\t\t<cmdParam paramId="%s">\n""" % config_control_send_paramid
                                #获取cmdParam下的section
                                from shucaiyidate.modelsnewdev import  ConfigControlSendPorsSection
                                ConfigControlSendPorsSection_list = ConfigControlSendPorsSection.objects.filter(configcontrolsendparamid_id=ConfigControlSendParamid_one.id)
                                ConfigControlSendPorsSection_list_count = ConfigControlSendPorsSection_list.count()
                                if ConfigControlSendPorsSection_list_count == 0:
                                    control_param_xml_content = ""
                                else:
                                    control_param_xml_content = ""
                                    control_param_factor_xml_content = ""
                                    for ConfigControlSendPorsSection_one in ConfigControlSendPorsSection_list:
                                        time.sleep(1)
                                        config_control_send_pors_section_datatype = ConfigControlSendPorsSection_one.config_control_send_pors_section_datatype
                                        config_control_send_pors_section_strformat = ConfigControlSendPorsSection_one.config_control_send_pors_section_strformat
                                        config_control_send_pors_section_findmode = ConfigControlSendPorsSection_one.config_control_send_pors_section_findmode
                                        config_control_send_pors_section_offset = ConfigControlSendPorsSection_one.config_control_send_pors_section_offset
                                        config_control_send_pors_section_mark = ConfigControlSendPorsSection_one.config_control_send_pors_section_mark
                                        config_control_send_pors_section_len = ConfigControlSendPorsSection_one.config_control_send_pors_section_len
                                        config_control_send_pors_section_decodetype = ConfigControlSendPorsSection_one.config_control_send_pors_section_decodetype
                                        config_control_send_pors_section_operator = ConfigControlSendPorsSection_one.config_control_send_pors_section_operator
                                        config_control_send_pors_section_operand = ConfigControlSendPorsSection_one.config_control_send_pors_section_operand

                                        control_param_session_xml_tou = """\t\t\t\t<section dataType="%s" strFormat="%s" findMode="%s" offset="%s" mark="%s" len="%s" decodeType="%s" operator="%s" operand="%s">\n"""%(
                                            config_control_send_pors_section_datatype,
                                            config_control_send_pors_section_strformat,
                                            config_control_send_pors_section_findmode,
                                            config_control_send_pors_section_offset,
                                            config_control_send_pors_section_mark,
                                            config_control_send_pors_section_len,
                                            config_control_send_pors_section_decodetype,
                                            config_control_send_pors_section_operator,
                                            config_control_send_pors_section_operand
                                        )

                                        #查看是否存在特殊规则
                                        from shucaiyidate.modelsnewdev import ConfigControlSendPorsConvertrule
                                        ConfigControlSendPorsConvertrule_list =ConfigControlSendPorsConvertrule.objects.filter(configcontrolsendporssection_id=ConfigControlSendPorsSection_one.id)
                                        ConfigControlSendPorsConvertrule_list_count = ConfigControlSendPorsConvertrule_list.count()
                                        if ConfigControlSendPorsConvertrule_list_count == 0:
                                            control_param_session_xml_content = ""
                                        else:
                                            control_param_session_xml_content = ""
                                            for ConfigControlSendPorsConvertrule_one in ConfigControlSendPorsConvertrule_list:
                                                time.sleep(1)
                                                config_control_send_pors_convertrule_ruletype = ConfigControlSendPorsConvertrule_one.config_control_send_pors_convertrule_ruletype
                                                config_control_send_pors_convertrule_enumvalue = ConfigControlSendPorsConvertrule_one.config_control_send_pors_convertrule_enumvalue
                                                config_control_send_pors_convertrule_minvalue = ConfigControlSendPorsConvertrule_one.config_control_send_pors_convertrule_minvalue
                                                config_control_send_pors_convertrule_maxvalue = ConfigControlSendPorsConvertrule_one.config_control_send_pors_convertrule_maxvalue
                                                config_control_send_pors_convertrule_resultvalue = ConfigControlSendPorsConvertrule_one.config_control_send_pors_convertrule_resultvalue

                                                control_convertrule_xml = """\t\t\t\t\t<convertRule ruleType="%s" enumValue="%s" minValue="%s" maxValue="%s" resultValue="%s"/>\n"""%(
                                                    config_control_send_pors_convertrule_ruletype,config_control_send_pors_convertrule_enumvalue,
                                                    config_control_send_pors_convertrule_minvalue,config_control_send_pors_convertrule_maxvalue,
                                                    config_control_send_pors_convertrule_resultvalue)

                                                control_param_session_xml_content = control_param_session_xml_content + control_convertrule_xml

                                        print("control_param_session_xml_content:")
                                        print(control_param_session_xml_content)

                                        control_param_session_xml_wei ="""\t\t\t\t\</section>\n"""

                                        control_param_section_xml = control_param_session_xml_tou + control_param_session_xml_content + control_param_session_xml_wei
                                        control_param_xml_content = control_param_xml_content+control_param_section_xml

                                print("control_param_xml_content:")
                                print(control_param_xml_content)

                                control_param_xml_wei ="\t\t\t</cmdParam>\n"
                                control_param_xml = control_param_xml_tou+control_param_xml_content+control_param_xml_wei

                                control_cmd_xml_content = control_cmd_xml_content+control_param_xml

                        #cmd命令
                        print("control_cmd_xml_content:")
                        print(control_cmd_xml_content)
                        control_cmd_xml_wei = """\t\t</cmd>\n """

                        control_cmd_xml = control_cmd_xml_tou+control_cmd_xml_content+control_cmd_xml_wei
                        control_xml_content = control_xml_content + control_cmd_xml

                    print("control_xml_content:")
                    print(control_xml_content)
                    control_xml_wei = """\t</controlCmds>\n"""
                    control_xml = control_xml_tou + control_xml_content + control_xml_wei

                #将control加入到file_content中
                print("control_xml:")
                print(control_xml)
                file_content = file_content + control_xml
                #获取反控命令结束

                #加最后的根目录
                end_root = """</root>"""
                file_content = file_content + end_root

                print("file_content:")
                print(file_content)

                #保存内容到文件夹
                file_name = NodeConfig_one.config_project+".dev"
                #打开文件
                with open(file_name, "w",encoding="utf-8") as f:
                    #写入内容
                    f.write(file_content)

                break  #终止循环，只处理第一个

        return file_content

#读取数据库中上传的文件并将文件内容保存入库
class ReadNodeConfig(object):
    def __init__(self,filePath,caseId):
        self.file_path = filePath
        self.content_list = self.readFile()
        self.case_id = int(caseId)
        self.node_config = self.createDB()
        self.xml_tree = self.readXml()
        self.xml_root = self.getRootFromXml()
        self.file_name = self.splitPathFile()


    #读取文件,并一行为单位项，返回一个列表
    def readFile(self):
        with open(self.file_path,"r",encoding="utf-8") as f:
            file_content_list = f.readlines()

        print("file_content_list:")
        print(file_content_list)
        return file_content_list

    #根据文件全路径获取文件名作为工程名字
    def splitPathFile(self):
        import re
        path_list = re.split('[/\\\\]', self.file_path)
        print(path_list)
        file_name = path_list[-1]   #获取最后一项
        print(file_name)
        file_name_list = file_name.split(".")
        project_name = file_name_list[0]
        print(project_name)
        return project_name

    def createDB(self):
        from shucaiyidate.modelsnewdev import NodeConfig
        nodeconfig = NodeConfig.objects.get(id=self.case_id)
        return nodeconfig

    def saveProjectName(self):
        #如果文件名称不等于上传的文件名称则修改为上传的文件名称
        if self.node_config.config_file_name !=self.file_name:
            self.node_config.config_file_name = self.file_name
            self.node_config.save()

    def readXml(self):
        xml_tree = ET.parse(self.file_path)
        print(xml_tree)
        return xml_tree

    def getRootFromXml(self):
        xml_root = self.xml_tree.getroot()
        return xml_root

    def saveVersionFromXml(self):
        version_node_list = self.xml_tree.getiterator("version")
        for version_node_one in version_node_list:
            time.sleep(1)
            version_content = version_node_one.text
            #保存 version
            self.node_config.config_version = version_content
            self.node_config.save()   #保存版本信息
            break
        print(version_content)

    def saveDeviceFromXml(self):
        device_node_list = self.xml_tree.getiterator("deviceModel")
        for device_node_one in device_node_list:
            time.sleep(1)
            device_content = device_node_one.text
            #保存 device
            self.node_config.config_device = device_content
            self.node_config.save()   #保存版本信息
            break
        print(device_content)

    def saveCollectFromXml(self):
        collect_node_list = self.xml_tree.getiterator("collectCmds")
        collect_node_list_len = len(collect_node_list)
        if collect_node_list_len == 0:   #如果节点个数为0，
            pass
        else: #否则返回节点
            for collect_node_one in collect_node_list:
                    time.sleep(1)
                    #保存节点属性
                    collect_attrib_dict = collect_node_one.attrib
                    print(collect_attrib_dict)
                    collect_attrib_dict_ackPacketMaxLen = collect_attrib_dict["ackPacketMaxLen"]
                    self.node_config.config_collect_packet_len = collect_attrib_dict_ackPacketMaxLen
                    self.node_config.save()  # 保存版本信息

                    #获取下发指令cmd
                    collect_cmd_list = collect_node_one.findall("cmd")
                    collect_cmd_list_len = len(collect_cmd_list)
                    if collect_cmd_list_len == 0:
                        pass
                    else:
                        for collect_cmd_one in collect_cmd_list:
                            time.sleep(1)
                            collect_cmd_one_attrib_dict = collect_cmd_one.attrib
                            print(collect_cmd_one_attrib_dict)
                            collect_cmd_one_id = collect_cmd_one_attrib_dict["id"]
                            collect_cmd_one_format = collect_cmd_one_attrib_dict["format"]
                            collect_cmd_one_cmd = collect_cmd_one_attrib_dict["cmd"]
                            collect_cmd_one_ackType = collect_cmd_one_attrib_dict["ackType"]
                            collect_cmd_one_ackHead = collect_cmd_one_attrib_dict["ackHead"]
                            collect_cmd_one_ackTail = collect_cmd_one_attrib_dict["ackTail"]
                            collect_cmd_one_ackLen = collect_cmd_one_attrib_dict["ackLen"]
                            collect_cmd_one_ackGap = collect_cmd_one_attrib_dict["ackGap"]
                            collect_cmd_one_ackCheckMode = collect_cmd_one_attrib_dict["ackCheckMode"]
                            collect_cmd_one_ackCheckArg = collect_cmd_one_attrib_dict["ackCheckArg"]

                            #保存下发指令
                            from shucaiyidate.modelsnewdev import ConfigCollectSendCmd
                            #先查看是否找到nodeconfig_id的值为当前caseid，并且存在cmd，则不保存
                            check_ConfigCollectSendCmd_list = ConfigCollectSendCmd.objects.filter(nodeconfig_id=self.case_id).filter(config_collect_send_cmd=collect_cmd_one_cmd)
                            check_ConfigCollectSendCmd_list_count = check_ConfigCollectSendCmd_list.count()
                            if check_ConfigCollectSendCmd_list_count == 0:#如果不存在，则保存
                                #保存，并获取最新一条数据
                                new_configcollectsendcmd =  ConfigCollectSendCmd()
                                new_configcollectsendcmd.nodeconfig_id = self.case_id
                                new_configcollectsendcmd.config_collect_send_id = collect_cmd_one_id
                                new_configcollectsendcmd.config_collect_send_format = collect_cmd_one_format
                                new_configcollectsendcmd.config_collect_send_cmd = collect_cmd_one_cmd
                                new_configcollectsendcmd.config_collect_send_acktype = collect_cmd_one_ackType
                                new_configcollectsendcmd.config_collect_send_ackhead = collect_cmd_one_ackHead
                                new_configcollectsendcmd.config_collect_send_acktail = collect_cmd_one_ackTail
                                new_configcollectsendcmd.config_collect_send_acklen = collect_cmd_one_ackLen
                                new_configcollectsendcmd.config_collect_send_ackgap = collect_cmd_one_ackGap
                                new_configcollectsendcmd.config_collect_send_ackcheckmode = collect_cmd_one_ackCheckMode
                                new_configcollectsendcmd.config_collect_send_ackcheckarg = collect_cmd_one_ackCheckArg
                                new_configcollectsendcmd.save()

                                zx_configcollectsendcmd = ConfigCollectSendCmd.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
                            else:  #否则筛选到这个对象
                                for check_ConfigCollectSendCmd_one in check_ConfigCollectSendCmd_list:
                                    time.sleep(1)
                                    zx_configcollectsendcmd = check_ConfigCollectSendCmd_one
                                    break  #只取第一个

                            #获取collect_cmd的子节点
                            collect_cmd_one_children_list = collect_cmd_one.getchildren()   #获取子节点
                            collect_cmd_one_children_list_len = len(collect_cmd_one_children_list)
                            print(collect_cmd_one_children_list)
                            if collect_cmd_one_children_list_len == 0:  #说明不存在子节点，不保存
                                pass
                            else: #否则进行保存
                                for collect_cmd_one_children_one in collect_cmd_one_children_list:
                                    time.sleep(1)
                                    # 获取下发指令中的监测因子
                                    if 'pollutantFactor' in str(collect_cmd_one_children_one):  #说明是监测因子
                                        pollutantfactor_factor_list = collect_cmd_one_children_one.getchildren()   #获取子节点
                                        pollutantfactor_factor_list_len = len(pollutantfactor_factor_list)
                                        if pollutantfactor_factor_list_len == 0:
                                            pass
                                        else:  #否则，遍历保存因子
                                            for pollutantfactor_factor_one in pollutantfactor_factor_list:
                                                time.sleep(1)
                                                pollutantfactor_factor_one_attrib_dict = pollutantfactor_factor_one.attrib
                                                print("监测因子属性字典：")
                                                print(pollutantfactor_factor_one_attrib_dict)
                                                pollutantfactor_factor_one_factorCode = pollutantfactor_factor_one_attrib_dict["factorCode"]
                                                pollutantfactor_factor_one_findMode = pollutantfactor_factor_one_attrib_dict["findMode"]
                                                pollutantfactor_factor_one_offset = pollutantfactor_factor_one_attrib_dict["offset"]
                                                pollutantfactor_factor_one_mark = pollutantfactor_factor_one_attrib_dict["mark"]
                                                pollutantfactor_factor_one_len = pollutantfactor_factor_one_attrib_dict["len"]
                                                pollutantfactor_factor_one_decodeType = pollutantfactor_factor_one_attrib_dict["decodeType"]
                                                pollutantfactor_factor_one_operator = pollutantfactor_factor_one_attrib_dict["operator"]
                                                pollutantfactor_factor_one_operand = pollutantfactor_factor_one_attrib_dict["operand"]

                                                #保存监测因子
                                                from shucaiyidate.modelsnewdev import ConfigCollectFactor

                                                #如果筛选到相应的内容，则不再保存，否则，进行保存
                                                check_ConfigCollectFactor_list = ConfigCollectFactor.objects.filter(nodeconfig_id=self.case_id).\
                                                    filter(configcollectsendcmd_id=zx_configcollectsendcmd.id).\
                                                    filter(config_collect_factor_factorcode=pollutantfactor_factor_one_factorCode)
                                                check_ConfigCollectFactor_list_count = check_ConfigCollectFactor_list.count()

                                                if check_ConfigCollectFactor_list_count == 0:  #没有查询到，则保存，并获取最新一条数据
                                                    new_configcollectfactor = ConfigCollectFactor()
                                                    new_configcollectfactor.nodeconfig_id = self.case_id
                                                    new_configcollectfactor.configcollectsendcmd_id = zx_configcollectsendcmd.id
                                                    new_configcollectfactor.config_collect_factor_factorcode = pollutantfactor_factor_one_factorCode
                                                    new_configcollectfactor.config_collect_factor_findmode = pollutantfactor_factor_one_findMode
                                                    new_configcollectfactor.config_collect_factor_offset = pollutantfactor_factor_one_offset
                                                    new_configcollectfactor.config_collect_factor_mark = pollutantfactor_factor_one_mark
                                                    new_configcollectfactor.config_collect_factor_len = pollutantfactor_factor_one_len
                                                    new_configcollectfactor.config_collect_factor_decodetype = pollutantfactor_factor_one_decodeType
                                                    new_configcollectfactor.config_collect_factor_operator = pollutantfactor_factor_one_operator
                                                    new_configcollectfactor.config_collect_factor_operand =  pollutantfactor_factor_one_operand
                                                    new_configcollectfactor.save()  # 保存
                                                    print("保存因子数据")
                                                else:  #否则不保存数据，获取筛选到的内容
                                                    pass

                                    # 获取下发指令中的 采集指令_回复指令中的参数或状态
                                    elif 'stateFactor' in str(collect_cmd_one_children_one):  # 说明是采集指令_回复指令中的参数或状态
                                        statefactor_factor_list = collect_cmd_one_children_one.getchildren()   #获取子节点
                                        statefactor_factor_list_len = len(statefactor_factor_list)
                                        if statefactor_factor_list_len == 0:  #说明不存在子节点
                                            pass
                                        else:  #否则保存子节点
                                            for statefactor_factor_one in statefactor_factor_list:
                                                time.sleep(1)
                                                statefactor_factor_one_attrib_dict = statefactor_factor_one.attrib
                                                print("采集指令_回复指令中的参数或状态属性字典：")
                                                print(statefactor_factor_one_attrib_dict)
                                                statefactor_factor_one_factorCode = statefactor_factor_one_attrib_dict["factorCode"]
                                                statefactor_factor_one_factorType = statefactor_factor_one_attrib_dict["factorType"]

                                                #保存 采集指令_回复指令中的参数或状态
                                                from shucaiyidate.modelsnewdev import ConfigCollectReceivePors
                                                check_ConfigCollectReceivePors_list = ConfigCollectReceivePors.objects.filter(nodeconfig_id=self.case_id).\
                                                    filter(configcollectsendcmd_id=zx_configcollectsendcmd.id).\
                                                    filter(config_collect_receive_pors_factorcode=statefactor_factor_one_factorCode).\
                                                    filter(config_collect_receive_pors_factortype=statefactor_factor_one_factorType)
                                                check_ConfigCollectReceivePors_list_count = check_ConfigCollectReceivePors_list.count()
                                                if check_ConfigCollectReceivePors_list_count == 0:   #如果没有筛选到内容，则说明不存在相同的数据，需要保存数据
                                                    new_configcollectreceivepors = ConfigCollectReceivePors()
                                                    new_configcollectreceivepors.nodeconfig_id = self.case_id
                                                    new_configcollectreceivepors.configcollectsendcmd_id = zx_configcollectsendcmd.id
                                                    new_configcollectreceivepors.config_collect_receive_pors_factorcode = statefactor_factor_one_factorCode
                                                    new_configcollectreceivepors.config_collect_receive_pors_factortype = statefactor_factor_one_factorType
                                                    new_configcollectreceivepors.save()  # 保存

                                                    zx_configcollectreceivepors = ConfigCollectReceivePors.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
                                                else:  #否则获取查询到的数据
                                                    for check_ConfigCollectReceivePors_one in check_ConfigCollectReceivePors_list:
                                                        time.sleep(1)
                                                        zx_configcollectreceivepors = check_ConfigCollectReceivePors_one
                                                        break  #只获取第一条

                                                #获取factor下的子节点
                                                collect_section_list = statefactor_factor_one.getchildren()   #获取子节点
                                                collect_section_list_len = len(collect_section_list)
                                                if collect_section_list_len == 0:  #说明不存在子节点，不需要保存
                                                    pass
                                                else:  #否则需要保存
                                                    for collect_section_one in collect_section_list:
                                                        time.sleep(1)
                                                        collect_section_one_attrib_dict = collect_section_one.attrib
                                                        print("采集指令_回复指令中的参数或状态_数据解析配置属性字典:")
                                                        print(collect_section_one_attrib_dict)

                                                        collect_section_one_dataType = collect_section_one_attrib_dict["dataType"]
                                                        collect_section_one_strFormat = collect_section_one_attrib_dict["strFormat"]
                                                        collect_section_one_findMode = collect_section_one_attrib_dict["findMode"]
                                                        collect_section_one_offset = collect_section_one_attrib_dict["offset"]
                                                        collect_section_one_mark = collect_section_one_attrib_dict["mark"]
                                                        collect_section_one_len = collect_section_one_attrib_dict["len"]
                                                        collect_section_one_decodeType = collect_section_one_attrib_dict["decodeType"]
                                                        collect_section_one_operator = collect_section_one_attrib_dict["operator"]
                                                        collect_section_one_operand = collect_section_one_attrib_dict["operand"]

                                                        #筛选相应的内容，如果可以查询到，则不保存，否则，保存
                                                        from shucaiyidate.modelsnewdev import ConfigCollectReceivePorsSection

                                                        check_ConfigCollectReceivePorsSection_list = ConfigCollectReceivePorsSection.objects.filter(nodeconfig_id=self.case_id).\
                                                            filter(configcollectreceivepors_id=zx_configcollectreceivepors.id).\
                                                            filter(config_collect_receive_pors_section_findmode=collect_section_one_findMode).\
                                                            filter(config_collect_receive_pors_section_offset=collect_section_one_offset).\
                                                            filter(config_collect_receive_pors_section_mark=collect_section_one_mark)
                                                        check_ConfigCollectReceivePorsSection_list_count = check_ConfigCollectReceivePorsSection_list.count()

                                                        if check_ConfigCollectReceivePorsSection_list_count == 0: #说明没有数据，需要保存
                                                            new_configcollectreceiveporssection = ConfigCollectReceivePorsSection()
                                                            new_configcollectreceiveporssection.nodeconfig_id = self.case_id
                                                            new_configcollectreceiveporssection.configcollectreceivepors_id = zx_configcollectreceivepors.id
                                                            new_configcollectreceiveporssection.config_collect_receive_pors_section_datatype = collect_section_one_dataType
                                                            new_configcollectreceiveporssection.config_collect_receive_pors_section_strformat = collect_section_one_strFormat
                                                            new_configcollectreceiveporssection.config_collect_receive_pors_section_findmode = collect_section_one_findMode
                                                            new_configcollectreceiveporssection.config_collect_receive_pors_section_offset = collect_section_one_offset
                                                            new_configcollectreceiveporssection.config_collect_receive_pors_section_mark = collect_section_one_mark
                                                            new_configcollectreceiveporssection.config_collect_receive_pors_section_len = collect_section_one_len
                                                            new_configcollectreceiveporssection.config_collect_receive_pors_section_decodetype = collect_section_one_decodeType
                                                            new_configcollectreceiveporssection.config_collect_receive_pors_section_operator = collect_section_one_operator
                                                            new_configcollectreceiveporssection.config_collect_receive_pors_section_operand = collect_section_one_operand
                                                            new_configcollectreceiveporssection.save()

                                                            zx_configcollectreceiveporssection = ConfigCollectReceivePorsSection.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
                                                        else:  #否则，获取最新的筛选到一条数据
                                                            for check_ConfigCollectReceivePorsSection_one in check_ConfigCollectReceivePorsSection_list:
                                                                time.sleep(1)
                                                                zx_configcollectreceiveporssection = check_ConfigCollectReceivePorsSection_one
                                                                break  #只获取第一条

                                                        # 获取section下的子节点
                                                        collect_convertrule_list = collect_section_one.getchildren()  # 获取子节点
                                                        collect_convertrule_list_len = len(collect_convertrule_list)
                                                        if collect_convertrule_list_len == 0:  #如果没有子节点，则不保存
                                                            pass
                                                        else: #否则，保存节点数据
                                                            for collect_convertrule_one in collect_convertrule_list:
                                                                time.sleep(1)
                                                                collect_convertrule_one_attrib_dict = collect_convertrule_one.attrib
                                                                print("采集指令_回复指令中的参数或状态_数据解析配置_特殊规则属性字典:")
                                                                print(collect_convertrule_one_attrib_dict)
                                                                collect_convertrule_one_ruleType = collect_convertrule_one_attrib_dict["ruleType"]
                                                                collect_convertrule_one_enumValue = collect_convertrule_one_attrib_dict["enumValue"]
                                                                collect_convertrule_one_minValue = collect_convertrule_one_attrib_dict["minValue"]
                                                                collect_convertrule_one_maxValue = collect_convertrule_one_attrib_dict["maxValue"]
                                                                collect_convertrule_one_resultValue = collect_convertrule_one_attrib_dict["resultValue"]

                                                                #保存节点数据
                                                                from shucaiyidate.modelsnewdev import ConfigCollectReceivePorsConvertrule

                                                                #筛选数据，如果筛选到则不再保存，如果没有则保存
                                                                check_ConfigCollectReceivePorsConvertrule_list = ConfigCollectReceivePorsConvertrule.objects.filter(nodeconfig_id=self.case_id).\
                                                                    filter(configcollectreceiveporssection_id=zx_configcollectreceiveporssection.id).\
                                                                    filter(config_collect_receive_pors_convertrule_ruletype = collect_convertrule_one_ruleType).\
                                                                    filter(config_collect_receive_pors_convertrule_enumvalue=collect_convertrule_one_enumValue).\
                                                                    filter(config_collect_receive_pors_convertrule_minvalue = collect_convertrule_one_minValue).\
                                                                    filter(config_collect_receive_pors_convertrule_maxvalue = collect_convertrule_one_maxValue).\
                                                                    filter(config_collect_receive_pors_convertrule_resultvalue = collect_convertrule_one_resultValue)

                                                                check_ConfigCollectReceivePorsConvertrule_list_count = check_ConfigCollectReceivePorsConvertrule_list.count()

                                                                if check_ConfigCollectReceivePorsConvertrule_list_count == 0:  #说明不存在，需要保存
                                                                    new_configcollectreceiveporsconvertrule = ConfigCollectReceivePorsConvertrule()
                                                                    new_configcollectreceiveporsconvertrule.nodeconfig_id = self.case_id
                                                                    new_configcollectreceiveporsconvertrule.configcollectreceiveporssection_id = zx_configcollectreceiveporssection.id
                                                                    new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_ruletype = collect_convertrule_one_ruleType
                                                                    new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_enumvalue = collect_convertrule_one_enumValue
                                                                    new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_minvalue = collect_convertrule_one_minValue
                                                                    new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_maxvalue = collect_convertrule_one_maxValue
                                                                    new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_resultvalue = collect_convertrule_one_resultValue
                                                                    new_configcollectreceiveporsconvertrule.save()
                                                                else:
                                                                    pass

    def saveControlFromXml(self):
        control_node_list = self.xml_tree.getiterator("controlCmds")
        control_node_list_len = len(control_node_list)
        if control_node_list_len == 0:  #如果节点个数为0，则不保存
            pass
        else:  #否则，保存数据
            for control_node_one in control_node_list:
                time.sleep(1)
                #获取反控指令cmd节点
                control_cmd_list = control_node_one.findall("cmd")
                control_cmd_list_len = len(control_cmd_list)
                if control_cmd_list_len == 0:   #说明没有cmd
                    pass
                else:
                    for control_cmd_one in control_cmd_list:
                        time.sleep(1)
                        control_cmd_one_attrib_dict = control_cmd_one.attrib
                        print(control_cmd_one_attrib_dict)
                        control_cmd_one_id = control_cmd_one_attrib_dict["id"]
                        control_cmd_one_format = control_cmd_one_attrib_dict["format"]
                        control_cmd_one_cmd = control_cmd_one_attrib_dict["cmd"]
                        control_cmd_one_ackType = control_cmd_one_attrib_dict["ackType"]
                        control_cmd_one_ackHead = control_cmd_one_attrib_dict["ackHead"]
                        control_cmd_one_ackTail = control_cmd_one_attrib_dict["ackTail"]
                        control_cmd_one_ackLen = control_cmd_one_attrib_dict["ackLen"]
                        control_cmd_one_ackGap = control_cmd_one_attrib_dict["ackGap"]
                        control_cmd_one_ackCheckMode = control_cmd_one_attrib_dict["ackCheckMode"]
                        control_cmd_one_ackCheckArg = control_cmd_one_attrib_dict["ackCheckArg"]

                        #筛选，如果查找到，则获取找到的内容，如果没查找到，则进行保存
                        from shucaiyidate.modelsnewdev import ConfigControlSendCmd
                        check_ConfigControlSendCmd_list = ConfigControlSendCmd.objects.filter(nodeconfig_id=self.case_id).\
                            filter(config_control_send_cmd=control_cmd_one_cmd)
                        check_ConfigControlSendCmd_list_count = check_ConfigControlSendCmd_list.count()
                        if check_ConfigControlSendCmd_list_count == 0:  #则说明没有筛选到数据，需要保存数据
                            new_configcontrolsendcmd = ConfigControlSendCmd()
                            new_configcontrolsendcmd.nodeconfig_id = self.case_id
                            new_configcontrolsendcmd.config_control_send_id =  control_cmd_one_id
                            new_configcontrolsendcmd.config_control_send_format = control_cmd_one_format
                            new_configcontrolsendcmd.config_control_send_cmd = control_cmd_one_cmd
                            new_configcontrolsendcmd.config_control_send_acktype = control_cmd_one_ackType
                            new_configcontrolsendcmd.config_control_send_ackhead = control_cmd_one_ackHead
                            new_configcontrolsendcmd.config_control_send_acktail = control_cmd_one_ackTail
                            new_configcontrolsendcmd.config_control_send_acklen = control_cmd_one_ackLen
                            new_configcontrolsendcmd.config_control_send_ackgap = control_cmd_one_ackGap
                            new_configcontrolsendcmd.config_control_send_ackcheckmode = control_cmd_one_ackCheckMode
                            new_configcontrolsendcmd.config_control_send_ackcheckarg = control_cmd_one_ackCheckArg
                            new_configcontrolsendcmd.save()

                            zx_configcontrolsendcmd = ConfigControlSendCmd.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
                        else:  #获取筛选到的数据
                            for check_ConfigControlSendCmd_one  in check_ConfigControlSendCmd_list:
                                time.sleep(1)
                                zx_configcontrolsendcmd = check_ConfigControlSendCmd_one
                                break  #只获取第一项

                        #获取cmdParam节点
                        control_cmdParam_list = control_cmd_one.findall("cmdParam")
                        control_cmdParam_list_len = len(control_cmdParam_list)
                        if control_cmdParam_list_len == 0:  #如果没有子节点，则不需要保存
                            pass
                        else: #否则保存节点数据
                            for control_cmdParam_one in control_cmdParam_list:
                                time.sleep(1)
                                control_cmdParam_one_attrib_dict = control_cmdParam_one.attrib   #获取属性字典
                                print("反控指令_下发指令_参数字典属性：")
                                print(control_cmdParam_one_attrib_dict)
                                control_cmdParam_one_paramId = control_cmdParam_one_attrib_dict["paramId"]

                                #筛选到相应的数据就取筛选到的数据，没有筛选到就保存新数据
                                from shucaiyidate.modelsnewdev import ConfigControlSendParamid

                                check_ConfigControlSendParamid_list = ConfigControlSendParamid.objects.filter(nodeconfig_id=self.case_id).\
                                    filter(configcontrolsendcmd_id=zx_configcontrolsendcmd.id).\
                                    filter(config_control_send_paramid = control_cmdParam_one_paramId)
                                check_ConfigControlSendParamid_list_count = check_ConfigControlSendParamid_list.count()

                                if check_ConfigControlSendParamid_list_count == 0:  #说明没有筛选到相应的数据，需要保存
                                    new_configcontrolsendparamid = ConfigControlSendParamid()
                                    new_configcontrolsendparamid.nodeconfig_id = self.case_id
                                    new_configcontrolsendparamid.configcontrolsendcmd_id = zx_configcontrolsendcmd.id
                                    new_configcontrolsendparamid.config_control_send_paramid = control_cmdParam_one_paramId
                                    new_configcontrolsendparamid.save()

                                    zx_configcontrolsendparamid = ConfigControlSendParamid.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的

                                else:
                                    for check_ConfigControlSendParamid_one in check_ConfigControlSendParamid_list:
                                        time.sleep(1)
                                        zx_configcontrolsendparamid = check_ConfigControlSendParamid_one
                                        break   #只获取第一条数据


                                #获取 反控指令_下发指令_参数_配置 节点内容
                                control_section_list = control_cmdParam_one.findall("section")
                                control_section_list_len = len(control_section_list)
                                if control_section_list_len == 0: #说明没有节点，不需要配置
                                    pass
                                else:  #保存节点内容
                                    for control_section_one in control_section_list:
                                        time.sleep(1)
                                        control_section_one_attrib_dict = control_section_one.attrib  #获取属性字典内容
                                        print("反控指令_下发指令_参数_配置字典属性:")
                                        print(control_section_one_attrib_dict)

                                        control_section_one_dataType = control_section_one_attrib_dict["dataType"]
                                        control_section_one_strFormat = control_section_one_attrib_dict["strFormat"]
                                        control_section_one_findMode = control_section_one_attrib_dict["findMode"]
                                        control_section_one_offset = control_section_one_attrib_dict["offset"]
                                        control_section_one_mark = control_section_one_attrib_dict["mark"]
                                        control_section_one_len = control_section_one_attrib_dict["len"]
                                        control_section_one_decodeType = control_section_one_attrib_dict["decodeType"]
                                        control_section_one_operator = control_section_one_attrib_dict["operator"]
                                        control_section_one_operand = control_section_one_attrib_dict["operand"]

                                        #筛选获取，如果筛选到相应内容，则获取相应内容， 如果没有，则保存
                                        from shucaiyidate.modelsnewdev import ConfigControlSendPorsSection
                                        check_ConfigControlSendPorsSection_list = ConfigControlSendPorsSection.objects.filter(nodeconfig_id=self.case_id).\
                                            filter(configcontrolsendparamid_id=zx_configcontrolsendparamid.id).\
                                            filter(config_control_send_pors_section_findmode=control_section_one_findMode).\
                                            filter(config_control_send_pors_section_offset=control_section_one_offset).\
                                            filter(config_control_send_pors_section_mark=control_section_one_mark)

                                        check_ConfigControlSendPorsSection_list_count = check_ConfigControlSendPorsSection_list.count()

                                        if check_ConfigControlSendPorsSection_list_count == 0:  #说明没有筛选到相应数据，需要将现有数据保存
                                            new_configcontrolsendporssection = ConfigControlSendPorsSection()
                                            new_configcontrolsendporssection.nodeconfig_id = self.case_id
                                            new_configcontrolsendporssection.configcontrolsendparamid_id = zx_configcontrolsendparamid.id
                                            new_configcontrolsendporssection.config_control_send_pors_section_datatype = control_section_one_dataType
                                            new_configcontrolsendporssection.config_control_send_pors_section_strformat = control_section_one_strFormat
                                            new_configcontrolsendporssection.config_control_send_pors_section_findmode = control_section_one_findMode
                                            new_configcontrolsendporssection.config_control_send_pors_section_offset = control_section_one_offset
                                            new_configcontrolsendporssection.config_control_send_pors_section_mark = control_section_one_mark
                                            new_configcontrolsendporssection.config_control_send_pors_section_len = control_section_one_len
                                            new_configcontrolsendporssection.config_control_send_pors_section_decodetype =  control_section_one_decodeType
                                            new_configcontrolsendporssection.config_control_send_pors_section_operator = control_section_one_operator
                                            new_configcontrolsendporssection.config_control_send_pors_section_operand = control_section_one_operand
                                            new_configcontrolsendporssection.save()

                                            zx_configcontrolsendporssection = ConfigControlSendPorsSection.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
                                        else: #否则，说明筛选到数据，获取筛选到的内容
                                            for check_ConfigControlSendPorsSection_one in check_ConfigControlSendPorsSection_list:
                                                time.sleep(1)
                                                zx_configcontrolsendporssection = check_ConfigControlSendPorsSection_one
                                                break  #只获取一条数据


                                        # 获取 反控指令_下发指令_参数_配置_特殊规则 节点内容
                                        control_convertRule_list = control_section_one.findall("convertRule")
                                        control_convertRule_list_len = len(control_convertRule_list)
                                        if control_convertRule_list_len == 0:  #说明没有子节点，不需要保存数据
                                            pass
                                        else:  #否则保存节点数据
                                            for control_convertRule_one in control_convertRule_list:
                                                time.sleep(1)
                                                control_convertRule_one_attrib_dict = control_convertRule_one.attrib  #获取节点属性字典内容\
                                                print("反控指令_下发指令_参数_配置_特殊规则字典属性:")
                                                print(control_convertRule_one_attrib_dict)
                                                control_convertRule_one_ruleType = control_convertRule_one_attrib_dict["ruleType"]
                                                control_convertRule_one_enumValue = control_convertRule_one_attrib_dict["enumValue"]
                                                control_convertRule_one_minValue = control_convertRule_one_attrib_dict["minValue"]
                                                control_convertRule_one_maxValue = control_convertRule_one_attrib_dict["maxValue"]
                                                control_convertRule_one_resultValue = control_convertRule_one_attrib_dict["resultValue"]

                                                #筛选相应内容，如果找到，则获取相应内容，如果未找到，则保存
                                                from shucaiyidate.modelsnewdev import ConfigControlSendPorsConvertrule
                                                check_ConfigControlSendPorsConvertrule_list = ConfigControlSendPorsConvertrule.objects.filter(nodeconfig_id=self.case_id).\
                                                    filter(configcontrolsendporssection_id=zx_configcontrolsendporssection.id).\
                                                    filter(config_control_send_pors_convertrule_ruletype=control_convertRule_one_ruleType).\
                                                    filter(config_control_send_pors_convertrule_enumvalue = control_convertRule_one_enumValue).\
                                                    filter(config_control_send_pors_convertrule_minvalue=control_convertRule_one_minValue).\
                                                    filter(config_control_send_pors_convertrule_maxvalue=control_convertRule_one_maxValue).\
                                                    filter(config_control_send_pors_convertrule_resultvalue=control_convertRule_one_resultValue)

                                                check_ConfigControlSendPorsConvertrule_list_count = check_ConfigControlSendPorsConvertrule_list.count()
                                                if check_ConfigControlSendPorsConvertrule_list_count == 0:  #没有筛选到，需要保存数据
                                                    new_configcontrolsendporsconvertrule = ConfigControlSendPorsConvertrule()
                                                    new_configcontrolsendporsconvertrule.nodeconfig_id = self.case_id
                                                    new_configcontrolsendporsconvertrule.configcontrolsendporssection_id = zx_configcontrolsendporssection.id
                                                    new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_ruletype = control_convertRule_one_ruleType
                                                    new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_enumvalue = control_convertRule_one_enumValue
                                                    new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_minvalue = control_convertRule_one_minValue
                                                    new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_maxvalue = control_convertRule_one_maxValue
                                                    new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_resultvalue = control_convertRule_one_resultValue
                                                    new_configcontrolsendporsconvertrule.save()  # 保存
                                                else:  #否则，不保存
                                                    pass


    #运行主函数,保存dev文件内容到数据库中，使用async_call装饰起一个新线程运行
    @async_call
    def runMain(self):
        self.saveProjectName()
        self.saveVersionFromXml()
        self.saveDeviceFromXml()
        self.saveCollectFromXml()
        self.saveControlFromXml()
        print("异步调用【%s】dev文件内容并入库到ID为【%s】的数据库的函数已经完成"%(str(self.file_path),str(self.case_id)))

#复制生成一条新数据
class CopyNodeConfig(object):
    def __init__(self,request,caseId):
        self.case_id = int(caseId)
        self.request = request
    #复制保存数据
    @async_call
    def saveCopy(self):
        from shucaiyidate.modelsnewdev import User,NodeConfig, ConfigCollectSendCmd, ConfigCollectFactor, \
            ConfigCollectReceivePors, ConfigCollectReceivePorsSection, ConfigCollectReceivePorsConvertrule, \
            ConfigControlSendCmd, ConfigControlSendParamid, ConfigControlSendPorsSection, \
            ConfigControlSendPorsConvertrule

        nodeconfig_id = self.case_id
        nodeconfig_old = NodeConfig.objects.get(id=int(nodeconfig_id))  # 获取用例
        new_nodeconfig = NodeConfig()
        new_nodeconfig.config_project = nodeconfig_old.config_project
        new_nodeconfig.config_version = nodeconfig_old.config_version
        new_nodeconfig.config_device = nodeconfig_old.config_device
        new_nodeconfig.config_collect_packet_len = nodeconfig_old.config_collect_packet_len
        username = self.request.user.username
        user = User.objects.get(username=username)
        new_nodeconfig.write_user_id = user.id   #保存当前用户的user
        new_nodeconfig.save()  # 保存

        # 获取最新的的数据
        zx_nodeconfig = NodeConfig.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的

        # 复制 采集指令_下发指令
        configcollectsendcmd_old_all = ConfigCollectSendCmd.objects.filter(nodeconfig_id=nodeconfig_old.id).order_by(
            "id")
        configcollectsendcmd_old_all_count = configcollectsendcmd_old_all.count()
        if configcollectsendcmd_old_all_count == 0:
            pass
        else:
            for configcollectsendcmd_old_one in configcollectsendcmd_old_all:
                time.sleep(1)
                new_configcollectsendcmd = ConfigCollectSendCmd()
                new_configcollectsendcmd.nodeconfig_id = zx_nodeconfig.id
                new_configcollectsendcmd.config_collect_send_id = configcollectsendcmd_old_one.config_collect_send_id
                new_configcollectsendcmd.config_collect_send_format = configcollectsendcmd_old_one.config_collect_send_format
                new_configcollectsendcmd.config_collect_send_cmd = configcollectsendcmd_old_one.config_collect_send_cmd
                new_configcollectsendcmd.config_collect_send_acktype = configcollectsendcmd_old_one.config_collect_send_acktype
                new_configcollectsendcmd.config_collect_send_ackhead = configcollectsendcmd_old_one.config_collect_send_ackhead
                new_configcollectsendcmd.config_collect_send_acktail = configcollectsendcmd_old_one.config_collect_send_acktail
                new_configcollectsendcmd.config_collect_send_acklen = configcollectsendcmd_old_one.config_collect_send_acklen
                new_configcollectsendcmd.config_collect_send_ackgap = configcollectsendcmd_old_one.config_collect_send_ackgap
                new_configcollectsendcmd.config_collect_send_ackcheckmode = configcollectsendcmd_old_one.config_collect_send_ackcheckmode
                new_configcollectsendcmd.config_collect_send_ackcheckarg = configcollectsendcmd_old_one.config_collect_send_ackcheckarg
                new_configcollectsendcmd.save()

                zx_configcollectsendcmd = ConfigCollectSendCmd.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
                # 复制 采集指令_监测因子
                configcollectfactor_old_all = ConfigCollectFactor.objects.filter(
                    configcollectsendcmd_id=configcollectsendcmd_old_one.id).order_by("id")
                configcollectfactor_old_all_count = configcollectfactor_old_all.count()
                if configcollectfactor_old_all_count == 0:
                    pass
                else:
                    for configcollectfactor_old_one in configcollectfactor_old_all:
                        time.sleep(1)
                        new_configcollectfactor = ConfigCollectFactor()
                        new_configcollectfactor.nodeconfig_id = zx_nodeconfig.id
                        new_configcollectfactor.configcollectsendcmd_id = zx_configcollectsendcmd.id
                        new_configcollectfactor.config_collect_factor_factorcode = configcollectfactor_old_one.config_collect_factor_factorcode
                        new_configcollectfactor.config_collect_factor_findmode = configcollectfactor_old_one.config_collect_factor_findmode
                        new_configcollectfactor.config_collect_factor_offset = configcollectfactor_old_one.config_collect_factor_offset
                        new_configcollectfactor.config_collect_factor_mark = configcollectfactor_old_one.config_collect_factor_mark
                        new_configcollectfactor.config_collect_factor_len = configcollectfactor_old_one.config_collect_factor_len
                        new_configcollectfactor.config_collect_factor_decodetype = configcollectfactor_old_one.config_collect_factor_decodetype
                        new_configcollectfactor.config_collect_factor_operator = configcollectfactor_old_one.config_collect_factor_operator
                        new_configcollectfactor.config_collect_factor_operand = configcollectfactor_old_one.config_collect_factor_operand
                        new_configcollectfactor.save()  # 保存

                # 复制 采集指令_回复指令中的参数或状态
                configcollectreceivepors_old_all = ConfigCollectReceivePors.objects.filter(
                    configcollectsendcmd_id=configcollectsendcmd_old_one.id).order_by("id")
                configcollectreceivepors_old_all_count = configcollectreceivepors_old_all.count()
                if configcollectreceivepors_old_all_count == 0:
                    pass
                else:
                    for configcollectreceivepors_old_one in configcollectreceivepors_old_all:
                        time.sleep(1)
                        new_configcollectreceivepors = ConfigCollectReceivePors()
                        new_configcollectreceivepors.nodeconfig_id = zx_nodeconfig.id
                        new_configcollectreceivepors.configcollectsendcmd_id = zx_configcollectsendcmd.id
                        new_configcollectreceivepors.config_collect_receive_pors_factorcode = configcollectreceivepors_old_one.config_collect_receive_pors_factorcode
                        new_configcollectreceivepors.config_collect_receive_pors_factortype = configcollectreceivepors_old_one.config_collect_receive_pors_factortype
                        new_configcollectreceivepors.save()  # 保存

                        zx_configcollectreceivepors = ConfigCollectReceivePors.objects.all().order_by('-add_time')[:1][
                            0]  # 根据添加时间查询最新的

                        # 复制 采集指令_回复指令中的参数或状态_数据解析配置
                        configcollectreceiveporssection_old_all = ConfigCollectReceivePorsSection.objects.filter(
                            configcollectreceivepors_id=configcollectreceivepors_old_one.id).order_by("id")
                        configcollectreceiveporssection_old_all_count = configcollectreceiveporssection_old_all.count()
                        if configcollectreceiveporssection_old_all_count == 0:
                            pass
                        else:
                            for configcollectreceiveporssection_old_one in configcollectreceiveporssection_old_all:
                                time.sleep(1)
                                new_configcollectreceiveporssection = ConfigCollectReceivePorsSection()
                                new_configcollectreceiveporssection.nodeconfig_id = zx_nodeconfig.id
                                new_configcollectreceiveporssection.configcollectreceivepors_id = zx_configcollectreceivepors.id
                                new_configcollectreceiveporssection.config_collect_receive_pors_section_datatype = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_datatype
                                new_configcollectreceiveporssection.config_collect_receive_pors_section_strformat = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_strformat
                                new_configcollectreceiveporssection.config_collect_receive_pors_section_findmode = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_findmode
                                new_configcollectreceiveporssection.config_collect_receive_pors_section_offset = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_offset
                                new_configcollectreceiveporssection.config_collect_receive_pors_section_mark = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_mark
                                new_configcollectreceiveporssection.config_collect_receive_pors_section_len = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_len
                                new_configcollectreceiveporssection.config_collect_receive_pors_section_decodetype = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_decodetype
                                new_configcollectreceiveporssection.config_collect_receive_pors_section_operator = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_operator
                                new_configcollectreceiveporssection.config_collect_receive_pors_section_operand = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_operand
                                new_configcollectreceiveporssection.save()

                                zx_configcollectreceiveporssection = \
                                ConfigCollectReceivePorsSection.objects.all().order_by('-add_time')[:1][
                                    0]  # 根据添加时间查询最新的

                                # 复制 采集指令_回复指令中的参数或状态_数据解析配置_特殊规则
                                configcollectreceiveporsconvertrule_old_all = ConfigCollectReceivePorsConvertrule.objects.filter(
                                    configcollectreceiveporssection_id=configcollectreceiveporssection_old_one.id).order_by(
                                    "id")
                                configcollectreceiveporsconvertrule_old_all_count = configcollectreceiveporsconvertrule_old_all.count()
                                if configcollectreceiveporsconvertrule_old_all_count == 0:
                                    pass
                                else:
                                    for configcollectreceiveporsconvertrule_old_one in configcollectreceiveporsconvertrule_old_all:
                                        time.sleep(1)
                                        new_configcollectreceiveporsconvertrule = ConfigCollectReceivePorsConvertrule()
                                        new_configcollectreceiveporsconvertrule.nodeconfig_id = zx_nodeconfig.id
                                        new_configcollectreceiveporsconvertrule.configcollectreceiveporssection_id = zx_configcollectreceiveporssection.id
                                        new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_ruletype = configcollectreceiveporsconvertrule_old_one.config_collect_receive_pors_convertrule_ruletype
                                        new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_enumvalue = configcollectreceiveporsconvertrule_old_one.config_collect_receive_pors_convertrule_enumvalue
                                        new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_minvalue = configcollectreceiveporsconvertrule_old_one.config_collect_receive_pors_convertrule_minvalue
                                        new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_maxvalue = configcollectreceiveporsconvertrule_old_one.config_collect_receive_pors_convertrule_maxvalue
                                        new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_resultvalue = configcollectreceiveporsconvertrule_old_one.config_collect_receive_pors_convertrule_resultvalue
                                        new_configcollectreceiveporsconvertrule.save()

        # 复制 反控指令_下发指令
        configcontrolsendcmd_old_all = ConfigControlSendCmd.objects.filter(nodeconfig_id=nodeconfig_old.id).order_by(
            "id")
        configcontrolsendcmd_old_all_count = configcontrolsendcmd_old_all.count()
        if configcontrolsendcmd_old_all_count == 0:
            pass
        else:
            for configcontrolsendcmd_old_one in configcontrolsendcmd_old_all:
                time.sleep(1)
                new_configcontrolsendcmd = ConfigControlSendCmd()
                new_configcontrolsendcmd.nodeconfig_id = zx_nodeconfig.id
                new_configcontrolsendcmd.config_control_send_id = configcontrolsendcmd_old_one.config_control_send_id
                new_configcontrolsendcmd.config_control_send_format = configcontrolsendcmd_old_one.config_control_send_format
                new_configcontrolsendcmd.config_control_send_cmd = configcontrolsendcmd_old_one.config_control_send_cmd
                new_configcontrolsendcmd.config_control_send_acktype = configcontrolsendcmd_old_one.config_control_send_acktype
                new_configcontrolsendcmd.config_control_send_ackhead = configcontrolsendcmd_old_one.config_control_send_ackhead
                new_configcontrolsendcmd.config_control_send_acktail = configcontrolsendcmd_old_one.config_control_send_acktail
                new_configcontrolsendcmd.config_control_send_acklen = configcontrolsendcmd_old_one.config_control_send_acklen
                new_configcontrolsendcmd.config_control_send_ackgap = configcontrolsendcmd_old_one.config_control_send_ackgap
                new_configcontrolsendcmd.config_control_send_ackcheckmode = configcontrolsendcmd_old_one.config_control_send_ackcheckmode
                new_configcontrolsendcmd.config_control_send_ackcheckarg = configcontrolsendcmd_old_one.config_control_send_ackcheckarg
                new_configcontrolsendcmd.save()

                zx_configcontrolsendcmd = ConfigControlSendCmd.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的

                # 复制 反控指令_下发指令_参数
                configcontrolsendparamid_old_all = ConfigControlSendParamid.objects.filter(
                    configcontrolsendcmd_id=configcontrolsendcmd_old_one.id).order_by("id")
                configcontrolsendparamid_old_all_count = configcontrolsendparamid_old_all.count()
                if configcontrolsendparamid_old_all_count == 0:
                    pass
                else:
                    for configcontrolsendparamid_old_one in configcontrolsendparamid_old_all:
                        time.sleep(1)
                        new_configcontrolsendparamid = ConfigControlSendParamid()
                        new_configcontrolsendparamid.nodeconfig_id = zx_nodeconfig.id
                        new_configcontrolsendparamid.configcontrolsendcmd_id = zx_configcontrolsendcmd.id
                        new_configcontrolsendparamid.config_control_send_paramid = configcontrolsendparamid_old_one.config_control_send_paramid
                        new_configcontrolsendparamid.save()

                        zx_configcontrolsendparamid = ConfigControlSendParamid.objects.all().order_by('-add_time')[:1][
                            0]  # 根据添加时间查询最新的

                        # 复制 反控指令_下发指令_参数_配置
                        configcontrolsendporssection_old_all = ConfigControlSendPorsSection.objects.filter(
                            configcontrolsendparamid_id=configcontrolsendparamid_old_one.id).order_by("id")
                        configcontrolsendporssection_old_all_count = configcontrolsendporssection_old_all.count()
                        if configcontrolsendporssection_old_all_count == 0:
                            pass
                        else:
                            for configcontrolsendporssection_old_one in configcontrolsendporssection_old_all:
                                time.sleep(1)
                                new_configcontrolsendporssection = ConfigControlSendPorsSection()
                                new_configcontrolsendporssection.nodeconfig_id = zx_nodeconfig.id
                                new_configcontrolsendporssection.configcontrolsendparamid_id = zx_configcontrolsendparamid.id
                                new_configcontrolsendporssection.config_control_send_pors_section_datatype = configcontrolsendporssection_old_one.config_control_send_pors_section_datatype
                                new_configcontrolsendporssection.config_control_send_pors_section_strformat = configcontrolsendporssection_old_one.config_control_send_pors_section_strformat
                                new_configcontrolsendporssection.config_control_send_pors_section_findmode = configcontrolsendporssection_old_one.config_control_send_pors_section_findmode
                                new_configcontrolsendporssection.config_control_send_pors_section_offset = configcontrolsendporssection_old_one.config_control_send_pors_section_offset
                                new_configcontrolsendporssection.config_control_send_pors_section_mark = configcontrolsendporssection_old_one.config_control_send_pors_section_mark
                                new_configcontrolsendporssection.config_control_send_pors_section_len = configcontrolsendporssection_old_one.config_control_send_pors_section_len
                                new_configcontrolsendporssection.config_control_send_pors_section_decodetype = configcontrolsendporssection_old_one.config_control_send_pors_section_decodetype
                                new_configcontrolsendporssection.config_control_send_pors_section_operator = configcontrolsendporssection_old_one.config_control_send_pors_section_operator
                                new_configcontrolsendporssection.config_control_send_pors_section_operand = configcontrolsendporssection_old_one.config_control_send_pors_section_operand
                                new_configcontrolsendporssection.save()

                                zx_configcontrolsendporssection = \
                                ConfigControlSendPorsSection.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的

                                # 复制 反控指令_下发指令_参数_配置_特殊规则
                                configcontrolsendporsconvertrule_old_all = ConfigControlSendPorsConvertrule.objects.filter(
                                    configcontrolsendporssection_id=configcontrolsendporssection_old_one.id).order_by(
                                    "id")
                                configcontrolsendporsconvertrule_old_all_count = configcontrolsendporsconvertrule_old_all.count()
                                if configcontrolsendporsconvertrule_old_all_count == 0:
                                    pass
                                else:
                                    for configcontrolsendporsconvertrule_old_one in configcontrolsendporsconvertrule_old_all:
                                        time.sleep(1)
                                        new_configcontrolsendporsconvertrule = ConfigControlSendPorsConvertrule()
                                        new_configcontrolsendporsconvertrule.nodeconfig_id = zx_nodeconfig.id
                                        new_configcontrolsendporsconvertrule.configcontrolsendporssection_id = zx_configcontrolsendporssection.id
                                        new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_ruletype = configcontrolsendporsconvertrule_old_one.config_control_send_pors_convertrule_ruletype
                                        new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_enumvalue = configcontrolsendporsconvertrule_old_one.config_control_send_pors_convertrule_enumvalue
                                        new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_minvalue = configcontrolsendporsconvertrule_old_one.config_control_send_pors_convertrule_minvalue
                                        new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_maxvalue = configcontrolsendporsconvertrule_old_one.config_control_send_pors_convertrule_maxvalue
                                        new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_resultvalue = configcontrolsendporsconvertrule_old_one.config_control_send_pors_convertrule_resultvalue
                                        new_configcontrolsendporsconvertrule.save()  # 保存

        print("异步调用复制ID为【%s】的数据生成ID为【%s】的数据完成"%(str(nodeconfig_id),str(zx_nodeconfig.id)))

#删除一条新数据
class DeleteNodeConfig(object):
    def __init__(self,caseId):
        self.case_id = int(caseId)
    #复制保存数据
    # @async_call
    def deleteDate(self):
        from shucaiyidate.modelsnewdev import NodeConfig, ConfigCollectSendCmd, ConfigCollectFactor, \
            ConfigCollectReceivePors, ConfigCollectReceivePorsSection, ConfigCollectReceivePorsConvertrule, \
            ConfigControlSendCmd, ConfigControlSendParamid, ConfigControlSendPorsSection, \
            ConfigControlSendPorsConvertrule


        # 关联之 ConfigCollectReceivePorsConvertrule 去掉依赖
        ConfigCollectReceivePorsConvertrule_all = ConfigCollectReceivePorsConvertrule.objects.filter(
            nodeconfig_id=self.case_id)
        for ConfigCollectReceivePorsConvertrule_one in ConfigCollectReceivePorsConvertrule_all:
            ConfigCollectReceivePorsConvertrule_one.nodeconfig_id = ""  # 置空依赖
            ConfigCollectReceivePorsConvertrule_one.configcollectreceiveporssection_id = ""  # 置空依赖
            ConfigCollectReceivePorsConvertrule_one.delete()  # 删除

        # 关联之 ConfigCollectReceivePorsSection 去掉依赖
        ConfigCollectReceivePorsSection_all = ConfigCollectReceivePorsSection.objects.filter(nodeconfig_id=self.case_id)
        for ConfigCollectReceivePorsSection_one in ConfigCollectReceivePorsSection_all:
            ConfigCollectReceivePorsSection_one.nodeconfig_id = ""  # 置空依赖
            ConfigCollectReceivePorsSection_one.configcollectreceivepors_id = ""  # 置空依赖
            ConfigCollectReceivePorsSection_one.delete()  # 删除

        # 关联之 ConfigCollectReceivePors 去掉依赖
        ConfigCollectReceivePors_all = ConfigCollectReceivePors.objects.filter(nodeconfig_id=self.case_id)
        for ConfigCollectReceivePors_one in ConfigCollectReceivePors_all:
            ConfigCollectReceivePors_one.nodeconfig_id = ""  # 置空依赖
            ConfigCollectReceivePors_one.configcollectsendcmd_id = ""  # 置空依赖
            ConfigCollectReceivePors_one.delete()  # 删除

        # 关联之 ConfigCollectFactor 去掉依赖
        ConfigCollectFactor_all = ConfigCollectFactor.objects.filter(nodeconfig_id=self.case_id)
        for ConfigCollectFactor_one in ConfigCollectFactor_all:
            ConfigCollectFactor_one.nodeconfig_id = ""  # 置空依赖
            ConfigCollectFactor_one.configcollectsendcmd_id = ""  # 置空依赖
            ConfigCollectFactor_one.delete()  # 删除

        # 关联之 ConfigCollectSendCmd 去掉依赖
        ConfigCollectSendCmd_all = ConfigCollectSendCmd.objects.filter(nodeconfig_id=self.case_id)
        for ConfigCollectSendCmd_one in ConfigCollectSendCmd_all:
            ConfigCollectSendCmd_one.nodeconfig_id = ""  # 置空依赖
            ConfigCollectSendCmd_one.delete()  # 删除

        # 关联之 ConfigControlSendPorsConvertrule 去掉依赖
        ConfigControlSendPorsConvertrule_all = ConfigControlSendPorsConvertrule.objects.filter(nodeconfig_id=self.case_id)
        for ConfigControlSendPorsConvertrule_one in ConfigControlSendPorsConvertrule_all:
            ConfigControlSendPorsConvertrule_one.nodeconfig_id = ""  # 置空依赖
            ConfigControlSendPorsConvertrule_one.configcontrolsendporssection_id = ""  # 置空依赖
            ConfigControlSendPorsConvertrule_one.delete()  # 删除

        # 关联之 ConfigControlSendPorsSection 去掉依赖
        ConfigControlSendPorsSection_all = ConfigControlSendPorsSection.objects.filter(nodeconfig_id=self.case_id)
        for ConfigControlSendPorsSection_one in ConfigControlSendPorsSection_all:
            ConfigControlSendPorsSection_one.nodeconfig_id = ""  # 置空依赖
            ConfigControlSendPorsSection_one.configcontrolsendparamid_id = ""  # 置空依赖
            ConfigControlSendPorsSection_one.delete()  # 删除

        # 关联之 ConfigControlSendParamid 去掉依赖
        ConfigControlSendParamid_all = ConfigControlSendParamid.objects.filter(nodeconfig_id=self.case_id)
        for ConfigControlSendParamid_one in ConfigControlSendParamid_all:
            ConfigControlSendParamid_one.nodeconfig_id = ""  # 置空依赖
            ConfigControlSendParamid_one.configcontrolsendcmd_id = ""  # 置空依赖
            ConfigControlSendParamid_one.delete()  # 删除

        # 关联之 ConfigControlSendCmd 去掉依赖
        ConfigControlSendCmd_all = ConfigControlSendCmd.objects.filter(nodeconfig_id=self.case_id)
        for ConfigControlSendCmd_one in ConfigControlSendCmd_all:
            ConfigControlSendCmd_one.nodeconfig_id = ""
            ConfigControlSendCmd_one.delete()  # 删除

        # 再删除本体
        qs_one = NodeConfig.objects.get(id=self.case_id)
        qs_one.delete()

        print("同步调用删除ID为【%s】的数据完成"%(str(self.case_id)))



if __name__ == '__main__':
    # mn = MakeNodeConfig(1)
    # mn.makeDev()
    # fileName = "test.dev"
    fileName = "D:\pycharmproject\shangbaogongju\media/Dev/2_哈希分析仪/哈希分析仪.dev"
    # fileName = r"D:\pycharmproject\shangbaogongju\WWQRSTest\util\autoXml\instr_1972_N.dev"


    rn = ReadNodeConfig(fileName,3)
    # # rn.readFile()
    # # rn.splitPathFile()
    rn.saveVersionFromXml()
    rn.saveDeviceFromXml()
    rn.saveCollectFromXml()
    rn.saveControlFromXml()







































