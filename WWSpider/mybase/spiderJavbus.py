
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from requests_html import HTMLSession

from WWTest.util.getTimeStr import GetTimeStr   #导入获取时间串函数
from WWSpider.util.handleTxt import HandleTxt



class SpiderBase(object):
    def __init__(self,weburl):
        self.ab = HTMLSession()
        self.web_url = weburl
        self.response = self.get_web_url()
        self.timeStr = GetTimeStr()

    #进入URL
    def get_web_url(self):
        response = self.ab.get(url=self.web_url)
        # response.html.render()  #使用render函数加载js
        result = self.get_obj_full_text(response)
        return response

    def get_image(self):
        response = self.response
        # 使用find方法获取类名为bigImage的a标签下的img标签 ，返回符合条件的第一项，如果first=False，则返回所有符合的集合
        front_cover_img = response.html.find("a.bigImage img",first=True)
        return front_cover_img

    #获取时间串
    def getTimeStr(self):
        tStr = self.timeStr.getTimeStr()
        return tStr

    def getTimeStrNY(self):
        tStrNY = self.timeStr.getTimeStrNY()
        return tStrNY

    #创建目录
    def createdir(self,filedir):
        filelist = filedir.split("/")
        # print(filelist)
        long = len(filelist)
        # print(long)
        zuhefiledir = filelist[0]
        for i in range(1,long):
            zuhefiledir = zuhefiledir+"/"+filelist[i]
            if os.path.exists(zuhefiledir):
                print("已经存在目录：%s" % zuhefiledir)
            else:
                os.mkdir(zuhefiledir)
                print("已经创建目录：%s" % zuhefiledir)

    #获取爬虫图片并保存
    def saveSpiderImage(self):
        tStr = self.getTimeStr()   #获取当前时间串
        currentny = self.getTimeStrNY()   #获取当前时间的年月
        firedir = r'%s/media/report/%s/screenshots/' % (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),currentny)
        self.createdir(firedir)
        path = '%sscreenpicture_%s.png' % (firedir,tStr)
        return path

    #获取封面图片
    def get_front_cover_img(self):
        front_cover_img = self.get_image()
        front_cover_img_url = front_cover_img.attrs["src"]
        print(front_cover_img_url)
        import requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Remote Address': '104.26.1.213:443',
            'Referrer Policy': 'no-referrer-when-downgrade',
        }
        imagewe = requests.get(url=front_cover_img_url, headers=headers)
        image_content = imagewe.content
        print(image_content)
        imageend = self.saveSpiderImage()
        with open(imageend, 'wb') as f:
            f.write(image_content)
        imageend_list = imageend.split("media")
        from wanwenyc.settings import DJANGO_SERVER_YUMING
        image_xpath = "%s/media%s"%(DJANGO_SERVER_YUMING,imageend_list[1])
        print("封面图：%s" % image_xpath)
        return image_xpath

    #获取标题
    def get_splider_title(self):
        front_cover_img = self.get_image()
        splider_title = front_cover_img.attrs["title"]
        print(splider_title)
        return splider_title

    def get_obj_full_text(self,inputObj):
        obj_full_text = inputObj.text
        print(obj_full_text)
        return obj_full_text

    #获取编号
    def get_prenum(self):
        # 使用xpath的方法获取类名为col-md-3 info的div标签下的第一个P标签下的第二个span元素集合
        prenums = self.response.html.xpath("//div[@class='col-md-3 info']/p[1]/span[2]")
        for prenum in prenums:
            prenum_text = self.get_obj_full_text(prenum)
            # print(prenum.attrs)
            return prenum_text

    #获取导演，制作商，发行商
    def get_direcotr_and_studio_and_label(self):
        # 使用xpath的方法获取类名为col-md-3 info的div标签下的所有P标签的a标签元素集合
        direcotr_and_studio_and_label_eles = self.response.html.xpath("//div[@class='col-md-3 info']/p/a")
        direcotr_and_studio_and_label_list = []
        for one in direcotr_and_studio_and_label_eles:
            one_text = self.get_obj_full_text(one)
            direcotr_and_studio_and_label_list.append(one_text)  #添加元素的text到列表中
            #将对应网址写入文件中
            one_href = one.attrs["href"]
            mynowdir = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            print("当前路径：%s" % mynowdir)
            base_dir = '%s/mybase/SJB/SPIDERURL'%mynowdir
            self.createdir(base_dir)
            if "director" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_DIRECTOR.txt"%base_dir)
                ht.add_content(one_href)
            elif "studio" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_STUDIO.txt"%base_dir)
                ht.add_content(one_href)
            elif "label" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_LABEL.txt"%base_dir)
                ht.add_content(one_href)
            else:
                ht = HandleTxt("%s/ONEWEBURL.txt"%base_dir)
                ht.add_content(one_href)
        return direcotr_and_studio_and_label_list #返回列表

    #获取类别
    def get_genre(self):
        # 使用xpath的方法获取类名为col-md-3 info的div标签下的所有P标签的span标签下的a标签元素集合
        genres = self.response.html.xpath("//div[@class='col-md-3 info']/p/span/a")
        genre_list = []
        for one in genres:
            one_text = self.get_obj_full_text(one)
            # print(one_text)
            one_href = one.attrs["href"]
            # print(one_href)
            mynowdir = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            print("当前路径：%s" % mynowdir)
            base_dir = '%s/mybase/SJB/SPIDERURL'%mynowdir
            self.createdir(base_dir)
            if "genre" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_GENRE.txt"%base_dir)
                ht.add_content(one_href)
                genre_list.append(one_text)  #添加到类别列表
        return genre_list

    #获取演员和演员头像
    def get_star_and_photo(self):
        # 使用xpath的方法获取类名为col-md-3 info的div标签下的所有P标签的span标签下的a标签下的img元素集合
        starts = self.response.html.xpath("//div[@id='avatar-waterfall']/a/div/img")
        start_list = []
        for one in starts:
            one_text = one.attrs["title"]
            print(one_text)
            one_href = one.attrs["src"]
            print(one_href)
            # mynowdir = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            # print("当前路径：%s" % mynowdir)
            # base_dir = '%s/mybase/SJB/SPIDERURL'%mynowdir
            # self.createdir(base_dir)
            #
            # ht = HandleTxt("%s/ONEWEBURL_STAR.txt"%base_dir)
            # ht.add_content(one_href)   #添加到演员列表
            # start_list.append(one_text)

        # return star_list

    #获取类别和演员
    def get_genres_and_stars(self):
        # 使用xpath的方法获取类名为col-md-3 info的div标签下的所有P标签的span标签下的a标签元素集合
        genre_and_starts = self.response.html.xpath("//div[@class='col-md-3 info']/p/span/a")
        genre_list = []
        start_list = []
        genre_and_start_list = []
        for one in genre_and_starts:
            one_text = self.get_obj_full_text(one)
            # print(one_text)
            one_href = one.attrs["href"]
            # print(one_href)
            mynowdir = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            print("当前路径：%s" % mynowdir)
            base_dir = '%s/mybase/SJB/SPIDERURL'%mynowdir
            self.createdir(base_dir)
            if "genre" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_GENRE.txt"%base_dir)
                ht.add_content(one_href)
                genre_list.append(one_text)  #添加到类别列表
            elif "star" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_STAR.txt"%base_dir)
                ht.add_content(one_href)   #添加到演员列表
                start_list.append(one_text)
            else:
                ht = HandleTxt("%s/ONEWEBURL.txt"%base_dir)
                ht.add_content(one_href)

        genre_and_start_list.append(genre_list)
        genre_and_start_list.append(start_list)
        print(genre_and_start_list)
        return genre_and_start_list


    #获取下载地址链接
    def get_down_load(self):
        # 使用xpath的方法获取类名为col-md-3 info的div标签下的所有P标签的span标签下的a标签元素集合
        down_loads = self.response.html.xpath("//div[@class='movie']")
        for one in down_loads:
            one_text = self.get_obj_full_text(one)
            print(one_text)
            # one_href = one.attrs["href"]
            # print(one_href)
        # print(down_load)
        # return down_load






if __name__ == "__main__":
    # yuming_list = ["https://www.javbus.com","https://www.busdmm.one","https://www.dmmbus.zone","https://www.seedmm.one"]
    # pre_number = ["HUNT","HUNTA","MKMP","YMDD","NASH","ZMEN","UMSO","MDTM","MDBK","BAZX","NASH","BAZX","BOKD","XRW","BNJC"]

    url = "https://www.busdmm.one/MIAA-261"
    sb = SpiderBase(url)
    # sb.get_front_cover_img()
    # sb.get_prenum()
    # direcotr_and_studio_and_label_list = sb.get_direcotr_and_studio_and_label()
    # director = direcotr_and_studio_and_label_list[0]
    # print(director)
    # studio = direcotr_and_studio_and_label_list[1]
    # print(studio)
    # label = direcotr_and_studio_and_label_list[1]
    # print(label)
    # genres_and_stars_list = sb.get_genres_and_stars()
    # genre_list = genres_and_stars_list[0]
    # print(genre_list)
    # star_list = genres_and_stars_list[1]
    # print(star_list)
    # sb.get_down_load()
    # genre_list = sb.get_genre()
    # print(genre_list)
    sb.get_star_and_photo()


    # url = "https://www.busdmm.one"
    # error_url_list=[]
    # for i in range(78,79):
    #     try:
    #         url = "http://fpie1.com/#/play-details/%s"% i
    #         sb = SpiderBase(weburl=url)
    #         #打开网址
    #         sb.get_web_url()
    #         #获取视频链接
    #         video_url = sb.get_video_url()
    #         #获取下载地址
    #         down_load = sb.get_down_load()
    #         #获取封面图
    #         front_cover_img = sb.get_front_cover_img()
    #
    #         from spiderdata.models import SpiderDate
    #
    #         spiderdata = SpiderDate()
    #         spiderdata.splider_url = url
    #         spiderdata.front_cover_img = front_cover_img
    #         spiderdata.video = video_url
    #         spiderdata.down_load = down_load
    #         is_exist_url_count = SpiderDate.objects.filter(splider_url=url).count()
    #         print(is_exist_url_count)
    #         if is_exist_url_count==0:
    #             spiderdata.save()
    #         else:
    #             print("已经爬取过网站：%s" % url)
    #     except:
    #         error_url_list.append(url)
    #
    # print("失败网址：")
    # print(error_url_list)




