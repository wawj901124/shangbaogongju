
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from requests_html import HTMLSession

from WWTest.util.getTimeStr import GetTimeStr   #导入获取时间串函数
from WWSpider.util.handleTxt import HandleTxt
from WWTest.base.activeBrowser import ActiveBrowser



class SpiderBase(object):
    def __init__(self,weburl):
        self.hs = HTMLSession()
        self.web_url = weburl
        self.response = self.get_web_url()
        self.timeStr = GetTimeStr()
        # self.ab = ActiveBrowser()

    #进入URL
    def get_web_url(self):
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        # }
        response = self.hs.get(url=self.web_url)
        # response.html.render()  #使用render函数加载js
        result = self.get_obj_full_text(response)
        return response

    def get_web_url_reponse_text(self):
        return self.get_obj_full_text(self.response)

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

    #把第三方地址的图片转化为本地图片
    def get_image_from_imgsrc(self,imgsrc):
        import requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Remote Address': '104.26.1.213:443',
            'Referrer Policy': 'no-referrer-when-downgrade',
        }
        imagewe = requests.get(url=imgsrc, headers=headers)
        image_content = imagewe.content
        print(image_content)
        imageend = self.saveSpiderImage()
        with open(imageend, 'wb') as f:
            f.write(image_content)
        imageend_list = imageend.split("media")
        from wanwenyc.settings import DJANGO_SERVER_YUMING
        image_xpath = "%s/media%s"%(DJANGO_SERVER_YUMING,imageend_list[1])
        print("转化成的本地图：%s" % image_xpath)
        return image_xpath

    #获取封面图片
    def get_front_cover_img(self):
        front_cover_img = self.get_image()
        front_cover_img_url = front_cover_img.attrs["src"]
        print(front_cover_img_url)
        import requests
        headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
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
        # print(obj_full_text)
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
        star_and_photos = self.response.html.xpath("//div[@id='avatar-waterfall']/a/div/img")
        star_and_photo_list = []
        for one in star_and_photos:
            star_and_photo_one_list = []
            one_text = one.attrs["title"]
            print(one_text)
            star_and_photo_one_list.append(one_text)
            one_href = one.attrs["src"]
            local_image_url = self.get_image_from_imgsrc(one_href)
            print(local_image_url)
            star_and_photo_one_list.append(local_image_url)
            star_and_photo_list.append(star_and_photo_one_list)
        return star_and_photo_list

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

    #正则匹配获取变量中的内容
    def get_re_content(self,pipei,content):
        import  re
        pipei_from_content = re.findall(pipei,content)
        print(pipei_from_content)
        return pipei_from_content


    def get_gid_and_uc_and_img(self):

        respose_text = self.get_obj_full_text(self.response)
        # print(respose_text)
        gid_and_uc_and_img_list = []
        gid_re = self.get_re_content(pipei=".*var.*gid.*=.*;",content=respose_text)
        gid = gid_re[0].split("=")[1].strip(" ").strip(";")
        gid_and_uc_and_img_list.append(gid)
        # print(gid)
        uc_re = self.get_re_content(pipei=".*var.*uc.*=.*;",content=respose_text)
        uc = uc_re[0].split("=")[1].strip(" ").strip(";")
        # print(uc)
        gid_and_uc_and_img_list.append(uc)
        img_re = self.get_re_content(pipei=".*var.*img.*=.*;",content=respose_text)
        img = img_re[0].split("=")[1].strip(" ").strip(";").strip("'")
        # print(img)
        gid_and_uc_and_img_list.append(img)
        print(gid_and_uc_and_img_list)
        return gid_and_uc_and_img_list



    #获取下载地址链接
    def get_down_load(self):
        #使用ajax请求获取链接地址
        gid_and_uc_and_img_list = self.get_gid_and_uc_and_img()
        ajax_url = "https://www.busdmm.one/ajax/uncledatoolsbyajax.php?gid=%s&lang=zh&img=%s&uc=%s&floor=236" %(gid_and_uc_and_img_list[0],gid_and_uc_and_img_list[2],gid_and_uc_and_img_list[1])
        headers = {
            # 'x-requested-with': 'XMLHttpRequest',  #这个说明是ajax请求，没有这个，也会识别
            # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'referer': '%s' % self.web_url,  # 此处要根据来源网址做出相应，没有就不会获取到相应内容
        }
        myresponse = self.hs.get(ajax_url, headers=headers)
        # print(myresponse.status_code)
        # print(myresponse.content)
        # print(myresponse.text)
        links_list = myresponse.html.absolute_links  #获取所有链接的绝对路径
        for i in links_list:
            print(i)
        return links_list


if __name__ == "__main__":
    # yuming_list = ["https://www.javbus.com","https://www.busdmm.one","https://www.dmmbus.zone","https://www.seedmm.one"]
    # pre_number = ["HUNT","HUNTA","MKMP","YMDD","NASH","ZMEN","UMSO","MDTM","MDBK","BAZX","NASH","BAZX","BOKD","XRW","BNJC"]

    url = "https://www.busdmm.one/HUNT-002"

    sb = SpiderBase(url)
    #获取封面图路径
    front_cover_img_local_xpath = sb.get_front_cover_img()
    print("获取封面图路径:")
    print(front_cover_img_local_xpath)
    #获取编号
    prenum_text = sb.get_prenum()
    print("编号:")
    print(prenum_text)
    #获取导演，制作商，发行商
    direcotr_and_studio_and_label_list = sb.get_direcotr_and_studio_and_label()
    print("导演，制作商，发行商:")
    print(direcotr_and_studio_and_label_list)
    #获取类别和演员
    genres_and_stars_list = sb.get_genres_and_stars()
    print("类别和演员:")
    print(genres_and_stars_list)
    #获取演员和头像
    star_and_photo_list = sb.get_star_and_photo()
    print("演员和头像:")
    print(star_and_photo_list)


    #进行ajax异步请求获取下载链接
    sb2 = SpiderBase(url)
    #获取下载链接
    down_load_list = sb2.get_down_load()
    print("下载链接:")
    print(down_load_list)


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
    # star_and_photo_list = sb.get_star_and_photo()
    # print(star_and_photo_list)
    # sb.get_down_load()


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




