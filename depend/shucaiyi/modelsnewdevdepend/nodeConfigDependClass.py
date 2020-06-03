# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from xml.etree import ElementTree as ET


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
            return file_content
        else:
            print("没有找到caseId：%s 对应的数据，请查看是否存在相应的数据!!!" % self.case_id)
            return ""

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

class ReadXml(object):
    def __init__(self,fileName):
        self.file_name = fileName



class ReadNodeConfig(object):
    def __init__(self,filePath,caseId):
        self.file_path = filePath
        self.content_list = self.readFile()
        self.case_id = caseId
        self.node_config = self.createDB()
        self.xml_tree = self.readXml()
        self.xml_root = self.getRootFromXml()

    #读取文件,并一行为单位项，返回一个列表
    def readFile(self):
        with open(self.file_path,"r") as f:
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
        nodeconfig = NodeConfig.objects.get(id=int(self.case_id))
        return nodeconfig

    def readXml(self):
        xml_tree = ET.parse(self.file_path)
        print(xml_tree)
        return xml_tree

    def getRootFromXml(self):
        xml_root = self.xml_tree.getroot()
        return xml_root

    def getVersionFromXml(self):
        version_node = self.xml_root.getiterator("version")
        version_content = version_node.text
        print(version_content)
        return version_content



    def saveVersion(self):
        pass




if __name__ == '__main__':
    # mn = MakeNodeConfig(1)
    # mn.makeDev()
    # fileName = "test.dev"
    fileName = "D:\pycharmproject\shangbaogongju\media/Dev/2_哈希分析仪/哈希分析仪.dev"
    # fileName = r"D:\pycharmproject\shangbaogongju\WWQRSTest\util\autoXml\instr_1972_N.dev"

    # import chardet
    # with open(fileName, "rb",encoding="utf8") as f:
    #
    #     data = f.read()
    #
    # res = chardet.detect(data)
    # print(res["encoding"])
    #
    # rn = ReadNodeConfig(fileName,1)
    # # # rn.readFile()
    # # # rn.splitPathFile()
    # rn.getVersionFromXml()







































