import urllib,urllib.request,sys
import urllib.parse
import re
import base64

def IdentificationVerificationCode(picture,v_type):
    #验证码转换为Base64编码
    f=open(picture,"rb")#转为二进制格式
    base64_date = base64.b64encode(f.read())#用b64encode方法进行转换
    base64_code = str(base64_date) #将转换后的结果转换成字符格式
    base64_code=base64_code.replace("b'","data:image/png;base64,") #字符替换
    base64_code=base64_code.replace("'","") #字符替换
    host = 'http://apigateway.jianjiaoshuju.com'
    path = '/api/v_1/yzm.html'
    method = 'POST'
    appcode = '1B48580DD49186A16A7AAD863BF1B25B'
    appKey = 'AKIDb9a59d11da2ccd70268e7b2011de5ea6'
    appSecret = 'c495b93cc1395c62812830d526a412a2'
    querys = ''
    bodys = {}
    url = host + path
    bodys['v_pic'] =base64_code
    bodys['v_type'] =v_type
    post_data =  urllib.parse.urlencode(bodys).encode("utf-8")
    request = urllib.request.Request(url, post_data)
    request.add_header('appcode', appcode)
    request.add_header('appKey', appKey)
    request.add_header('appSecret', appSecret)
    #根据API的要求，定义相对应的Content-Type
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    result = str(content)
    #返回数据的格式b'{"msg":"\xe6\x9f\xa5\xe8\xaf\xa2\xe6\x88\x90\xe5\x8a\x9f!","v_code":"7377","errCode":0,"v_type":"n4"}'
    #其中"v_code":"7377"是我们需要的验证码字段
    w1 = '"v_code":"'
    w2 = '"'
    pat = re.compile(w1+'(.*?)'+w2,re.S)
    result = str(pat.findall(result)) #输出结果是['7377']格式的
    result=result.replace("['","") #把两边的东西替换掉
    result=result.replace("']","")
    return result

if __name__ == "__main__":
    picture = r"/root/PycharmProjects/wanwenyc/WWTest/util/timg.jpg"
    ivc = IdentificationVerificationCode(picture,"n4")
    print("ivc:%s"%ivc)