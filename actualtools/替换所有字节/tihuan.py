pre = '                <input id="tcp_server_port" name="tcp_server_port" type="text" value="{{ xieyiconfigdateorderform.tcp_server_port|default:""  }}"/>'

b="xieyiconfigdateorderform.tcp_server_port"
c= "xieyiconfigdateorderform.tcp_server_port.value"
d = pre.replace(b,c)
print(pre)
print(d)