import json
import socket
import sys



if __name__=="__main__":

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect(("192.168.8.205", 57001))

    #2061数据
    data_2062 = "##0677ST=21;CN=2061;PW=123456;MN=chang000003;CP=&&DataTime=20200109090000;w01001-Avg=8.437,w01001-Cou=5711.829,w01001-Max=15.996,w01001-Min=1.014;w01006-Avg=4958.334,w01006-Cou=3356792.219,w01006-Max=9977.125,w01006-Min=2.722;w01010-Avg=4986.002,w01010-Cou=3375523.127,w01010-Max=9998.616,w01010-Min=22.339;w01014-Avg=4977.767,w01014-Cou=3369948.511,w01014-Max=9991.611,w01014-Min=10.638;w21003-Avg=1.544,w21003-Cou=1045.241,w21003-Max=3.000,w21003-Min=0.019;w21011-Avg=0.507,w21011-Cou=343.524,w21011-Max=0.997,w21011-Min=0.000;w01019-Avg=8.534,w01019-Cou=5777.551,w01019-Max=15.982,w01019-Min=1.066;w01003-Avg=5106.176,w01003-Cou=3456880.823,w01003-Max=9992.920,w01003-Min=28.406&&6300"
    # luan = bytes(srr,encoding='utf-8')
    luan =data_2062.encode('utf-8')
    print(type(luan))
    print(luan)
    s.send(luan)
    print(s.recv(1024))

    # #乱码
    # srr = "毄夝叅?毄塕ich毄?                       PE  L 鴌G        ?  `  @      ?      p   @                     ?    ?                               d` (    ? "
    # # luan = bytes(srr,encoding='utf-8')
    # luan =srr.encode('utf-8')
    # print(type(luan))
    # print(luan)
    # s.send(luan)
    # print(s.recv(1024))

    # s.send(b'##0321ST=32;CN=2011;PW=123456;MN=DM000001;CP=&&DataTime=20191223165100;w01001-Rtd=15.294,w01001-Flag=N;w01006-Rtd=12.122,w01006-Flag=N;w01010-Rtd=21.639,w01010-Flag=N;w01014-Rtd=92.088,w01014-Flag=N;w21003-Rtd=78.741,w21003-Flag=N;w21011-Rtd=92.488,w21011-Flag=N;w01019-Rtd=51.248,w01019-Flag=N;w01003-Rtd=3.262,w01003-Flag=N&&A141\r\n') # 前面为十六进制数据，后面可接字符串等正文
    # #全包
    # s.send(b'##0888ST=32;CN=2011;PW=123456;MN=DM000001;CP=&&DataTime=20191223165100;w01001-Rtd=15.294,w01001-Flag=N;w01006-Rtd=12.122,w01006-Flag=N;w01010-Rtd=21.639,w01010-Flag=N;w01014-Rtd=92.088,w01014-Flag=N;w21003-Rtd=78.741,w21003-Flag=N;w21011-Rtd=92.488,w21011-Flag=N;w01019-Rtd=51.248,w01019-Flag=N;w01003-Rtd=3.262,w01003-Flag=N&&A141\r\n') # 前面为十六进制数据，后面可接字符串等正文
    # print(s.recv(1024))

    # #断保  断保1
    # d1 = b'##0888ST=32;CN=2011;PW=123456;MN=DM000001;CP=&&DataTime=20191223165100;w01001-Rtd=15.294,w01001-Flag=N;w01006-Rtd=12.122,w01006-Flag=N;'
    # s.send(d1)  # 前面为十六进制数据，后面可接字符串等正文
    # print(s.recv(1024))
    # # 断保  断保2
    # d2 = b'w01010-Rtd=21.639,w01010-Flag=N;w01014-Rtd=92.088,w01014-Flag=N;w21003-Rtd=78.741,w21003-Flag=N;w21011-Rtd=92.488,w21011-Flag=N;w01019-Rtd=51.248,w01019-Flag=N;w01003-Rtd=3.262,w01003-Flag=N&&A141\r\n'
    # s.send(d2)  # 前面为十六进制数据，后面可接字符串等正文
    # print(s.recv(1024))
    # # 分包 分包1
    # bao1 = b'##0270ST=21;CN=2011;PW=123456;MN=DM000001;PNO=1;PNUM=2;CP=&&DataTime=20191225155200;w01001-Rtd=91.980,w01001-Flag=N;w01006-Rtd=21.130,w01006-Flag=N;w01010-Rtd=61.970,w01010-Flag=N;w01014-Rtd=38.450,w01014-Flag=N;w21003-Rtd=56.427,w21003-Flag=N;w21011-Rtd=2.497,w21011-Flag=N&&F9C1'
    # s.send(bao1)
    # print(s.recv(1024))
    # # 分包 分包2
    # bao2 = b'##0143ST=21;CN=2011;PW=123456;MN=DM000001;PNO=2;PNUM=2;CP=&&DataTime=20191225155200;w01019-Rtd=91.579,w01019-Flag=N;w01003-Rtd=48.624,w01003-Flag=N&&9301'
    # s.send(bao2)
    # print(s.recv(1024))

    s.close()