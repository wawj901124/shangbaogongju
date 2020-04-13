
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


    #进入URL
    def get_web_url(self):
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        # }
        response = self.hs.get(url=self.web_url)
        print("进入网址：%s" % self.web_url)
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
        direcotr_list = []
        studio_list = []
        label_list = []
        for one in direcotr_and_studio_and_label_eles:
            one_text = self.get_obj_full_text(one)
            #将对应网址写入文件中
            one_href = one.attrs["href"]
            mynowdir = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            print("当前路径：%s" % mynowdir)
            base_dir = '%s/mybase/SJB/SPIDERURL'%mynowdir
            self.createdir(base_dir)
            if "director" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_DIRECTOR.txt"%base_dir)
                ht.add_content(one_href)
                direcotr_list.append(one_text)
                direcotr_list.append(one_href)
                direcotr_and_studio_and_label_list.append(direcotr_list)
            elif "studio" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_STUDIO.txt"%base_dir)
                ht.add_content(one_href)
                studio_list.append(one_text)
                studio_list.append(one_href)
                direcotr_and_studio_and_label_list.append(studio_list)
            elif "label" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_LABEL.txt"%base_dir)
                ht.add_content(one_href)
                label_list.append(one_text)
                label_list.append(one_href)
                direcotr_and_studio_and_label_list.append(label_list)
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
                genre_list_one = []
                genre_list_one.append(one_text)
                genre_list_one.append(one_href)
                genre_list.append(genre_list_one)  #添加到类别列表

            elif "star" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_STAR.txt"%base_dir)
                ht.add_content(one_href)   #添加到演员列表
                star_list_one = []
                star_list_one.append(one_text)
                star_list_one.append(one_href)
                start_list.append(star_list_one)
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


    yuming = "https://www.busdmm.one"
    error_url_list=[]
    for i in range(1,200):
        if len(str(i)) == 1:
            fcount_i = '00%s' % i
        elif len(str(i)) == 2:
            fcount_i = '0%s' % i
        else:
            fcount_i = i

        url = "https://www.busdmm.one/HUNT-%s" % fcount_i

        from spiderdata.models import SpiderData
        is_exist_url_count = SpiderData.objects.filter(splider_url=url).count()
        print(is_exist_url_count)
        if is_exist_url_count != 0:
            print("已经爬取过网站：%s" % url)
        else:
            try:
                sb = SpiderBase(url)
                #获取标题
                splider_title = sb.get_splider_title()
                print("标题：")
                print(splider_title)
                # 获取封面图路径
                front_cover_img_local_xpath = sb.get_front_cover_img()
                print("封面图路径：")
                print(front_cover_img_local_xpath)
                # 获取编号
                prenum = sb.get_prenum()
                print("编号：")
                print(prenum)
                # 获取导演，制作商，发行商
                direcotr_and_studio_and_label_list = sb.get_direcotr_and_studio_and_label()
                print("导演，制作商，发行商：")
                print(direcotr_and_studio_and_label_list)
                # 获取类别和演员
                genres_and_stars_list = sb.get_genres_and_stars()
                print("类别和演员：")
                print(genres_and_stars_list)
                # 获取演员和头像
                star_and_photo_list = sb.get_star_and_photo()
                print("演员和头像:")
                print(star_and_photo_list)

                # 进行ajax异步请求获取下载链接
                sb2 = SpiderBase(url)
                # 获取下载链接
                down_load_list = sb2.get_down_load()
                print("下载链接:")
                print(down_load_list)

                #保存数据前，先保存导演，制作商，发行商：
                # #保存导演
                #------------------------------------------------------------------------------
                from spiderdata.models import SpiderDirector
                director_save = direcotr_and_studio_and_label_list[0][0]
                is_exist_director_count = SpiderDirector.objects.filter(director=director_save).count()
                if is_exist_director_count != 0:
                    print("导演[%s]已经存在" % director_save)
                else:
                    spiderdirector = SpiderDirector()
                    spiderdirector.director = director_save
                    spiderdirector.director_url = direcotr_and_studio_and_label_list[0][1]
                    spiderdirector.save()
                    print("已经成功保存导演【%s】到相应数据库中" % director_save)

                #保存制作商
                # ------------------------------------------------------------------------------
                from spiderdata.models import SpiderStudio
                studio_save = direcotr_and_studio_and_label_list[1][0]
                is_exist_studio_count = SpiderStudio.objects.filter(studio=studio_save).count()
                if is_exist_studio_count != 0:
                    print("制作商[%s]已经存在"%studio_save)
                else:
                    spiderstudio = SpiderStudio()
                    spiderstudio.studio = studio_save
                    spiderstudio.studio_url = direcotr_and_studio_and_label_list[1][1]
                    spiderstudio.save()
                    print("已经成功保存制作商【%s】到相应数据库中"%studio_save)

                # 保存发行商
                # ------------------------------------------------------------------------------
                from spiderdata.models import SpiderLabel

                label_save = direcotr_and_studio_and_label_list[2][0]
                is_exist_label_count = SpiderLabel.objects.filter(label=label_save).count()
                if is_exist_label_count != 0:
                    print("发行商[%s]已经存在"%label_save)
                else:
                    spiderlabel = SpiderLabel()
                    spiderlabel.label = label_save
                    spiderlabel.label_url = direcotr_and_studio_and_label_list[2][1]
                    spiderlabel.save()
                    print("已经成功保存发行商【%s】到相应数据库中"%label_save)

                #保存数据前，先保存类别，演员：
                #保存类别
                for genre_one_list in genres_and_stars_list[0]:
                    from spiderdata.models import SpiderGenre

                    genre_save = genre_one_list[0]
                    is_exist_genre_count = SpiderGenre.objects.filter(genre=genre_save).count()
                    if is_exist_genre_count != 0:
                        print("类别[%s]已经存在"% genre_save)
                    else:
                        spidergenre = SpiderGenre()
                        spidergenre.genre = genre_save
                        spidergenre.genre_url = genre_one_list[1]
                        spidergenre.save()
                        print("已经成功保存类别【%s】到相应数据库中"% genre_save)

                #保存演员
                for star_one_list in genres_and_stars_list[1]:
                    from spiderdata.models import SpiderStar

                    star_save = star_one_list[0]
                    is_exist_star_count = SpiderStar.objects.filter(star=star_save).count()
                    if is_exist_star_count != 0:
                        print("演员[%s]已经存在"% star_save)
                    else:
                        spiderstar = SpiderStar()
                        spiderstar.star = star_save
                        spiderstar.star_url = star_one_list[1]
                        spiderstar.save()
                        print("已经成功保存演员【%s】到相应数据库中"% star_save)

                #保存演员头像到相应的数据库
                for star_and_photo_one_list in star_and_photo_list:
                    from spiderdata.models import SpiderStar
                    star_search = star_and_photo_one_list[0]
                    star_find_list = SpiderStar.objects.filter(star=star_search)
                    for star_one in star_find_list:
                        print("star_one.star_url:")
                        print(star_one.star_url)
                        star_one.star_url=star_and_photo_one_list[0]
                        star_one.save()
                        print("已经成功保存演员头像【%s】到相应数据库中" % star_and_photo_one_list[0])

                #保存除下载链接外的数据
                #保存数据到数据库
                spiderdata = SpiderData()
                #保存url
                spiderdata.splider_url = url
                #保存title
                spiderdata.splider_title = splider_title
                #保存封面图
                spiderdata.front_cover_img = front_cover_img_local_xpath
                #保存编号
                spiderdata.prenum = prenum
                spiderdata.save()

                #保存下载地址
                for down_load in down_load_list:
                    from spiderdata.models import SpiderDownLoad

                    sdl_sd_list = SpiderData.objects.filter(splider_url=url)
                    for sdl_sd in sdl_sd_list:
                        spiderdownload = SpiderDownLoad()
                        spiderdownload.spiderdata_id = sdl_sd.id
                        spiderdownload.down_load = down_load
                        spiderdownload.save()
                        break

            except Exception as e:
                print("报错：%s" % e)
                error_url_list.append(url)

    print("失败网址：")
    print(error_url_list)




