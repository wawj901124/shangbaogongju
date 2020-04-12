
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

    #进入URL
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

        img = rese.html.find("a.bigImage img",
                             first=True)  # 获取类名为bigImage的a标签下的img标签 ，返回符合条件的第一项，如果first=False，则返回所有符合的集合

        front_cover_img = self.ab.findELe("xpath", "/html/body/div[5]/div[1]/div[1]/a/img")
        img_url = front_cover_img.get_attribute("src")
        print(img_url)
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


    #获取标题
    def get_splider_title(self):
        splider_title = self.ab.findEleAndReturnText(0, "xpath", "/html/body/div[5]/h3")
        print(splider_title)
        return splider_title

    #获取编号
    def get_prenum(self):
        prenum = self.ab.findEleAndReturnText(0, "xpath", "/html/body/div[5]/h3")
        prenum_end = prenum.split(" ")[0]
        print(prenum_end)
        return prenum_end

    #获取类别
    def get_genre(self):
        genre = self.ab.findEleAndReturnText(0, "xpath", "/html/body/div/div[2]/div[1]/div[2]/p[4]/span")
        print(genre)
        return genre

    #获取演员
    def get_star(self):
        star = self.ab.findEleAndReturnText(0, "xpath", "/html/body/div/div[2]/div[1]/div[2]/p[4]/span")
        print(star)
        return star

    #获取发行商
    def get_label(self):
        label = self.ab.findEleAndReturnText(0, "xpath", "/html/body/div/div[2]/div[1]/div[2]/p[4]/span")
        print(label)
        return label

    #获取制作商
    def get_studio(self):
        studio = self.ab.findEleAndReturnText(0, "xpath", "/html/body/div/div[2]/div[1]/div[2]/p[4]/span")
        print(studio)
        return studio

    #获取导演
    def get_director(self):
        director = self.ab.findEleAndReturnText(0, "xpath", "/html/body/div/div[2]/div[1]/div[2]/p[4]/span")
        print(director)
        return director


if __name__ == "__main__":
    # yuming_list = ["https://www.javbus.com","https://www.busdmm.one","https://www.dmmbus.zone","https://www.seedmm.one"]
    # pre_number = ["HUNT","HUNTA","MKMP","YMDD","NASH","ZMEN","UMSO","MDTM","MDBK","BAZX","NASH","BAZX","BOKD","XRW","BNJC"]

    yuming = "https://www.dmmbus.zone"
    pre_number = "HUNT"
    error_url_list=[]
    for i in range(1,2):
        if len(str(i)) == 1:
            forcount_i = '00%s' % i
        elif len(str(i)) == 2:
            forcount_i = '0%s' % i
        else:
            forcount_i = i

        try:
            url = "%s/%s-%s"% (yuming,pre_number,forcount_i)

            sb = SpiderBase(weburl=url)
            #打开网址
            sb.get_web_url()
            #获取封面图
            front_cover_img = sb.get_front_cover_img()
            #获取视频链接
            video_url = sb.get_video_url()
            #获取下载地址
            down_load = sb.get_down_load()
            genre = sb.get_genre()
            star = sb.get_star()
            label = sb.get_label()
            studio = sb.get_studio()
            director = sb.get_director()
            splider_title = sb.get_splider_title()
            prenum = sb.get_prenum()

            # from spiderdata.models import SpiderDate
            #
            # spiderdata = SpiderDate()
            # spiderdata.splider_url = url
            # spiderdata.front_cover_img = front_cover_img
            # spiderdata.video = video_url
            # spiderdata.down_load = down_load
            # spiderdata.genre = genre
            # spiderdata.star = star
            # spiderdata.label = label
            # spiderdata.studio = studio
            # spiderdata.director = director
            # spiderdata.splider_title =splider_title
            # spiderdata.prenum = prenum
            # is_exist_url_count = SpiderDate.objects.filter(splider_url=url).count()
            # print(is_exist_url_count)
            # if is_exist_url_count==0:
            #     spiderdata.save()
            # else:
            #     print("已经爬取过网站：%s" % url)
        except:
            error_url_list.append(url)

    print("失败网址：")
    print(error_url_list)




