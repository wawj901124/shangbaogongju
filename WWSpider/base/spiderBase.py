

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
        print("封面图：%s" % imageend)

        #将封面图地址修改为数据库可识别的地址
        imageend_list_two = imageend.split("media")[1]
        imgae_sql_path ="/media%s"%imageend_list_two
        print("入库地址：%s"% imgae_sql_path)
        return imgae_sql_path




if __name__ == "__main__":
    url = "http://fpie1.com/#/play-details/78"
    sb = SpiderBase(weburl=url)
    #打开网址
    sb.get_web_url()
    #获取视频链接
    video_url = sb.get_video_url()
    #获取下载地址
    down_load = sb.get_down_load()
    #获取封面图
    front_cover_img = sb.get_front_cover_img()

    


