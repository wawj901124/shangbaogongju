from requests_html import HTMLSession

url="https://www.baidu.com/"

headers={
"Host": "www.baidu.com",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

}

session=HTMLSession()
req=session.get(url,headers=headers)
req.encoding="utf-8"

req.html.render()
result=req.html.find("a.mnav",first=True)
print(req.status_code)
print(result.text)
print(result.attrs.get('href'))