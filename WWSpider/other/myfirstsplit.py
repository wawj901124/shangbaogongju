# import requests
# import json
#
# url = "http://fpie1.com/#/play-details/78"
# rese = requests.get(url)
# retext = rese.text
# print(retext)
# html = json.loads(retext)
# print(html)
# from requests_html import HTMLSession
#
# session = HTMLSession()
#
# rese = session.get(url)
# retext = rese.text
# print(retext)
# print(rese.links)

from WWTest.base.activeBrowser import ActiveBrowser

ab = ActiveBrowser()
ab.getUrl(url)
text = ab.findEleAndReturnText(0,"xpath","/html/body/div/div[2]/div[1]/div[2]/p[4]/span")
print(text)
