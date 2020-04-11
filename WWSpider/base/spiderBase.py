import unittest
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from WWTest.base.activeBrowser import ActiveBrowser


class SpiderBase(object):
    def __init__(self,weburl):
        self.ab = ActiveBrowser()
        self.web_url = weburl

    def get_web_url(self):
        self.ab.getUrl(self.web_url)
        self.ab.delayTime(2)

    #获取iframe
    def get_iframe(self):
        #定位到iframe获取其src属性内容即视频链接
        # 定位到frame
        frame_xpath = "/html/body/div/div[2]/div[1]/div[2]/p[2]/iframe"
        frame_obj = self.ab.findELe("xpath", frame_xpath)
        return frame_obj

    #获取视频链接
    def get_video_url(self):
        frame_obj = self.get_iframe()
        video_url = frame_obj.get_attribute("src")
        print(video_url)
        return video_url

    #获取下载地址链接
    def get_down_load(self):
        down_load = self.ab.findEleAndReturnText(0, "xpath", "/html/body/div/div[2]/div[1]/div[2]/p[4]/span")
        print(down_load)
        return down_load

    #获取封面图片
    def get_front_cover_img(self):
        self.ab.driver.switch_to.frame(self.get_iframe())
        print("切换到frame")

        front_cover_img = self.ab.findELe("xpath", "/html/body/div/div/div[7]")
        video_url = front_cover_img.get_attribute("style").split('"')[1]
        print(video_url)
        import requests
        imagewe = requests.get(video_url)
        image_content = imagewe.content
        print(image_content)
        imageend = self.ab.saveSpiderImage()
        with open(imageend, 'wb') as f:
            f.write(image_content)
        imageend_list = imageend.split("media")
        from wanwenyc.settings import DJANGO_SERVER_YUMING
        image_xpath = "%s/media%s"%(DJANGO_SERVER_YUMING,imageend_list[1])
        print("封面图：%s" % image_xpath)

        return image_xpath




if __name__ == "__main__":
    error_url_list=[]
    for i in range(78,79):
        try:
            url = "http://fpie1.com/#/play-details/%s"% i
            sb = SpiderBase(weburl=url)
            #打开网址
            sb.get_web_url()
            #获取视频链接
            video_url = sb.get_video_url()
            #获取下载地址
            down_load = sb.get_down_load()
            #获取封面图
            front_cover_img = sb.get_front_cover_img()

            from spiderdata.models import SpiderDate

            spiderdata = SpiderDate()
            spiderdata.splider_url = url
            spiderdata.front_cover_img = front_cover_img
            spiderdata.video = video_url
            spiderdata.down_load = down_load
            is_exist_url_count = SpiderDate.objects.filter(splider_url=url).count()
            print(is_exist_url_count)
            if is_exist_url_count==0:
                spiderdata.save()
            else:
                print("已经爬取过网站：%s" % url)
        except:
            error_url_list.append(url)

    print("失败网址：")
    print(error_url_list)




