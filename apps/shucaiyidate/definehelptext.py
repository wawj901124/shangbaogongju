from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码

class DefineHelpText(object):

    html_tou = """
                        <!DOCTYPE html> 
                        <html> 
                            <head> 
                                <meta charset="utf-8" /> 
                                <title>html边框虚线演示</title> 
                                <style> 
                                    .tabledata{
	                                    background: rgba(251, 251, 251, 0.93);
	                                    margin: 0;  /* 上 右 下 左 */
	                                    border:1px solid #F00;
	                                    }
	                                .tabledataxuxian{
	                                    background: rgba(251, 251, 251, 0.93);
	                                    margin: 0;  /* 上 右 下 左 */
	                                    border:1px dashed #F00;
	                                    }
                                </style> 
                            </head> 
                            <body> 
    """

    html_wei = """
                                </body> 
                        </html>
    """

    #采集指令-下发指令_下发指令类型
    config_collect_send_format_help_text = mark_safe(html_tou+"""

                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">指令类型</th>
                                        <th class="tabledataxuxian">类型说明</th>
                                        <th class="tabledataxuxian">备注</th>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">HEX</td>
                                        <td class="tabledataxuxian">十六进制格式</td>
                                        <td class="tabledataxuxian">报文以HEX的形式发送</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">ASCII</td>
                                        <td class="tabledataxuxian">字符串格式</td>
                                        <td class="tabledataxuxian">报文以ASCII的形式发送</td>
                                    </tr>
                                </table> 

    """ + html_wei)

    config_collect_send_cmd_help_text = mark_safe(html_tou+"""
                                <span>具体下发指令，例如：\"${ID}0375320002${MODBUS_L_CRC16}\" ,其中中间部分指令内容0375320002根据需求而得</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">指令内容</th>
                                        <th class="tabledataxuxian">含义说明</th>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${ID}</td>
                                        <td class="tabledataxuxian">用宏表示设备ID，表示ID可以在别处配置；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">03</td>
                                        <td class="tabledataxuxian">表示功能码，和需求说明的功能码一致；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">7532</td>
                                        <td class="tabledataxuxian">表示寄存器起始地址，和需求说明的寄存器起始地址一致；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">0002</td>
                                        <td class="tabledataxuxian">表示寄存器个数或长度，和需求说明的寄存器个数或长度一致；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${MODBUS_L_CRC16}</td>
                                        <td class="tabledataxuxian">表示下发指令的CRC校验方式；</td>
                                    </tr>
                                </table> 
                                
                                <span>\"${}\" 为一项宏，可选宏如下表：</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">宏名称</th>
                                        <th class="tabledataxuxian">宏描述</th>
                                        <th class="tabledataxuxian">备注</th>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${ID}</td>
                                        <td class="tabledataxuxian">设备ID，该字段取值为串口设备配置中的id配置中下划线之后的内容；</td>
                                        <td class="tabledataxuxian">配置时直接写${ID}即可；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${CR}</td>
                                        <td class="tabledataxuxian">回车，会在指令会用’\r’替换该宏；</td>
                                        <td class="tabledataxuxian">直接配置${CR}；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${LF}</td>
                                        <td class="tabledataxuxian">换行，会在指令会用’\n’替换该宏；</td>
                                        <td class="tabledataxuxian">直接配置${LF}，通常联合回车一起使用；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${MODBUS_L_CRC16}</td>
                                        <td class="tabledataxuxian">Modbus crc16位校验，低字节在前，用校验结果替换宏；</td>
                                        <td class="tabledataxuxian">指令中直接写${MODBUS_L_CRC16}；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${MODBUS_H_CRC16}</td>
                                        <td class="tabledataxuxian">Modbus crc16位校验，高字节在前，用校验结果替换宏；</td>
                                        <td class="tabledataxuxian">指令中直接写${MODBUS_H_CRC16}；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${HJ212_CRC}</td>
                                        <td class="tabledataxuxian">HJ212国标校验，用校验结果替换宏；</td>
                                        <td class="tabledataxuxian">指令中直接写${ HJ212_CRC }；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${HJ212_JG_CRC}</td>
                                        <td class="tabledataxuxian">聚光校验，用校验结果替换宏；</td>
                                        <td class="tabledataxuxian">指令中直接写${ HJ212_JG_CRC }；</td>
                                    </tr>
                                </table> 

    """ + html_wei)

    config_collect_send_acktype_help_text = mark_safe(html_tou + """
                                <span>数据的回复类型，根据下发指令格式确定报文的类型，可选值如下表：</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">名称</th>
                                        <th class="tabledataxuxian">描述</th>
                                        <th class="tabledataxuxian">备注</th>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">R_NO_RULE</td>
                                        <td class="tabledataxuxian">没有规则：取走buffer中已存在的所有数据；</td>
                                        <td class="tabledataxuxian">该规则代表的是前端仪器回复的数据包的类型；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">R_HEAD_TAIL</td>
                                        <td class="tabledataxuxian">满足指定包头和包尾的数据帧；</td>
                                        <td class="tabledataxuxian">该规则代表的是前端仪器回复的数据包的类型；</td>
                                    
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">R_HEAD_LEN</td>
                                        <td class="tabledataxuxian">满足指定包头和长度的数据帧；</td>
                                        <td class="tabledataxuxian">该规则代表的是前端仪器回复的数据包的类型；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">R_LEN_ONLY</td>
                                        <td class="tabledataxuxian">满足指定长度的数据帧；</td>
                                        <td class="tabledataxuxian">该规则代表的是前端仪器回复的数据包的类型；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">R_TAIL_ONLY</td>
                                        <td class="tabledataxuxian">满足指定包尾的数据帧；</td>
                                        <td class="tabledataxuxian">该规则代表的是前端仪器回复的数据包的类型；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">R_CUSTOM_RULE</td>
                                        <td class="tabledataxuxian">满足指定包尾的数据帧；</td>
                                        <td class="tabledataxuxian">该规则代表的是前端仪器回复的数据包的类型；</td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">R_TAIL_ONLY</td>
                                        <td class="tabledataxuxian">定制规则，由上层定义匹配函数matchFunc；</td>
                                        <td class="tabledataxuxian">定制规则目前不支持；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">NO_ACK</td>
                                        <td class="tabledataxuxian">不需要回复；</td>
                                        <td class="tabledataxuxian">该规则下，不处理串口数据，一般用在反控中；</td>
                                    </tr>
                                </table> 
                                <span>说明:带有R的，例如R_NO_RULE使用时常可以去掉R，比如R_NO_RULE，则可以为NO_RULE；</span>
    """ + html_wei)

    config_collect_send_ackcheckmode_help_text = mark_safe(html_tou + """
                                <span>回复报文的检验，用来判断报文的正确性，可选项如下表：</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">名称</th>
                                        <th class="tabledataxuxian">描述</th>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">MODBUS_L_CRC16</td>
                                        <td class="tabledataxuxian">Modbus crc16位校验，低字节在前；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">MODBUS_H_CRC16</td>
                                        <td class="tabledataxuxian">Modbus crc16位校验，高字节在前；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">FIXED_MARK</td>
                                        <td class="tabledataxuxian">固定标识，会在报文中查找固定的标识，固定标识配置在校验参数(ackCheckArg)中；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">HJ212_CRC</td>
                                        <td class="tabledataxuxian">国标CRC校验；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">HJ212_JG_CRC</td>
                                        <td class="tabledataxuxian">聚光CRC检验；</td>
                                    </tr>
                                </table> 

    """ + html_wei)

    #采集指令-监测因子
    config_collect_factor_findmode_help_text = mark_safe(html_tou + """
                                <span>查找模式，有以下选项：</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">名称</th>
                                        <th class="tabledataxuxian">描述</th>                                        
                                        <th class="tabledataxuxian">备注</th>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">OFFSET</td>
                                        <td class="tabledataxuxian">固定偏移；</td>
                                        <td class="tabledataxuxian">相对包头的偏移量；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">MARK</td>
                                        <td class="tabledataxuxian">固定标识；</td>
                                         <td class="tabledataxuxian">所有的固定标识不能有包含与被包含的关系，否则没法解析；</td>
                                    </tr>
                                </table> 

    """ + html_wei)

    config_collect_factor_decodetype_help_text = mark_safe(html_tou + """
                                <span>数据解析算法，有时须与解析宽度配合使用，有以下选项：</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">算法代码</th>
                                        <th class="tabledataxuxian">算法描述</th>                                        
                                        <th class="tabledataxuxian">举例</th>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode1</td>
                                        <td class="tabledataxuxian">将IEEE745格式的四字节数据(小端)转换成一个float型数值4321；</td>
                                        <td class="tabledataxuxian">4855D045-》45D05548->6666.66；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode2</td>
                                        <td class="tabledataxuxian">将IEEE745格式的四字节数据(大端)转换成一个float型数值1234；</td>
                                         <td class="tabledataxuxian">45D05548-》45D05548->6666.66；</td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode3</td>
                                        <td class="tabledataxuxian">将IEEE745格式的四字节数据(小端)转换成一个float型数值2143；</td>
                                        <td class="tabledataxuxian">D0454855-》45D05548->6666.66；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode4</td>
                                        <td class="tabledataxuxian">将IEEE745格式的四字节数据(大端)转换成一个float型数值3412；</td>
                                         <td class="tabledataxuxian">554845D0-》45D05548->6666.66；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode5</td>
                                        <td class="tabledataxuxian">字符串转换成浮点数；</td>
                                        <td class="tabledataxuxian">“12345.3”-》 12345.3；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode6</td>
                                        <td class="tabledataxuxian">字符串转换成整形转换宽度由上面len决定,如len=2；</td>
                                         <td class="tabledataxuxian">len=2 &nbsp; “12345.63”-》 12</br>len=7 &nbsp; “12345.63”-》 12345</td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode7@字节序</br>不传递字节序时，默认为12</td>
                                        <td class="tabledataxuxian">
                                            字符数组转换成短整型</br>
                                            decode7、decode7@12、decode7@21等算法默认解析出的结果是有符号数</br>
                                            如果现场特殊，需要解析无符号数，可按照如下方式配置：decode7@u12、decode7@u21;
                                        </td>
                                        <td class="tabledataxuxian">
                                            规则：decode7@12</br>
                                            源字节数组(HEX)：31 32</br>
                                            解析结果：12594；
                                        </td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode8</td>
                                        <td class="tabledataxuxian">将一个字符的十六进制直接转换成对应的十进制；</td>
                                         <td class="tabledataxuxian">0x0a-》10；</td>
                                    </tr>
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode9@bitn</br>n为比特位数</td>
                                        <td class="tabledataxuxian">
                                            取对应字节的比特位，返回0或者1<br/>
                                            @后面为参数格式为：@bitn<br/>
                                            支持解析多位比特位，格式为：<br/>
                                            decode9@bitEnd-bitStart,比如 decode9@bit1-bit0 
                                        </td>
                                        <td class="tabledataxuxian">
                                            例 1： <br/>
                                                deocde9@bit3 <br/>
                                                0x04-》1 <br/>
                                                0x03-》0 <br/>
                                            例 2: <br/>
                                                decode9@bit1-bit0 <br/>
                                                0x01-》1 <br/>
                                                0x02-》2 <br/>
                                        </td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">
                                            decode10  @字节序 <br/>
                                            不传递字节序时，默认为 1234 
                                        </td>
                                        <td class="tabledataxuxian">将十六进制字符串直接转换成4字节浮点数（可配置顺序）；</td>
                                         <td class="tabledataxuxian">
                                            规则：decode10@1234 <br/>
                                            源字符串(ASCII)： <br/>
                                            449a4000 <br/>
                                            解析结果：1234.0 <br/>
                                         </td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">
                                            decode11 @字节序 <br/>
                                            不传递字节序时，默认为 12
                                        </td>
                                        <td class="tabledataxuxian">将十六进制字符串直接转换成2字节短整型（可配置顺序）；</td>
                                        <td class="tabledataxuxian">
                                            规则：decode11@12 <br/>
                                            源字符串(ASCII)：449a <br/>
                                            解析结果：17562 <br/>
                                        </td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">
                                            decode12 @字节序 <br/>
                                            不传递字节序时，默认为 1234 
                                        </td>
                                        <td class="tabledataxuxian">将IEEF745格式的4字节数据转成一个float型数值（可配置顺序）；</td>
                                        <td class="tabledataxuxian">
                                            规则：decode12@4312 <br/>
                                            源字节数组（HEX）：40 00 9a 44 <br/>
                                            解析结果：1234.0
                                        </td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">
                                            decode13@u 字节序 <br/> 
                                            decode13@s 字节序
                                        </td>
                                        <td class="tabledataxuxian">
                                            16 进制字节数组转化为 4 字节整型数据；<br/>
                                            u 代表无符号数；<br/>
                                            s 代表有符号数；<br/>
                                            注：配置时必须指明符号类型，如果不明确是什么符号类型，请使用 s ；
                                        </td>
                                        <td class="tabledataxuxian"> 
                                                例 1： 规则：decode13@u1234 ，源字节数组（HEX）：45 1C 30 2F ，解析结果：1159475247（即45 1C 30 2F-》451C302F->1159475247）；<br/>
                                                例 2： 规则：decode13@s3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果:-245 （即ff 0b ff ff-》FFFFFF0B->-245）；<br/>
                                                例 3： 规则：decode13@u3412 ，源字节数组（HEX）：ff 0b ff ff ，解析结果: 4294967051（即ff 0b ff ff-》FFFFFF0B->4294967051；<br/>
                                                注：对比例 2 和例 3 可观察有符号和无符号的解析差别；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">
                                            decode14@u 字节序 <br/>
                                            decode14@s 字节序
                                        </td>
                                        <td class="tabledataxuxian">
                                            16 进制字节数组转化为 4 字节整型数据；<br/>
                                            u 代表无符号数；<br/>
                                            s 代表有符号数；<br/>
                                            注：配置时必须指明符号类型，如果不明确是什么符号类型，请使用 s ；</td>
                                         <td class="tabledataxuxian">                                                
                                                例 1： 规则：decode14@u1234 ，源字节数组（ASCII）：45 1C 30 2F ，解析结果：1159475247（即45 1C 30 2F-》451C302F->1159475247）；<br/>
                                                例 2： 规则：decode14@s3412 ，源字节数组（ASCII）：ff 0b ff ff ，解析结果:-245 （即ff 0b ff ff-》FFFFFF0B->-245）；<br/>
                                                例 3： 规则：decode14@u3412 ，源字节数组（ASCII）：ff 0b ff ff ，解析结果: 4294967051（即ff 0b ff ff-》FFFFFF0B->4294967051；<br/>
                                                注：对比例 2 和例 3 可观察有符号和无符号的解析差别；</td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode15@字节序</td>
                                        <td class="tabledataxuxian">
                                            16 进制字节数组转化为 8 字节有符号浮点数<br/>
                                            注意： <br/>
                                            1、本算法针对 linux 版本为 3.2.0及其以上版本，
                                                涉及的产品包括动态管控仪及其衍生产品（数采
                                                仪 6.0、用电量数采仪…..）。 <br/>
                                            2、如果是 linux 版本为 2.6.0（新国标版本）， 
                                                字 节 序 相 对linux3.2.0来说需前后4字节整体对调。 
                                                例如:<br/>
                                                 linux3.2.0: decode15@12345678 等价于 linux2.6.0: decode15@56781234 
                                        </td>
                                        <td class="tabledataxuxian">
                                            例 1： 规则：decode15@12345678 ，源字节数组（HEX）： 40aa4875c28f5c29 ，解析结果：3364.23（即40aa4875c28f5c29-》40AA4875C28F5C29->3364.23）<br/>
                                            注意： <br/>
                                                linux3.2.0: decode15@12345678 等价于 linux2.6.0: decode15@56781234 
                                        </td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode16</td>
                                        <td class="tabledataxuxian">16 进制字节数组转化为 16 进制字符串对应的浮点数；</td>
                                        <td class="tabledataxuxian">
                                            例 1： 规则：decode16 ，源字节数组（HEX）： 12 34 56 78 ，解析结果：12345678.0（即12 34 56 78-》12345678.0）；
                                        </td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode17@ 010203040506 </td>
                                        <td class="tabledataxuxian">
                                            16 进制字节数组按权重累加,@符号后传递的是指数，默认底数是 10。指数是 16 进制的，20 表示 32 <br/>
                                            decode17@010203040506070F 代表 <br/>
                                                x1*10 的 1 次方 + <br/>
                                                x2*10 的 2 次方 + <br/>
                                                x3*10 的 3 次方 + <br/>
                                                x4*10 的 4 次方 + <br/>
                                                x5*10 的 5 次方 + <br/>
                                                x6*10 的 6 次方 + <br/>
                                                x7*10 的 15 次方 <br/>
                                            decode17@-1-2-3-4-5-a 代表 <br/>
                                                x1*10 的 1 次方 + <br/>
                                                x2*10 的 2 次方 + <br/>
                                                x3*10 的 3 次方 + <br/>
                                                x4*10 的 4 次方 + <br/>
                                                x5*10 的 5 次方 + <br/>
                                                x6*10 的 6 次方 + <br/>
                                                x7*10 的 10 次方 <br/>
                                            正数指数范围是 00 到 FF <br/>
                                            负数指数范围是-0 到-F <br/>

                                        </td>
                                        <td class="tabledataxuxian">
                                            例 1： <br/>
                                                规则：decode17@01020304 <br/>
                                                源字节数组（HEX）： 04 03 02 01 <br/>
                                                解析结果：12340.0 <br/>
                                            例 2： <br/>
                                                规则：decode17@-1-2-3-4 <br/>
                                                源字节数组（HEX）： 04 03 02 01 <br/>
                                                解析结果：0.432100 <br/>
                                        </td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode18</td>
                                        <td class="tabledataxuxian">
                                            16 进制 3 字节数组转化为 16 进制字符串对应的 float 浮点数,小数点位置从报文读取 <br/>
                                            第 1 字节标识小数点位置 第 2、3 字节标识有效数据 <br/>
                                            第 1 字节的第 1 位为整数的符号位 <br/>
                                            第 1 字节的第 2 位为小数点位，表示向左右移几位 <br/>
                                        </td>
                                        <td class="tabledataxuxian">
                                            例 1： <br/>
                                                规则：decode18 <br/>
                                                源字节数组（HEX）： 03 45 24 <br/>
                                                解析结果：452.4.0 <br/>
                                            例 2： <br/>
                                                规则：decode18 <br/>
                                                源字节数组（HEX）： 7E 45 24 <br/>
                                                解析结果：0. 004524 <br/>
                                        </td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode19</td>
                                        <td class="tabledataxuxian">
                                            整数部分为16进制4字节数整形数据(字节序 1234), <br/>
                                            小数部分为16 进制 4 字节浮点型数据（字节序 1234） <br/>
                                        </td>
                                        <td class="tabledataxuxian">
                                            例 1： 
                                                规则：decode19 
                                                源字节数组（HEX）： 00 00 49 1D 3C DE 5A 17 
                                                解析结果：18717.027143
                                        </td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode20</td>
                                        <td class="tabledataxuxian">
                                            16 进制 4 字节数组按权重累加，底数固定为 10， <br/>
                                            Decode20 <br/>
                                            源字节数组（HEX） X1 X2 X3 X4 <br/>
                                            结果=X1 * 10^0 + X2*10^2 + X3*10^4 + X4 * 10 ^6 <br/>
                                        </td>
                                        <td class="tabledataxuxian">
                                            例 1： <br/>
                                                规则：decode20 <br/>
                                                源字节数组(HEX) 00 02 00 01 <br/>
                                                解析结果： 1000200 <br/>
                                        </td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode21@/1000 </td>
                                        <td class="tabledataxuxian">
                                            16 进制 8 字节数组,前部分为 4字节整形数据（字节序 3412）加上后部分为四字节整形数据（字节序 3412） / （可配置为加减乘除）1000（可配置参数）的数值。 <br/>
                                            decode21 不传任何参数和运算符，<br/>
                                            或者传递的运算符非以上四种，<br/>
                                            默认为解析结果为两个四字节整数相加，<br/>
                                            如果要除以的参数为 0 时，默认为后半部分为 0，得到的结果是前四字节整数数据，<br/>
                                            如果传递的参数为非数字，默认参数为 0，按以上规则进行运算 <br/>
                                        </td>
                                        <td class="tabledataxuxian">
                                            例 1： <br/>
                                                规则：decode21@/1000 <br/>
                                                源字节数组： <br/>
                                                    00 02 00 01 02 40 00 00 <br/>
                                                    00 02 00 01:65538 <br/>
                                                    02 40 00 00:576 <br/>
                                                参数：1000 <br/>
                                                解析结果： 65538.576 <br/>
                                        </td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode22@H/100</td>
                                        <td class="tabledataxuxian">
                                            16 机制 2 字节数组，大写 H 代表解析数据 12，大写 L 解析顺序21， /表示操作符，也可以是+， -，*。 <br/>
                                            100 表示要操作的参数，大写 H不写按照解析顺序 12 数据进行解析，<br/>
                                            操作符不写，默认得到的数据为 2 字节解析得到的数值，<br/>
                                            注意：如果除以的参数为 0，则得到的数据默认为 0 <br/>
                                        </td>
                                        <td class="tabledataxuxian">
                                            例：
                                                decode22@H/100 <br/>
                                                源字节数组： 01 72 <br/>
                                                    按照的解析顺序 12 得到的数值为 370； <br/>
                                                最终得到的数值为 370/100 = 3.7 <br/>
                                        </td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">
                                            decode23@字节序;ADMin,ADMax;rangMin,rangeMax
                                        </td>
                                        <td class="tabledataxuxian">
                                            2 字节整型数据表示 ADC 值， 根据量程上下限进行计算出实时数据：<br/>
                                                参数格式： <br/>
                                                    docode23@字节序; ADMin,ADMax; rangeMin,rangeMax  <br/>
                                        </td>
                                        <td class="tabledataxuxian">
                                            例如：  <br/>
                                                decode23@12;0,65535;100,200  <br/>
                                                源字节数组 10 20 <br/>
                                                解析结果：106.2989  <br/>
                                                解析结果公式：Y=（（rangeMax-rangeMin）*（X-ADMin））/(ADMax-ADMin)+rangeMin <br/>
                                                其中X为（10 20 按照字节序12解析出的整数：1020-》4128） <br/>
                                                Y = （（200-100）*（4128-0））/(65535-0)+100=412800/65535+100=106.2989242389563 <br/>
                                        </td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">
                                            decode24@字节序;ADMin,ADMax;rangMin,rangeMax
                                        </td>
                                        <td class="tabledataxuxian">
                                            4 字节浮点数据表示 ADC 值， 根据量程上下限进行计算出实时数据： <br/>
                                                参数格式： <br/>
                                                    Decode24@字节序;ADMin,ADMax;rangeMin,rangeMax <br/>
                                        </td>
                                        <td class="tabledataxuxian">
                                            例如： <br/>
                                                decode24@3412;0,40;0,4000 <br/>
                                                源字节数组 00 00 41 a0 <br/>
                                                解析结果：2000.0 <br/>
                                                解析结果公式：Y=（（rangeMax-rangeMin）*（X-ADMin））/(ADMax-ADMin)+rangeMin <br/>
                                                其中X为（ 00 00 41 a0 按照字节序3412解析出的整数：00 00 41 a0-》 41 a0 00 00 ->20.000000） <br/>
                                                Y = （（4000-0）*（20-0））/(40-0)+0=80000/40+0=2000 <br/>
                                        </td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">decode25@ 010203040506 </td>
                                        <td class="tabledataxuxian">
                                            16进制字节数组对应的1字节字符串按权重累加,@符号后传递的是指数，默认底数是 10。指数是 16 进制的，20 表示 32 <br/>
                                            decode25@010203040506070F 代表 <br/>
                                                x1*10 的 1 次方 + <br/>
                                                x2*10 的 2 次方 + <br/>
                                                x3*10 的 3 次方 + <br/>
                                                x4*10 的 4 次方 + <br/>
                                                x5*10 的 5 次方 + <br/>
                                                x6*10 的 6 次方 + <br/>
                                                x7*10 的 15 次方 <br/>
                                            decode17@-1-2-3-4-5-a 代表 <br/>
                                                x1*10 的 1 次方 + <br/>
                                                x2*10 的 2 次方 + <br/>
                                                x3*10 的 3 次方 + <br/>
                                                x4*10 的 4 次方 + <br/>
                                                x5*10 的 5 次方 + <br/>
                                                x6*10 的 6 次方 + <br/>
                                                x7*10 的 10 次方 <br/>
 
                                            正数指数范围是 00 到 FF <br/>
                                            负数指数范围是-0 到-F <br/>

                                        </td>
                                        <td class="tabledataxuxian">
                                            例 1： <br/>
                                                规则：decode25@01020304 <br/>
                                                源字节数组（HEX）： 04 03 02 01 <br/>
                                                解析结果：12340.0 <br/>
 
                                            例 2： <br/>
                                                规则：decode25@000A0B0C <br/>
                                                源字节数组（HEX）： 10 20 30 40 <br/>
                                                解析结果： 43200000000010.000000 <br/>
 
                                            例 3： <br/>
                                                规则：decode25@-1-2-3-4 <br/>
                                                源字节数组（HEX）： 10 20 30 40 <br/>
                                                解析结果： 1.234000 <br/>
                                        </td>
                                    </tr>
                                    
                                </table> 
                                <span>注意：该算法由算法库提供，当有不满足时，可适当进行扩展。</span>

    """ + html_wei)

    # 采集指令_回复指令中的参数或状态
    config_collect_receive_pors_factortype_help_text = mark_safe(html_tou + """
                                <span>参数或者状态类型，可选项如下：</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">类型</th>
                                        <th class="tabledataxuxian">描述</th>                                        
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">STATE</td>
                                        <td class="tabledataxuxian">状态因子；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">PARAM</td>
                                        <td class="tabledataxuxian">参数因子；</td>
                                    </tr>
                                </table> 

    """ + html_wei)

    #采集指令_回复指令中的参数或状态_数据解析配置
    config_collect_receive_pors_section_datatype_help_text = mark_safe(html_tou + """
                                <span>数据类型，不写默认为INT,可选选项如下：</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">类型</th>
                                        <th class="tabledataxuxian">描述</th>                                        
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">INT</td>
                                        <td class="tabledataxuxian">将解析到的值以整形的形式存储成字符串；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">FLOAT</td>
                                        <td class="tabledataxuxian">将解析到的值以浮点数的形式存储成字符串；</td>
                                    </tr>
                                </table> 
    """ + html_wei)

    config_collect_receive_pors_section_findmode_help_text = config_collect_factor_findmode_help_text
    config_collect_receive_pors_section_decodetype_help_text = config_collect_factor_decodetype_help_text
    config_collect_receive_pors_section_strformat_help_text = mark_safe(html_tou + """
                                                    为空时默认为'%d'或'%f',
                                                    <br/>具体根据dataType（数据类型）决定，
                                                    <br/>数据类型为INT时，则为'%d'；
                                                    <br/>数据类型为FLOAT时，则为'%f'。
                                                    <br/>注意：</br>
                                                    1.对于时间的数据是整形时，需要加字节个数的限制，如%02d（限制2个字节）或%04d（限制4个字节） ,如果没有加限制，时间格式会出现数字不够的现象，例如：7月1号展示为71 ，但正确需展示应为0701；<br/>
                                                    2.对于非时间的数据是整形时，一般不需要加字节个数的限制，否则会出现数据不对应的问题,例如： 2500 如果是%02d限制后为25，数据错误；</br>    
    """+ html_wei)

    #采集指令_回复指令中的参数或状态_数据解析配置_特殊规则
    config_collect_receive_pors_convertrule_ruletype_help_text = mark_safe(html_tou + """
                                <span>特殊规则类型，需要增加时以convertRule为单位进行增加，可增加多行，选择相应的类型时，对应的值才有意义，可选类型如下：</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">类型</th>
                                        <th class="tabledataxuxian">描述</th>                                        
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">1</td>
                                        <td class="tabledataxuxian">枚举类型；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">2</td>
                                        <td class="tabledataxuxian">小于最小值；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">3</td>
                                        <td class="tabledataxuxian">大于最大值；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">4</td>
                                        <td class="tabledataxuxian">最大值最小值之间；</td>
                                    </tr>
                                </table> 
                                <span>注意：当配置多个特殊转换规则时，只要有满足的规则，之后的规则将不再判断，无特殊配置直接去掉convertRule节点。</span>

    """ + html_wei)

    #反控指令_下发指令
    config_control_send_id_help_text = mark_safe(html_tou + """
                                <span>反控指令的ID，可取值如下表：</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">反控指令ID</th>
                                        <th class="tabledataxuxian">反控指令名称</th>                                           
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">zeroAndFull</td>
                                        <td class="tabledataxuxian">校零校满；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">adjustTime</td>
                                        <td class="tabledataxuxian">校时；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">immediateSample</td>
                                        <td class="tabledataxuxian">及时采样；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">remoteQualityCtrl</td>
                                        <td class="tabledataxuxian">远程质控；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">startTest</td>
                                        <td class="tabledataxuxian">仪器启动测试；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">stopTest</td>
                                        <td class="tabledataxuxian">仪器停止测试；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">autoCorrection</td>
                                        <td class="tabledataxuxian">仪器自动校准；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">init</td>
                                        <td class="tabledataxuxian">仪器初始化；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">checkStdSample</td>
                                        <td class="tabledataxuxian">仪器进行标样核查；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">setMeasureMode</td>
                                        <td class="tabledataxuxian">仪器修改测量模式；</td>
                                    </tr>

                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">setMeasureInterval</td>
                                        <td class="tabledataxuxian">仪器修改周期测量间隔；</td>
                                    </tr>
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">setAutoCorrectInterval</td>
                                        <td class="tabledataxuxian">仪器修改自动校准间隔；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">setCheckStdSampleInterval</td>
                                        <td class="tabledataxuxian">仪器修改自动标样核查间隔；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">setOneLevelPasswd</td>
                                        <td class="tabledataxuxian">修改一级密码；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">setTwoLevelPasswd</td>
                                        <td class="tabledataxuxian">修改二级密码；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">setThreeLevelPasswd</td>
                                        <td class="tabledataxuxian">修改三级密码；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">zeroCorrectRange</td>
                                        <td class="tabledataxuxian">零点校准量程校准；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">startClean</td>
                                        <td class="tabledataxuxian">启动清洗/反吹；</td>
                                    </tr>

                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">compareSample</td>
                                        <td class="tabledataxuxian">比对采样；</td>
                                    </tr>
                                    
                                     <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">overproofSample</td>
                                        <td class="tabledataxuxian">超标留样；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">setSampleCycle</td>
                                        <td class="tabledataxuxian">设置采样时间周期；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">getSampleCycle</td>
                                        <td class="tabledataxuxian">提取采样时间周期；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">getLastSampleTime</td>
                                        <td class="tabledataxuxian">提取出样时间；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">getEquipmentId</td>
                                        <td class="tabledataxuxian">提取设备唯一标识；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">getEquipmentTime</td>
                                        <td class="tabledataxuxian">提取现场机时间；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">setEquipmentTime</td>
                                        <td class="tabledataxuxian">设置现场机时间；</td>
                                    </tr>
                                    
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">setEquipmentParam</td>
                                        <td class="tabledataxuxian">设置现场机参数；</td>
                                    </tr>
                                    
                                </table> 
                                <span>注意：反控指令中的ID不能为空。</span>

    """ + html_wei)
    config_control_send_format_help_text = config_collect_send_format_help_text

    config_control_send_cmd_help_text = mark_safe(html_tou+"""
                                <span>具体下发指令，例如：\"${ID}050001FF00@{SYSTEMTIME}${MODBUS_L_CRC16}\" ,其中中间部分指令内容050001FF00@{SYSTEMTIME}根据需求而得</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">指令内容</th>
                                        <th class="tabledataxuxian">含义说明</th>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${ID}</td>
                                        <td class="tabledataxuxian">用宏表示设备ID，表示ID可以在别处配置；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">05</td>
                                        <td class="tabledataxuxian">表示功能码，和需求说明的功能码一致；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">0001</td>
                                        <td class="tabledataxuxian">表示寄存器起始地址，和需求说明的寄存器起始地址一致；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">FF00</td>
                                        <td class="tabledataxuxian">表示寄存器个数或长度，和需求说明的寄存器个数或长度一致；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">@{SYSTEMTIME}</td>
                                        <td class="tabledataxuxian">@{参数名}为参数，该参数的值来源于上报程序，具体的处理方法见反控指令中的参数配置；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${MODBUS_L_CRC16}</td>
                                        <td class="tabledataxuxian">表示下发指令的CRC校验方式；</td>
                                    </tr>
                                </table> 
                                
                                <span>\"${}\" 为一项宏，可选宏如下表：</span>
                                <table class="tabledata"> 
                                    <tr class="tabledataxuxian">
                                        <th class="tabledataxuxian">宏名称</th>
                                        <th class="tabledataxuxian">宏描述</th>
                                        <th class="tabledataxuxian">备注</th>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${ID}</td>
                                        <td class="tabledataxuxian">设备ID，该字段取值为串口设备配置中的id配置中下划线之后的内容；</td>
                                        <td class="tabledataxuxian">配置时直接写${ID}即可；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${CR}</td>
                                        <td class="tabledataxuxian">回车，会在指令会用’\r’替换该宏；</td>
                                        <td class="tabledataxuxian">直接配置${CR}；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${LF}</td>
                                        <td class="tabledataxuxian">换行，会在指令会用’\n’替换该宏；</td>
                                        <td class="tabledataxuxian">直接配置${LF}，通常联合回车一起使用；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${MODBUS_L_CRC16}</td>
                                        <td class="tabledataxuxian">Modbus crc16位校验，低字节在前，用校验结果替换宏；</td>
                                        <td class="tabledataxuxian">指令中直接写${MODBUS_L_CRC16}；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${MODBUS_H_CRC16}</td>
                                        <td class="tabledataxuxian">Modbus crc16位校验，高字节在前，用校验结果替换宏；</td>
                                        <td class="tabledataxuxian">指令中直接写${MODBUS_H_CRC16}；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${HJ212_CRC}</td>
                                        <td class="tabledataxuxian">HJ212国标校验，用校验结果替换宏；</td>
                                        <td class="tabledataxuxian">指令中直接写${ HJ212_CRC }；</td>
                                    </tr>
                                    <tr class="tabledataxuxian">
                                        <td class="tabledataxuxian">${HJ212_JG_CRC}</td>
                                        <td class="tabledataxuxian">聚光校验，用校验结果替换宏；</td>
                                        <td class="tabledataxuxian">指令中直接写${ HJ212_JG_CRC }；</td>
                                    </tr>
                                </table> 

    """ + html_wei)
    config_control_send_acktype_help_text = config_collect_send_acktype_help_text
    config_control_send_ackcheckmode__help_text = config_collect_send_ackcheckmode_help_text

    #反控指令_下发指令_参数_配置
    config_control_send_pors_section_datatype_help_text = config_collect_receive_pors_section_datatype_help_text
    config_control_send_pors_section_findmode_help_text = config_collect_receive_pors_section_findmode_help_text
    config_control_send_pors_section_decodetype_help_text = config_collect_receive_pors_section_decodetype_help_text
    config_control_send_pors_section_strformat_help_text = config_collect_receive_pors_section_strformat_help_text

    # 反控指令_下发指令_参数_配置_特殊规则
    config_control_send_pors_convertrule_ruletype_help_text = config_collect_receive_pors_convertrule_ruletype_help_text


definehelptext = DefineHelpText()