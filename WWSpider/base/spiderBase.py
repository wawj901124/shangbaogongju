url = "http://fpie1.com/#/play-details/78"

from WWTest.base.activeBrowser import ActiveBrowser


class SpiderBase
ab = ActiveBrowser()
ab.getUrl(url)
ab.delayTime(2)
#定位到frame
frame_xpath = "/html/body/div/div[2]/div[1]/div[2]/p[2]/iframe"
frame_obj = ab.findELe("xpath",frame_xpath )
video_url = frame_obj.get_attribute("src")
print(video_url)

down_load = ab.findEleAndReturnText(0,"xpath","/html/body/div/div[2]/div[1]/div[2]/p[4]/span")
print(down_load)


# ab.getUrl(video_url)
front_cover_img = ab.getScreenshotAboutMySQL()
# print(front_cover_img)

ab.driver.switch_to.frame(frame_obj)
print("切换到frame")

front_cover_img = ab.findELe("xpath","/html/body/div/div/div[7]")
video_url = front_cover_img.get_attribute("style").split('"')[1]
print(video_url)
import requests
imagewe = requests.get(video_url)
image_content = imagewe.content
print(image_content)
imageend = ab.saveSpiderImage()
with open(imageend,'wb') as f:
    f.write(image_content)
print("封面图：%s"% imageend)