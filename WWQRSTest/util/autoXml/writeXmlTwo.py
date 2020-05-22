from xml.dom import minidom

# mydata_list = [{'TagName': 'version', 'TagText': 'v20200513', 'TagAttrib': {}, 'TagChildren': []}, {'TagName': 'deviceModel', 'TagText': '1972 德林COD', 'TagAttrib': {}, 'TagChildren': []}, {'TagName': 'collectCmds', 'TagText': '\n\t\t', 'TagAttrib': {'ackPacketMaxLen': ''}, 'TagChildren': [{'TagName': 'cmd', 'TagText': '\n\t\t\t', 'TagAttrib': {'id': 'rtdCollect', 'format': 'HEX', 'cmd': '${ID}0400000048${MODBUS_L_CRC16}', 'ackType': 'HEAD_LEN', 'ackHead': '${ID}04', 'ackTail': '', 'ackLen': '149', 'ackGap': '', 'ackCheckMode': 'MODBUS_L_CRC16', 'ackCheckArg': ''}, 'TagChildren': [{'TagName': 'pollutantFactor', 'TagText': '\n\t\t\t\t', 'TagAttrib': {}, 'TagChildren': [{'TagName': 'factor', 'TagText': None, 'TagAttrib': {'factorCode': 'w01018', 'findMode': 'OFFSET', 'offset': '5', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'stateFactor', 'TagText': '\n\t\t\t\t', 'TagAttrib': {}, 'TagChildren': [{'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i12090', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'FLOAT', 'strFormat': '%.3f', 'findMode': 'OFFSET', 'offset': '9', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i12001', 'factorType': 'STATE'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t\t', 'TagAttrib': {'dataType': 'INT', 'strFormat': '%02d', 'findMode': 'OFFSET', 'offset': '39', 'mark': '', 'len': '2', 'decodeType': 'decode7', 'operator': '*', 'operand': '1'}, 'TagChildren': [{'TagName': 'convertRule', 'TagText': None, 'TagAttrib': {'ruleType': '1', 'enumValue': '1', 'minValue': '', 'maxValue': '', 'resultValue': '9'}, 'TagChildren': []}, {'TagName': 'convertRule', 'TagText': None, 'TagAttrib': {'ruleType': '1', 'enumValue': '2', 'minValue': '', 'maxValue': '', 'resultValue': '3'}, 'TagChildren': []}, {'TagName': 'convertRule', 'TagText': None, 'TagAttrib': {'ruleType': '1', 'enumValue': '4', 'minValue': '', 'maxValue': '', 'resultValue': '7'}, 'TagChildren': []}, {'TagName': 'convertRule', 'TagText': None, 'TagAttrib': {'ruleType': '1', 'enumValue': '5', 'minValue': '', 'maxValue': '', 'resultValue': '1'}, 'TagChildren': []}, {'TagName': 'convertRule', 'TagText': None, 'TagAttrib': {'ruleType': '1', 'enumValue': '6', 'minValue': '', 'maxValue': '', 'resultValue': '2'}, 'TagChildren': []}, {'TagName': 'convertRule', 'TagText': None, 'TagAttrib': {'ruleType': '1', 'enumValue': '7', 'minValue': '', 'maxValue': '', 'resultValue': '8'}, 'TagChildren': []}]}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i13008', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'FLOAT', 'strFormat': '%.3f', 'findMode': 'OFFSET', 'offset': '87', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i13007', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'FLOAT', 'strFormat': '%.3f', 'findMode': 'OFFSET', 'offset': '91', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i15009', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'FLOAT', 'strFormat': '%.3f', 'findMode': 'OFFSET', 'offset': '95', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i15010', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'FLOAT', 'strFormat': '%.3f', 'findMode': 'OFFSET', 'offset': '99', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i13005', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'INT', 'strFormat': '%02d', 'findMode': 'OFFSET', 'offset': '103', 'mark': '', 'len': '2', 'decodeType': 'decode7', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i13004', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'FLOAT', 'strFormat': '%.3f', 'findMode': 'OFFSET', 'offset': '105', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i15013', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'FLOAT', 'strFormat': '%.3f', 'findMode': 'OFFSET', 'offset': '117', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i15014', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'FLOAT', 'strFormat': '%.3f', 'findMode': 'OFFSET', 'offset': '121', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i15015', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'FLOAT', 'strFormat': '%.3f', 'findMode': 'OFFSET', 'offset': '125', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}, {'TagName': 'factor', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'factorCode': 'i15016', 'factorType': 'PARAM'}, 'TagChildren': [{'TagName': 'section', 'TagText': '\n\t\t\t\t\t', 'TagAttrib': {'dataType': 'FLOAT', 'strFormat': '%.3f', 'findMode': 'OFFSET', 'offset': '129', 'mark': '', 'len': '4', 'decodeType': 'decode2', 'operator': '*', 'operand': '1'}, 'TagChildren': []}]}]}]}]}, {'TagName': 'controlCmds', 'TagText': '\t\n\t\t', 'TagAttrib': {}, 'TagChildren': [{'TagName': 'cmd', 'TagText': '\n\t\t', 'TagAttrib': {'id': 'startTest', 'format': 'HEX', 'cmd': '${ID}0600000001${MODBUS_L_CRC16}', 'ackType': 'NO_ACK', 'ackHead': '', 'ackTail': '', 'ackLen': '', 'ackGap': '', 'ackCheckMode': '', 'ackCheckArg': ''}, 'TagChildren': []}, {'TagName': 'cmd', 'TagText': '\n\t\t', 'TagAttrib': {'id': 'autoCorrection', 'format': 'HEX', 'cmd': '${ID}0600080001${MODBUS_L_CRC16}', 'ackType': 'NO_ACK', 'ackHead': '', 'ackTail': '', 'ackLen': '', 'ackGap': '', 'ackCheckMode': '', 'ackCheckArg': ''}, 'TagChildren': []}]}]
# mydata_list= [
#  {
#   "TagName": "version",
#   "TagText": "v20200513",
#   "TagAttrib": {},
#   "TagChildren": []
#  },
#  {
#   "TagName": "deviceModel",
#   "TagText": "1972 \u5fb7\u6797COD",
#   "TagAttrib": {},
#   "TagChildren": []
#  },
#  {
#   "TagName": "collectCmds",
#   "TagText": "\n\t\t",
#   "TagAttrib": {
#    "ackPacketMaxLen": ""
#   },
#   "TagChildren": [
#    {
#     "TagName": "cmd",
#     "TagText": "\n\t\t\t",
#     "TagAttrib": {
#      "id": "rtdCollect",
#      "format": "HEX",
#      "cmd": "${ID}0400000048${MODBUS_L_CRC16}",
#      "ackType": "HEAD_LEN",
#      "ackHead": "${ID}04",
#      "ackTail": "",
#      "ackLen": "149",
#      "ackGap": "",
#      "ackCheckMode": "MODBUS_L_CRC16",
#      "ackCheckArg": ""
#     },
#     "TagChildren": [
#      {
#       "TagName": "pollutantFactor",
#       "TagText": "\n\t\t\t\t",
#       "TagAttrib": {},
#       "TagChildren": [
#        {
#         "TagName": "factor",
#         "TagText": null,
#         "TagAttrib": {
#          "factorCode": "w01018",
#          "findMode": "OFFSET",
#          "offset": "5",
#          "mark": "",
#          "len": "4",
#          "decodeType": "decode2",
#          "operator": "*",
#          "operand": "1"
#         },
#         "TagChildren": []
#        }
#       ]
#      },
#      {
#       "TagName": "stateFactor",
#       "TagText": "\n\t\t\t\t",
#       "TagAttrib": {},
#       "TagChildren": [
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i12090",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "FLOAT",
#            "strFormat": "%.3f",
#            "findMode": "OFFSET",
#            "offset": "9",
#            "mark": "",
#            "len": "4",
#            "decodeType": "decode2",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i12001",
#          "factorType": "STATE"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "INT",
#            "strFormat": "%02d",
#            "findMode": "OFFSET",
#            "offset": "39",
#            "mark": "",
#            "len": "2",
#            "decodeType": "decode7",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": [
#            {
#             "TagName": "convertRule",
#             "TagText": null,
#             "TagAttrib": {
#              "ruleType": "1",
#              "enumValue": "1",
#              "minValue": "",
#              "maxValue": "",
#              "resultValue": "9"
#             },
#             "TagChildren": []
#            },
#            {
#             "TagName": "convertRule",
#             "TagText": null,
#             "TagAttrib": {
#              "ruleType": "1",
#              "enumValue": "2",
#              "minValue": "",
#              "maxValue": "",
#              "resultValue": "3"
#             },
#             "TagChildren": []
#            },
#            {
#             "TagName": "convertRule",
#             "TagText": null,
#             "TagAttrib": {
#              "ruleType": "1",
#              "enumValue": "4",
#              "minValue": "",
#              "maxValue": "",
#              "resultValue": "7"
#             },
#             "TagChildren": []
#            },
#            {
#             "TagName": "convertRule",
#             "TagText": null,
#             "TagAttrib": {
#              "ruleType": "1",
#              "enumValue": "5",
#              "minValue": "",
#              "maxValue": "",
#              "resultValue": "1"
#             },
#             "TagChildren": []
#            },
#            {
#             "TagName": "convertRule",
#             "TagText": null,
#             "TagAttrib": {
#              "ruleType": "1",
#              "enumValue": "6",
#              "minValue": "",
#              "maxValue": "",
#              "resultValue": "2"
#             },
#             "TagChildren": []
#            },
#            {
#             "TagName": "convertRule",
#             "TagText": null,
#             "TagAttrib": {
#              "ruleType": "1",
#              "enumValue": "7",
#              "minValue": "",
#              "maxValue": "",
#              "resultValue": "8"
#             },
#             "TagChildren": []
#            }
#           ]
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i13008",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "FLOAT",
#            "strFormat": "%.3f",
#            "findMode": "OFFSET",
#            "offset": "87",
#            "mark": "",
#            "len": "4",
#            "decodeType": "decode2",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i13007",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "FLOAT",
#            "strFormat": "%.3f",
#            "findMode": "OFFSET",
#            "offset": "91",
#            "mark": "",
#            "len": "4",
#            "decodeType": "decode2",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i15009",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "FLOAT",
#            "strFormat": "%.3f",
#            "findMode": "OFFSET",
#            "offset": "95",
#            "mark": "",
#            "len": "4",
#            "decodeType": "decode2",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i15010",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "FLOAT",
#            "strFormat": "%.3f",
#            "findMode": "OFFSET",
#            "offset": "99",
#            "mark": "",
#            "len": "4",
#            "decodeType": "decode2",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i13005",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "INT",
#            "strFormat": "%02d",
#            "findMode": "OFFSET",
#            "offset": "103",
#            "mark": "",
#            "len": "2",
#            "decodeType": "decode7",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i13004",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "FLOAT",
#            "strFormat": "%.3f",
#            "findMode": "OFFSET",
#            "offset": "105",
#            "mark": "",
#            "len": "4",
#            "decodeType": "decode2",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i15013",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "FLOAT",
#            "strFormat": "%.3f",
#            "findMode": "OFFSET",
#            "offset": "117",
#            "mark": "",
#            "len": "4",
#            "decodeType": "decode2",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i15014",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "FLOAT",
#            "strFormat": "%.3f",
#            "findMode": "OFFSET",
#            "offset": "121",
#            "mark": "",
#            "len": "4",
#            "decodeType": "decode2",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i15015",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "FLOAT",
#            "strFormat": "%.3f",
#            "findMode": "OFFSET",
#            "offset": "125",
#            "mark": "",
#            "len": "4",
#            "decodeType": "decode2",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        },
#        {
#         "TagName": "factor",
#         "TagText": "\n\t\t\t\t\t",
#         "TagAttrib": {
#          "factorCode": "i15016",
#          "factorType": "PARAM"
#         },
#         "TagChildren": [
#          {
#           "TagName": "section",
#           "TagText": "\n\t\t\t\t\t",
#           "TagAttrib": {
#            "dataType": "FLOAT",
#            "strFormat": "%.3f",
#            "findMode": "OFFSET",
#            "offset": "129",
#            "mark": "",
#            "len": "4",
#            "decodeType": "decode2",
#            "operator": "*",
#            "operand": "1"
#           },
#           "TagChildren": []
#          }
#         ]
#        }
#       ]
#      }
#     ]
#    }
#   ]
#  },
#  {
#   "TagName": "controlCmds",
#   "TagText": "\t\n\t\t",
#   "TagAttrib": {},
#   "TagChildren": [
#    {
#     "TagName": "cmd",
#     "TagText": "\n\t\t",
#     "TagAttrib": {
#      "id": "startTest",
#      "format": "HEX",
#      "cmd": "${ID}0600000001${MODBUS_L_CRC16}",
#      "ackType": "NO_ACK",
#      "ackHead": "",
#      "ackTail": "",
#      "ackLen": "",
#      "ackGap": "",
#      "ackCheckMode": "",
#      "ackCheckArg": ""
#     },
#     "TagChildren": []
#    },
#    {
#     "TagName": "cmd",
#     "TagText": "\n\t\t",
#     "TagAttrib": {
#      "id": "autoCorrection",
#      "format": "HEX",
#      "cmd": "${ID}0600080001${MODBUS_L_CRC16}",
#      "ackType": "NO_ACK",
#      "ackHead": "",
#      "ackTail": "",
#      "ackLen": "",
#      "ackGap": "",
#      "ackCheckMode": "",
#      "ackCheckArg": ""
#     },
#     "TagChildren": []
#    }
#   ]
#  }
# ]


from WWQRSTest.util.autoXml.autoXml import AutoXml
filename = "instr_1972_N.dev"
ax = AutoXml(filename)
mydata_list = ax.redXml()
print("+++++++++++++++++++++++++已经获取数据++++++++++++++++++++++++++++++++++++")

def writeXml(doc,rootElement,data_list):
    rootElement = rootElement
    mydata_list = data_list

    #为根元素添加添加子元素
    for mydate_one_dict in mydata_list:
        tag_name = mydate_one_dict["TagName"]
        print("tag_name")
        print(tag_name)
        # 创建子元素
        childElement = doc.createElement(tag_name)

        #创建子元素的节点文本内容
        tag_text = mydate_one_dict["TagText"]
        print("tag_text")
        print(tag_text)
        if tag_text != None:
            childElementText = doc.createTextNode(tag_text)
            childElement.appendChild(childElementText)

        tag_attrib_dict = mydate_one_dict["TagAttrib"]
        print(tag_attrib_dict)
        if tag_attrib_dict != {}:
            for key,value in tag_attrib_dict.items():
                # 为子元素添加id属性
                childElement.setAttribute(key, value)

        child_list = mydate_one_dict["TagChildren"]
        print("child_list:")
        print(child_list)
        if child_list != []:
            doc=doc
            rootElement= childElement
            data_list = child_list
            writeXml(doc, rootElement, data_list)
        else:
            child_list

        # 将子元素追加到根元素中
        rootElement.appendChild(childElement)
        # print(childElement.firstChild.data)

        # 将拼接好的根元素追加到dom对象
        doc.appendChild(rootElement)



# 生成XML文件方式
def generateXml():
    impl = minidom.getDOMImplementation()

    # 创建一个xml dom
    # 三个参数分别对应为 ：namespaceURI, qualifiedName, doctype
    doc = impl.createDocument(None, None, None)

    # 创建根元素
    rootElement = doc.createElement('root')
    doc=doc
    rootElement=rootElement
    data_list = mydata_list

    writeXml(doc, rootElement, data_list)
    print("*******************************")
    print(doc)
    print("*******************************")

    # 打开test.xml文件 准备写入
    f = open('test.dev', 'w',encoding='utf-8')
    # 写入文件
    doc.writexml(f, addindent=' ', newl='\n')
    # 关闭
    f.close()


# 执行生成xml方法
generateXml()