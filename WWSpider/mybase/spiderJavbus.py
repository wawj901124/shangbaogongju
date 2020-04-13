
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
        self.prenum = self.get_prenum()
        self.init_image = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\x03\x02\x02\x03\x02\x02\x03\x03\x03\x03\x04\x03\x03\x04\x05\x08\x05\x05\x04\x04\x05\n\x07\x07\x06\x08\x0c\n\x0c\x0c\x0b\n\x0b\x0b\r\x0e\x12\x10\r\x0e\x11\x0e\x0b\x0b\x10\x16\x10\x11\x13\x14\x15\x15\x15\x0c\x0f\x17\x18\x16\x14\x18\x12\x14\x15\x14\xff\xdb\x00C\x01\x03\x04\x04\x05\x04\x05\t\x05\x05\t\x14\r\x0b\r\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\xff\xc0\x00\x11\x08\x00}\x00}\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1e\x00\x00\x02\x02\x03\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x06\x07\x05\x08\x03\x04\t\x02\x01\x00\n\xff\xc4\x00G\x10\x00\x01\x03\x02\x04\x03\x05\x03\t\x04\t\x02\x07\x00\x00\x00\x01\x02\x03\x04\x05\x11\x00\x06\x12!\x071A\x08\x13"Qaq\x81\x91\x14\x15#2B\x82\xa1\xb1\xb2\x16Rb\xc1$%CScr\xa2\xc2\xd1\tt34ds\x92\xd2\xf0\xff\xc4\x00\x1b\x01\x00\x03\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x05\x06\x03\x02\x07\x01\x00\xff\xc4\x007\x11\x00\x01\x03\x02\x03\x04\x08\x05\x03\x04\x03\x00\x00\x00\x00\x00\x01\x00\x02\x03\x04\x11\x05!1\x12AQq\x13"a\x81\x91\xa1\xc1\xf0\x14$R\xd1\xe12\xb1\xf1\x06#4bBr\xb2\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xba\xfcI@V`?\xf6\xc8\xff\x00v\x05U\xba\x1d>G\xf9`\xbf\x88\x88\xbed\x03\xce2\x7f\xdd\x81\x02l\xd3\xbed\xe3\xc21\\\xabf\xff\x00\xb1^\xbf\x86\xe7K\x1f \x98m5\xfd\x01\x92\x06\xfd\xda?!\x8c\xd0\xd0;\xdb\xdb\xa7\\lDh\x1als\x7f\xec\x91\xfaF=\xa1\xb0\x97\x01\xe5\x8a\x06\xc5b\n\x9ft\x97\xb8Y\xe8\xc3\xfa\xe6\x19\xff\x00\x1d?\x9e\x19C\x0b\x9aZt\xd6"\x91\xfd\xfa\x7f<1\x86,\xb01h\xdf\xcf\xd1Mbf\xefo%\xf7\x1f\xb1^8\xd5\xdb\n\x97\x90s\x19\xc9Y\x1b/O\xe2\x8f\x12\x16\x93j\r\x10\x8e\xee/MR\x9f\xdd-$\x1ew\xdf\xce\xd8\x01g)\xf6\x92\xe2sb^o\xe2\x05\'\x87,;\xe2\x14|\xb0\xd9yl\x03\xf6K\x80\xa5J>\xbd\xed\xbd0\xe5\xd57\x1f\xd9iw+\x01\xe2}.\xb0\x8b\x0f\x96@\x1c\xf2\x1a\x0f\x1d\xfc\x86\xaa\xe0>\xf3q\x99[\x8e(!\xb4\rJQ\xe4\x06\x02\xab9\x9e]L\x96a%\xc8\xd1\xb9k\x02\xce/\xff\x00\xa8\xfc}\x98\xafOvG\xa5U\x99@\xcd<@\xcf\x19\x9d\xd1\xba\xbb\xea\x92Xl\x9f0\x90\x95+\xe2\xa3\xcb\x01Y\xeb\xb0\xc3\x13)\xee~\xc5\xf1\x1b0\xe5\xda\x87\xd6@\xaa,M\x8e\xa3\xd0\x12\x8e\xedi\x17\xea\t\xf6au@\xaf\x9cl\xb5\xadh\xdf\xd67\xff\x00\xcaqMA\x04Gm\xce\xda;\xb2\xcb\xdf5g\xd8\x8b\xdd\x10\x14\x9d\n\xf5\x1c\xf1\xb0\xe3D\xb2\x95\xdc\'Q6\xdb\xa69\xcb\x97\xb3/j\x0e\xce\xbcO\xcb\x19K0C\x19\x96\x91[\xaaF\xa6\xc1\xa80\xea\xe5\xd3\xdeS\x8e%\x16.\x91\xad\xa2\x01*\xd2\xb0\x83d\xa8\x8eW\xc7Es\x0c\x93\x16\xe8`\x95!\xa3\xa4+\xf7\x80\xeb\x8c\xa9(\\\t\x136\xdd\xe8\xec\xdf kJGq\x89\x9ar\xd1.l\xae\xee#\xf1\x90\xa2\xe4\x92\xa0\x8d)M\xcd\xd4\xaf$\xda\xfb\xfeXT\xf0\xc7\x86sx\xbe\x13Yy\xc7\xa9\x99x=x\xefX%\xc7\xd0>\xdaE\xac\t<\x89\xe5by\xe9\xb1\xa7j\xae\x1fU\xf8\x8a\x9c\x9d\x02\x8e\xad\x14\xbc\xc1Wf\x97Z)&\xe8F\xeb\n6\xfb+J\x16\x15\xea\x94\x8f\xb5\x82\xfa\xc6y\xa0\xe4\xfa\xd5\x1f\'\xb4\xd3\x91)\xe0\x08\xb1\xbb\xbb\x06\xc2\x926\n\xde\xe4\x9fA\xcc\xe2R\xa2\x97\xe1\xaa\x1e\\3\xbe\\\xb8\xfb\xd0\xf6\xa0\xa5\xfe\x92\xc1k*\xdb\x88|+zmI\xcf^%\xb7\xd9\'\x81"\xe7T{\x95\xb2M\'.S\xda\x89M\x8c\xdcx\xc8\xe4\x1b\xdc\xa8\xf5*W2O2I$\xf5\xc1:!\x84\xa6\xdamlCe\x15\x87\xa3\xb8\xaeI\x07\xc2\x95y`\x94\x01m\xc1>\xec0\x81\x9bL\x0e\xb2:a\xd1<\xb0nB\x1cF=\xdefl\xf41\x90\r\xfd\xaa\xc0i7J\xc9\xe9\xff\x00\x18-\xe2\x89(\xaf6\x7f\xc0o\xf5\x9c\t\xac\x00\\\x07\xa5\xb1\t\x8b\x1f\x9e\x98v\x95K\x86\x0f\x94\x8c\xf6&\x9c\x03z\\\x7f\xfd\x96\xff\x00H\xc7\xc9AKehI\xb2\x88\x00\x1fx\xc7\xaau\x95H\x8cGV[\xfc\x863h* \x01rH\xc5P\x17h\xe4\xa6I\xb3\xc9\xed_\x916=.@\x9b6CQ!\xc7P}\xf9\x0f\xac!\xb6\x90\x9d\xd4\xa5(\xec\x00\x1b\x92p\x96\xcd|S\xce=\xa6\xab\xb5\x1c\xa1\xc3YO\xe5\\\x95\x19A\x8a\xbeq[D<R@=\xdct\x9b}"\x92A\t\xe6\x94\x90\xa5\xe9\x04!J\x9e;qy\xfe+f\xb6\xb2~\\\x93z\x03\x13\xda\x83\xde6n\x9a\x9c\xe2\xab\x0b\xdb\xeb0\xd6\xea#\x92\x8a\t;\x01\x8bZ\x97r\xaf\x032\x04(\xd2$\xb5F\xa1\xd3\xd1\xdd4\\\xba\x9c}\xc3r\xb5i\x17S\x8e\xadWR\x8e\xe4\x95\x12p\xd7\x0b\xbdH\x92\xe6\xd1\x03\x9f\xfb\x1e\x17\xfax\xf1\xe5u\xac\xb4\xa2\x06\xc73\xdb\xb5#\xb2h\xe1m\xf6\xdes\xc8w\xeeXxU\xc1\xfc\xa9\xc1\\\xb0(yR\x99\xf2\x16\x16{\xc9R\xde_{.s\xbd]\x90\xe9\xdd\xc5\x9f]\x87$\x806\xc1j\x85\x90M\x8e\x907U\xb9{\xf1J\xf8\xaf\xdb\xa2\xb7>C\xf0r$\x06\xe8\xd0\x91t\xaa\xa9=\x94\xbf%D\x1b\\ \x92\xdbv\xf5\xd6y\r\x8e\xd8\xabY\xbb\x8ay\xc37\x97MO1U\xeb\xcf\xac\xde\xf3&)H\xe7\xe2\tl\x10\x84\x81\xfb\xd6\x00\x1f24\x86\xb2c04\xec\xc26\xad\xdc=\xf7r_\x99\x86\xca\xee\xb4\xee\xb5\xfb\xcf\xbe\xf5\xd5\xaa\x9ei\xa4\xd3I\x12\'\xc5l\x8eaR\x1b\x04{\x8a\x864b\xe6\xaa]MG\xe4\xd2R\xf9\xff\x00\r%c\xe2\x9b\x8f\xc7\x1c?\xe2\x0ec\x7f\xbap\xbb!\xda\x9e\x81\xff\x00\x92\x83t\xb0\x83\x7f\xb6\xe0\x04\xab{_\x95\xfa[\n\x98\xb5\n\xb4z\x82g\xb2\xe2\xe9\x8f%_F\xb8JR\x14\x83\xe8A\xbe\xd7\xf3\xea7\xdf\x06S\xd6>v\xed9\xa0\x0e\x7f\x81\xfb.^!\x85\xdb\x16$\xfb\xee\xf3_\xd0\xc2\xe46\xa7\xa3Jiz\xd3\x1d\xe4\xb8\xbe\xec\x85xy\x1b\xdb\xc8\x12}\xd8\x90\x9a\x94\xbe\x92\xa1e\xa6\xd76\xdc)$s\x1e~x\xe2/\x0b\xbbj\xf1\x87\x87\xf3\xdbC\x19\xb2N`\x86\xda\x92\x94\xc3\xcc\nT\xb0N\x92t\xa5\xd2{\xe4\xec>\xca\xc0\xf48\xbf=\x9f{{\xe5\xee&\xc6\x80\xcc\xf6UH\xa9IIR\xa08\xb0\xa3\xa8}b\xd2\xc0\x01`s(\xb2T9\xe9"\xe4\x9e%h9\x94M<\x7f\x18@\x84\xf5\x85\xec\x0e\xfc\xf7{\xde\xad}5\x94;\x00\xf7\x8d%.\x03\xa5IH\xd8-\'\xeb_\xf1\x07\xc8\xe1K?\x84\xd4\xca\x9e\x7fNa\x95\x01\x0e\xd5XU\x99\x92\xa2HA\x1b\x05\x04\x93mV\xfbV\xe9\x83\x8a\xd0^y\xcau\x984*\xc0\xa5\xfc\xe1\x05\xd6W5\x90\x14\xb8\xfa\xd0P\x14\xdd\xf6\x04\x82lO"\x9b\xf4\xb6$r\xfc\'\xa9t\x881fKT\xf9MFm\xb5\xcau\xb0\xdb\x8f\x14\x8d%JH\xd8(\xe9\xde\xdb^\xf8\x9f\xc5\xe9\x8c\xc5\x92\xee\x19]\x16\xd9$\xa6/:\x13\xbbxRt\xe2 \xb0\x86\xc7\xd9\x1c\xcf\\H"h\xb6\xff\x00\x86 \xdd\x90\x90\x9d\x95\xb5\xf1\x80\xcfI\xb7\x8a\xd6\xdb|\x06\xc7\x00,\x12\xa70\xb8\xdc\xaf<QM\xeb-y\xf7\x08\xfdg\x01\xca\xb9u\xed\xb9\x01\x83N\'\x81\xf3\xc3w;\x08\xe97\xfb\xe7\x01\xaa\xdaC\xc9\xfe\x10\x7f<y\xde0>~^j\x93\x0b?\'\x1f$\xd5\xa6\x8bQ"y\xf7-\xfeC\n\x1e\xd3\xdcJw$\xe4\x7f\x9a\xa9o\x06\xeb\xd5\xb0c\xb0\xab\xd8\xb2\xd7\'\x1c\xf4\xda\xff\x00\x03\x86\xfd!:\xa8\x90w\x02\xec\xb7s\xee\x18\xa5\xfcaq\xce"\xe7\x895\x95K\xb3j\x98\x8au"\x02\x1b*\\\x86\x92\xe6\x8dj7\xf0#X\xbf\x9a\x8d\xec-s\x87\xb5\x92\xecB\xd6\r]\x97v\xff\x00\xb2WCO\xd3\xd48\x9d\x1an|V\x1e\x01\xca\xcb<69\x93\x88y\x8c\x91B\xc91[\x8d\x069\xb6\xa7\xea2N\xdao\xcd\xcd!)\x1eE\xe2~\xce\x15y\xeb\x8cY\x93\x8d\x95c\x98\xab\x8f\x98\xac\xcb\xd6i\xd0\xd9\xd5\xa2\x14$\x91\xf4\x89\x07\xaa\x89\x00\x13\xf5\x89I;\\`[2Iw0\xe6\xf8\x1c\x1a\x95-2\xa3\xd2s\x05J\xbf[TU\x90\x87\x96B\x1b\x8eTy\x8d-\xa5[t.[\xa66\xf3\x84\xa8\xf1\x98[\xeaE\xd3+F\x88\xc8\xbaK\x8d\x8b\x86\x19\x1f\xba\x15\xba\xbd\x01Q\xf2\xc1\x13\xcd\xd1\xd3CI\x19\xd4\\\xf6\xdf;\xf6\xfd\x87jr@\x92w\xcd\xc3/\r\xde9\x9e\xd3\xd8\x86j\x12>xZ\x18B;\xb8$\xe9j;\x04\x95\xba\x01\xd2-\xd7M\xce\xeb\xea|)\xe6p\xd5\xe1\xd7g9\xf9\xbd\xa4\xae\xa6\xd7t\xc3\x84^+b\xc8\x03\xa0Q\x1f[\xd9\xc8t\x18\x9f\xec\xd9\xc1\x199\xa2Rk5\x16\x82\x9et\x85\x17-\xe0BF\xc9J\x07 \x906H\xe8\t=qvh\x99J&_\xa7\x86\x99e(\t\x1c\xc0\xc1\x14\xf4\xb7\x00\xa1\'\x9d\xb1\xe4u*\x84v\x8c\xe1U#!e8\xb4\xa8\xec2\xdc\xb9gH\r\xa6\xd6@\xe7\xe1\xf5;|qNs\x0eSA2\n.\xda\x12\x94\x95\x0f5\\\xed\xec\xbd\xc9\xf5\x1e\x98\xbc\xbd\xa8\xaa\xe2\xb5\xc4\xa9\xcc\xa7\xc4\xd5=\x94\xb0\x0fD\xac\x8dJ\x1f\xea\xfc1^*\xb9m\xbf\x9b\xdcwH\x0e-\x05\xd2\x00\xe6y\xa4|t\x8f}\xb1\x94s\xbe7\x97\x03\xbdv\xf8\x83\xda.\x15q\xa7Q\x93\x1a\xb1\x13\xbc\x1a\x06\xa5>\xa5\xa4_rH\xb0\xf3\xd8~8\xfb\x92\x03\x88\xcbS\x12\xa0\xa5\x06\x9dL\xa4\xe9U\x88\xb0B\x95n\xa0\xe8+7\x1eXiO\xc9\x9f$\xa88\xda\x10R\x86P\x1b\x00\x0b\xf2\xb8\xd8\xf5\xe4O\xbcb\x13+\xe5\xcf\x92\xcdTR\x8b\x05wHX\xb7\x9b\x0bA>\xdb\xdb\x0e\x8d`|n\xbe\xb9\x1f\x03\xf9J\xc56\xc4\x8ds{|\xc0\xfb+\xcf\xd8\xb3\x8e\xb2\xdd.d\xda\xd3\x91\x912"\x04\x86\xe4\xa9E*\x9f\x1d)\xd2\x97\x16N\xc5h\x03J\xb9~\xf5\xb7\xc5\xb4U\nmC13\x98\xa1T\x1e-*\x07\xc8\xdd\xa7(\x02\xcb\xc9\xef\x14\xea\x1dA\xe6\x97\x01Z\x86\xf7\nI\x16\xb1\x17<\xdf\xec\x89]\x10sd\x07V\xd8\\\xa6a\x97\x1a\xdf\xc4\xa2\xca\xf58\x8b\xff\x00\x13h\xd3\xf7\xb1\xd0\xde\x13\xe7jmR\x04\xaa\x03\xb3\x1a\x15*C\x86#\xec(\xe8XE\xfe\x85\xc1\xe6\x85\xa0\xa5@\x8f2:[\x0e)\x9c\xca\xca~\x8ec\x9d\xc8\xef\x1f\x8c\xff\x00\n\x86\xaa\x17\xd4R\n\xc6\x0b\x91\x93\xb7\x9bq> _\xb7\x8a\xda\x95X\x16>+y\xdcb)\xdc\xc0\x12\xab\x05\x9b{q\xb7\xc5\x0c\xa7Rf@\xa8\xd2\xfe\x91\x126u\xa5\x1d\xd2\xe0\x1c\xc1\xf2P\xdf\xdb|)\xe4\xc6\xcd\x9d\xe9\t\xa5\xa9@u\n\xc4eL\xb2\xd2\xcc\xe8^3\x1e}\xa8\x18`d\xd1\x87\xb0\xab\x0b\xc4\xc4\x07*\xcc\x8b\xd9&2N\xdeZ\xce\x02\xd4.\xea\xcfR\x9f\xe6pm\xc41z\xa4OX\x89\xdf\xef\x1c\x06\x1eK\xb7\xee\xff\x00<M\xe3\x03\xe7\xa5\xe6\xbe\xe1g\xe5\x18;\x11/\x10s\x0f\xec\xb7\x06\xaa\x95-\xc2\xda\xa6\x84\xa3O2T\x90\x9d\xbdw8\xabQ\x1c\xd7\x98\xe8\xfa\x95\x1e\x0b4\x86\x1aQ\x9a\xca.\xeaU\xdc6\x146\xe7g\x14t\xed\xb1R\x8e\xf8\xb0<{mR8"\xcc{\xa86\xfb\x91\x12\xbd"\xf7\x17\x16\x1f\x1bb\xbff\xfc\x9d6<\xe9\xb0!2\xf3\xaf6\xd3}\xf2#\xa7R\xf4\x13u\xaf\xd4\x00\x8c\x15U!\xe9\x9a\xde\x01\xbe\xa5\x15\x85F\xde\x8eBu$\xf9{\xf3J<\xb9\xc3\xb8\x94\x0c\xe3\x9e\xb33/\x87\xbfh\xe4&;\n\xd5\xa8\xa1\xb3\xe3\x91\x7fP\x06\x9b\x0e\xbdq\xad\x95\xb2\xab\xdcZ\xe2+\x91ZRQ\x19\xb7\x14\xcbcM\xd3s`\xa3a\xd0\x00\x10=\x00\xb6\x0fs\xc2\x93\x96\xf2\xd4(P\x92\x9e\xf9hDx\xe9E\xad\xad`\xadJ\xf6\x01\x7f\xfe>\xb8WW\xf8C\xc48\xaeS\xa7\xe4Y\xd2\xa3\xc6oO\xcb\xd1\x127\xca\x1fCz\xb5\x17[@ \xac\xa6\xdb\xa7\xa8\xc1P\x03S6\xd3\x8d\x86@_\x80\xc9t\xe1\xd0\xb2\xccm\xf5>\'\xb6\xcb\xa0Y~[\x1c#\xa0D\x85T\xa6\x06\xe36\x90\x156\n\t@?\xc4\x93\xba}\xf83\xfd\xac\xa6N\xa1I\xa8\xc4\x94\x89\x11ZmKZ\x92wM\x85\xecGC\xff\x008\xe5\xaa;[\xf1\x13\x81\xbcOr\x88\x9c\xda\xdf\x12\xb2\xc8s\xbaM2\\\x153*KE\xf52\x92\x84\xa5\x16K\x8a\t\x0e%\tQ\x05.$\x12M\xc0\xbb\xf4(\x91\xb3\xd5\x19\xa9\xd9yK\xa61X\x8c\x97;\x93\xb2t+{Xy\\\xf2\xdb\x14\xd3\xf4\xd4\x8d\x00u\x81\xd3\xf9\xcb\xccw\xa9\xe8[\x1dc\x8b\x8d\xc1\x1a\xdf\xed\xbb\xb8\xaa}\x9es\x1b\xb5\x9a\xd4\xa7\x9cP\x0b\x9b=\xc7\\Q\xe7\xba\x85\xff\x00+zb\x1eD\xc4\x97e\xb4\x13r\x86\x9bP\x07\x90\xfaC\xf8}\x1ap\xc5\xe3\x0fg\xac\xcd\x92W\x16S1\x9c\x9a\xdf\xca\\\x00\xb4/q\xabP\'\xca\xe0\x0f~\x02k\x99>\xa7Na\x12\xa4\xc7S.?\x1diPP\xb1\xba\\\x06\xc7\xd8\t\xf8bpK\xb0\x03\x1c,B\xa31\x97u\xdb\x98A\xc0\xa2Me\xd6\xd2R\x95\x17\x0e\xdc\xf6\x07\xa7\xb7lBF\x84\x85\xe7\x19\x8c4\x02\xc3KM\xc16&\xd7\x17\xf7\xef\x8c\xbf(r\x97\x9aU\xdf\x02t8\x97nv\xf0,\x85\x03\xeb\xbd\xc7\xc3\x1e)\xf2>G\x99\xe6\xcaQB\x80\x8e\\\x05]H\xd4\x7f\xe7\x0c\x05\x9c\xdb\x0e\t{\x85\xb5D\x1d\x9d&*\x9b\xc4*Oz\x03}\xdb\x8a\x7ft\xfdd\xa9iR\x87\xc0\x1c\\\xfe:Pj\x19\'\x84\xb9\xb7;e\x97\xd3\x073P)O\x16\xa5\x96\x92\xe0R\x18\xf1\x10\xb4\xa8\x10\xa4\x96\xd2E\x88#{\xf4\xc5*\xe12\x15\x1b;@)\xb2\xb4\xb4\x94\x03\xed*I?\xe9\xc5\xec\xedk\x9a\xe2d\xde\xcc<O\x91!iI\x99Lz\x0bI?i\xc9\tK#\xf1tb\x83\x0ch\x7fH\xd7q\x07\xbf?\xb2\xd0UK\x05+\xdb\x13\x88\xb87\xb7\x0b"\xce\xcd\xb9\xfe\xb7\xc5>\x07\xe5Z\xf5i\xb6\x14\xedN\x10\x92W\x18Y\r<\x97\x16\xda\xd0\x12I!$\'P\xdc\xdbq\xe5c\xf7\xa1\x84\x11d\x8d\xfc\xf0\xa5\xecRLN\xcc9%\xa2-\xdd2\xf2uZ\xdc\xdeZ\xb9}\xec8d\xb8J\xee/of\x17L\xe39\x0e~\xa9Yy\x0e+\xc7\x10Uj\x9c\x11\xe7\x11?\xa8\xe0D\xa8\\l\x05\xd0pW\xc41\xa2\xab\x00s\xd3\x18\x0b\xfb\x14p A\xd4\xaf+\x1b|F"1\x83j\xe9Go\xa0Lp\xc1\xf2\x91\xf2\xf5E\xf9\x92\x8c+\xdc:\x8d\x19IK\x84!\x85\x84\xabpJH?\xcb\x02\xb5J\x02 W%UX\x86\'\xbf.\x93\xa1,-a\xb4\xab\xc7\xa5WQ\xd8Y\x0b\'\x7f/\\2(\xe0;\x95\xa0&\xc2\xe5\x84\x8d\xfd\x98\x84\xcf\x0c">Q\xa9>\x12\x14\xb6\xa3\xb8\x94_\xa6\xa0G>\x9b\x90}\xd8}$\rp\x12\xff\x00\xa8\xfd\xbf)l5.\x8d\xe6!\xbd\xc7\xcf\xf8T\xb2\xa5\x0f\xf6\xa7\x89\xf4\xcakcTh-\x87T\x91\xcbS\x9b\'\xe0\x96\xff\x00\xd5\x8be\x93\xf2z)\x10\xa3\xb8\xca\x8b\x12[\x00\xa1\xc4sN+\x0f\x03\x96\x8a\xb7\x14j\xf3\x17\xe3mr\x02Qq\xc9(\xbaG\xff\x00\xbdqs\x18R\x12\xdaJ|"\xdf\x0c\x15\x86B\xd3\x1fY:\xc4$,cZ\xdd\xe8\x077p\xe2\x16d\xa9D\x9b2\x8bM\x97Q\x8a\xe7{\x1ezB\x99\x92\xca\xcd\xee\xa48\x8b)*\xb1;\x83}\xf13\xc3\\\x84\xc6G\xa4\xc4\xa60\xb7\xdfn9Z[rR\x92\xa7\x12\x82\xb5,&\xe0\x0b\x84\x85i\x06\xd7\xb2E\xf0`\xd6\x95\xa8u\'\xae2\xbeS\x0e+\xcf\x1e`Xa\xc9\x8fA{\xd9O\xbacm\x905A\xbcC\xaa\xa3\xc4\xd3h\n\'nW\xb7\xae+\xd7\x173\xb7\r2\xad(;\x9e&\x16U\xa3\xbc-\xb3~\xfa\xc4tH\xf3\x00\xf4\xdf\x0f\x05\xb4\xba\x8c\xb7\x1c^\xfa\x8e\xc3\n\x9e&vo\xcb\\F\xa0Vi\x13$\xd52\xe3uI\x02\\\xaa\x85\x1d\xe2K\xae\x80\xa4\xeaq\x0b\xbe\xe5.-\x07I\x00\xa5D\x11k`gF\xd9\x9e\x1d)\xb3Q\xc0\xba\x18\xb6"\xfdJ\xaf;G\xe1g\x16ji^A\xcf\x06T\xad%?6\xd4Y\xee\xdd\xe4U\xa5;\r[_o\x85\xf0\xa1\xcc\xf4\xc9\x14\xba\x8a\xd9W\xfe:Yu\x95%7#V\xc0\x11\xe9b}\x989\xe2Wc\x0c\xc5\xc3\x98,H\xca\xf5\x089\x86\xaa\x99\xaa\x90\xfdy\xf9\xabm\xd7X\xd2\x12\x86\x16\xd1H\xb2@H$\xeaQ*\xde\xe2\xc0`bTY\xf5U\tUd\xa9\xb9\xee\xbd\xdd\xb9as\xab\xc3{\xf9\xdfO\xe7\xe7\x81\xaa"\x86\tC\xa0u\xdaWp\xbei#-\x9d\xb6p\xf3D|;m\x0cq\x1d\x0c\xa4hB\x14\xd8\xb1;\xee\x97\x17\xfc\xf1\xb3\xff\x00P\xae?\xb5\x9b\xb3\x1d\x17\x86\xb4\xa9=\xf3P\xe5&m_\xbb7\x1d\xf7\xf6l\x9f= \xea#\xa1\xd3\xe5\x8d\x1c\xb0U\x0b\x8aM)6\xb3\x89J\xd0\x06\xff\x00U)H\x1f\xab\x15\xde\xbbD\xa6\xd4\xbbF\xd7\xa3Q\xd2\xe2)i\xaa\xba\xb4\x87\xde/)\x1e?\x1aJ\xce\xeb\xb2\x8a\x86\xa3r@\xb9\xbe\x19a\xb2\x06\x99o\xf4\xdf\xc2\xff\x00t-T\xaf\x8e6D\xdf\xf9\xb8\x03\xc6\xda\x9f\x1d\xff\x00\x95\xd8>\xca0\x857\xb3\xceRcR\x95t<\xab\xa8\x1f\xef\x96:\xfb\x0e\x1a\x96+77\xb7\xb3\x00\xfc\x01\x80\xe4\x0e\x07\xe4\x86\xdeIC\xaeS\x11!@\xf3\xfaU)\xdf\xf7\x8c\x1b\x95$u>\xeb\xe06\xe6\x16N9\x95\xe3\x89;\xd5a\xff\x00\xdb\x9f\xd4p"\xa4\xe9\x1b\x9d\xecG\xe5\x82\x9e%\xab\xfa\xd6\x17\x9f\xc9\x95\xfa\x8e\x05\x1c:\x9bY\xfd\xd5t\xf6\x1cD\xe3\x19\xd7\xcd\xcf\xd0\'\x18g\xf8\x91\xfb\xdeS3/*\xf9v\x9e/\x7f\xa1N\x078\xc7$G\xe1\xb5b\xc4\xa5J@H \x7f\x10\xfc6\xc4\xf6]XV\\\x80G\xf7)\xc4\'\x16\xa1*w\r\xeb\x89@\x05h\x8f\xde[\xcc\x05\x02\x7f\x0cR\xb8\x93Jm\xf4\xfa$l\x00U\x0b\xfd^\xaa\xb3pJ\x84)\xe2\x05L\x0b.[E\xed_|\x82?\x0f\xc7\x166\x1dMR\xf4!\xb2.v\xc2G\x84\xc9S\xf9>;zH\\\t.\xc6"\xd6:J\x8a\x87\xf3\xc4\xc0\xcc\x15L\x95\x9b\xcdD\xb1"\xb1G\x92\xd9K\xf0\xda?H\xca\xd3\xb8SC\xed\\\\\x14\xf5 \x11\xd6\xfc\xd1\xc9f\x00\x15EDn\x95\xd6h\xb9\xdc\x9c\xe2\xb5\n\x93*<y\xce:\xdb\xb2\x16\x1bi\xce\xe9JoQ\xfd\xe5\x01d\xfb\xed\x8d\x9c\xe5Ve\x8aS\x8c\xb4\xee\xb5\x91\xa4\x1f\xcf\x01\x94\xfe\'e\\\xf3K&\x9fPG\xd2\x02\x80\x1e\xf0\xef\xc8\x8b\xde\xd7\x06\xe0\x8b\xecE\x8d\xb1\x1f\\\xc9\xceTZ\x86\xfb5\x89l\xf7k\x0e)m;\xa9.[\xec\xa8r)>Xu\xb6\xf0\xd3\xb3\x9aK\xd0\x06\xc8\xd35\xdaG\x15\'Gp\x95\x90v<\xec|\xba`\x9d\x86\x1bu\xb1{\x1d\xb7\xc0t&S\x0c\xee\xf9u\xd2n\xa5\x11o\xc3\xa6&\xd9\xa8\x86\xdb \xaa\xf6\x1c\xce;\x86F\xb4X\xad\x9f\x16\xde`\xa0\xfe(C\x82\xd5"G\x81\x17 \xdbkb\x8ffX\xe8\x91\\\x8c\x96\x90\x08L\xcdg\xd8\x12\xbb\x93\xf8b\xda\xf1\xa30\xa1\x9a[\xa0(\x95\xa8\x10\x94\xa7r}\x83\xae\x11r\xf8o\\\xa4\xe4\tu\xc9\xd4w\xe1!\xf7\x90\xe2\xa7<\x93\xa7\xbb\x0bN\x94 s\xb7\x8bu\x10\x01&\xc0\x9eXC[3Z\xfe\x01\x1e\xc8\x83\x186\x8ei)NY\x8b\x9e"H\xd5\xa86\xde\xe4mk\x04\xfb\xfe\xce\x11\xdc\x04\xc9\x13k\xf5\xa6Ld)u\x1a\x9b\xe8\x83\x15$s\xd6Bu_\xda\xae~\x98vBi\xb9y\x82F\xc1\r\x08\xee\x15,\xf2F\xa0\x01?\xab\xe1\x8b\x15\xd8\x87\xb3\xb2\xe9\xefE\xce\xd5\xa8\x8af3\x03\xfa\xa2,\x84X\xd8\'J\x1d \xee-\xcc_\x997\xe9\x82i\xa7,c\xe3\x1a\xba\xdeWK\xa7\x889\xed\x90\xe8\xdb\xf9\xab\x93\x02\x9c\xd5\x0e\x8b\x02\x9b\x1c\xff\x00G\x87\x1d\xb8\xc8\xff\x00*\x12\x12?,a[\xe9J\xad\xaa\xd8\xdb\x98\xed\x92I\xe89`N\xa5QSo\xe9\x07\x97=\xaf\x8d\xcb\xc3FHV\xb0\xb9Nq5\xd0*pO\xfe\x9d_\xab\x02\xcd\xaf\xc0\xe8;o{\xe0\xef8\xe4\xaa\xd5~\xa5\x11Q\x18d6\xd3J\n[\xcf\xa5\t\xd5\xaa\xe0\x0ed\xfc13G\xc8tl\xbe\x88\xeeT\xdart\xa1\xa4\xad\xe7\x0f\xd0%_\xe4\x1ff\xfdM\xfdm\x84ux]Eet\xb2\x0e\xab.3:h4\xe3\xfbv\xae\xe9q\x08i\xa9\x18\xd2n\xee\x03]V\x9eZ!yb\x05\x88\xb1ho\xf1\xc6\xdd^3r\xa93#?e3!\x95\xb2\xa0yx\x85\xbf\x9e&fw,\xd54\xa9\xa4w\x0b\x176\x16\x02\xfc\xb6\x1e\xfcE\xe6\x98\x0bK)\x91\x14\x95\xc6E\xfb\xc6\xb9\x94\x8f\xdf\x1e~\xa3\xcb|:u9\x8a2\xcdvE\x92\xb6\xca%\x94\x13\x96\xd1\xba\xab\xbc6fF\\\xceul\xbf1\x05\xb5H\x1d\xf3W;-m\xf8\\\x03\xdb\xb2\xbe8aV\xa9\x06K`\xb6\x14\x87\x01\x05+A\xb2\x92\xa1\xb8#\xd4\x1cGq7-\xb9\xf3\x8cj\xd58\xe9\x9d\x1d\xc4\xc8mH\x1b\x95\x0ec\xd4(m\xeb\xb6\'\xa8\xf9\x9e\x1dV\x0bR\x12@\xd6\x80K}Rz\x8ff\x11Qu\\aq\xcch\xad\xa5ys[3=\x94\xbc\xaeF\x81P\x93\xde\xd4\x10\xed1\xe4\xac\xadB\x10\x01\xa5(\x8f\x12\x8bD\x11\xb9\xdfm\xef\xd7\x02\xb1\xe9\xd5\xdaEik\xcay\x92[\x8c\xb9\xb2b9M\ti<\xb6+\xd7\xcb\x9f0y\xe1\xd7=\x10_\nQJ\x16m\xd4b\x1aB\xe3E\x04\xa0\xa5\x03\x9e\xdb\x0cQ>g\xb4Y\xc0\x15\xf0U\x876\xc5\xaa\x12\x95K\xcdI\xaf5>\xb3]\x88\xfca\x18\xa1pa\xc2\r\x00\xe9"\xca\xd6TJ\xb6\xd5\xe47\x1bbj\xb5\x98\x91N\x86\xe3\x8aPJR.TN\xd8\xd2\x87*ve\xa8\xa6\x99C\x86\xedRz\x92U\xdd1k%#\x9a\x94\xa3\xb2S\xb8\xdc\x9e\xbex&\x91\xc3X\x99a\xb8RsMm\xb8\xd5\tNZ)1K\x8cFZl\xa2\xae\xedV\xefm\xb0\xd4\xab\x0b\x91a{`=\xa789\xed\xb0\x03y \x0f\x12\x812\xc7\x1b\xdb\x1b\xff\x00Q\xd0\x00I\xe7`\t\xb0\xfd\xb8\xaf\x1c\x1c\xe1\xe2k\xb5\xd6\xb3\rz8[\xa1AQ!II!\xb6\xf7=\xe2\x81\x1c\xd5\xc8\x0e\x82\xf7\xdc\xdb\x12\xdd\xaee\xa1\xde\x08W\x84\x95\xb7\x14-L\xa1\xa4\xd8]\xe2\x97\x12~\x8cs\t\xb5\xc9&\xc7\x97\x9e\'2\xc1o/\xc6\xa7\xb9:\xa6\xddZ[\xce\x94.\xa3\xf2r\xcfz\xa0\x01\x04\xa0n\x08O;\xef~|\xf0\xb5\xed\xe3\x98"en\x19E\xa6w\x88v\xa5Z\x91\xde\x92\x14\x05\xd9ksa\xbf\x84\xa9i\xd8s;\xeflwS\x1cn\xa0\x01\xe2\xce\xc8\xeb\xc4\x8dm\x91\xf1\xb7v\xb2\xa2o\x88\xc5\t\x0e.\x01\xd6\x19\x102\x19\xda\xe0e\xcc\x03\xc4\\\xaa{\xd9\xc7+\xb5\x9b8\xb9I\x8b.:^\x8c\xb7\xc3\xae\xb4\xa4\xdd$4\x85:\xa0GQ\xbaE\x8e\xd8\xe8\xb3\r&3iJ@\x01#{\x0e\xb8\xa8\xfd\x88\xf2\xbb\xafV+\xb9\x85\xe4]\xb8\xd1\xc4d:\xb1r\xb7\x9eV\xb5X\xf4\xb2\x12\x9b\xff\x00\x98b\xda\xb8\xe7\xd1\xa8\xf5\xb7Lc\x10\xb0\xba\x7f1\xb9\rQ\x959\x97*$\x900\x95\xe3\x1f\x1c\xf2\xbf\x07^\xa5\x8c\xcdQM9U\x10\xe9\x8e\xd0V\x92R\xde\x80\xa2m\xea\xb1\xf8\xfa\xe1\x9f\x98\xaa\xcd\xc0mkY\xdf\xa9\xbf,rK\xb6\x87\x12cqS\x8e\x95w\x1e\x96\xb3I\xa2\x84\xd2ai\xfa\xa5M\xee\xf1\x1f}D{\x86\t\xa6\x8f\xe2\xa6\xe8\xef\x90\xcc\xdb\xdf\xbc\xd6S<\xd3\xc5\xb6\x06g!}\x17qY\xa9\xad%%D-**\x04\x1f,m\xa2\xb8\xdb@\tV,\xdc\x04\xbaE\xf4\x7f\x9b\xd3\xd7\xe3\x80\xec\xb7Tv\xa7Ma\xe7@\n#}<\xb1(\xb7\x14\x94\xa8\xf3"\xfe\xfcZ\xba\x10\xf1\x96D\xa5R\xd25\xaf,p\xcc"\xb7\x1ajb\xd5\xa8\x05\x05\'\xbbP\xebc\xc8\x8cEGuq\\[/(,\xb6\xb2\x80\xe0\x1b*\xdf\xcf\x182\xae\xb5L}iYK,0V\x96y\x80I\x00[\xc8\x0b\x9d\xbf,lJmh\xbd\x9c \x13r,-\x81]Mp\x1c\xec\x8eh\r\x9e\x8eC\t7\x19 |\xfbBM<\x07\xdbE\xe9\xf2\x15\xa4\x81\xc9\x95\x9f\xc9*<\xbc\x8e\xdc\x88\xc2\x8e\xa9\x97\xd5\x15\x0ew\x0bSZ\xd4W\xb1\xb6\x95u#\xca\xfc\xfe8\xb2N0\xdc\xe8\x0e\xc6\x96\x81!\x87\x93\xa1hP\xb5\xc1\xc2j\xabO\x10\xeaR\xe1\xa9\xc2\xf7p\xea\x9a\xef\x14,T\x01\xd8\xfbq+\x88a\xbd\x1b\xc3\xc6\xf5M\x87\xd6\xbbd\xc6\xedG\x98I\x8a\x8dG3BZ\x90\xd3\x89u\x1b\xd9N\'\x7f\xc3\x10SjU\xf7Q\xaad\xae\xed=R\xd8\xb0\xc3~\xa3NeM\xa8\xe9\xc2\xcb5\xa7[\xe8c\x92I7\xc2w\xb5\xe3W\'"P\xed\x02\xb3\x1d\x8erx\xa6\xe4)\xb9\x92@S\x93k2T\x948\xb3r\x18h\x94$\x0f+\xaf\xbc?\x0f,c\xe3\x9d31U8\x8b\x1e,6\xdev3\xd4\xf6\x15O\xd4\xea[\x8c\x89h}GS\x97#U\x89A\xb0\xbe\xc0\x1b`\xf7\xb3\xa2R\x8e\x0bed\xa1:R\x18X\xb7\xafz\xbb\x9f\x7f?~\x0f*\x94\x885\xa8\xa6=B\x1b\x13X?\xd9\xbe\xd8Zw\x16;\x1fBG\xbf\x15\x93a\x9f\x19\x86\xc7\x0cn\xd99\x1ed\x83{\xeb\xc4\xee66PQb\xa6\x87\x15\x96\xa5\xcd\x0e\xcc\x8c\xf7n\x07v\x96\x1b\xf3H\x1e\x19\xe4\xc9\x99\x9d\xc9+\x8c\xdcH\x94\xda}A\xa0\x87\xd9yN\xb6\xe3\x89kD\xa4\'{\xfdu(s#\xc278\xa7\x1d\xab\xf3\xa9\xe2\xbf\x19~n\xa4!r\xe8\xf4\xd2)\x94\xd0\x83\xa9N%\x95iZ\xbc\xc8S\xaaP\x07\xedY6\xe5\x8b\xd9\xdao8H\xe1\x8f\x06\xe5"\x82\xd3p\x1c\x96\xa4\xd3Y\\p\x1b\x11P\xb0AR\x00\x16\x04\x0b\x81kZ\xf7\xe9\x84\x1ffN\x07\xd0\xa0dJ\x16~\x91\xfd6\xb5Q:\xd9\xef\x1b\x01\x11\x105\xa5\xb4 u\xd3bnw*Q>\xc4\x15\xb7\x8c\xc5\x87\xb4\xdc\xb0\x0b\x9bXi\xbb\x90\xf1\xcbM\xcei\xaaEL\x8f\xaf\x90Y\xae6h\xd4\xe9\x99\'\x89\xb6\xbc\xf8\xa6\x07\t\xb2(\xe1\xae@\x81HZS\xf2\xe5^L\xc5\xa4}g\xd7mC\xee\x80\x94\xfd\xdc\x15)\xcdM(zc\xdc\xb5\x14\xa7P\xe6q\x1c]>!\xe7\x8d\x0fW\xaa\x11b\xee%\xc5+x\xdf-\xca^N\xadU\x06\xcdS\xe1\xbd1\xc5^\xc3Ch+#\xdf\xa6\xde\xfcqC4Mzl\x96\xdc\x91\xe2y\xe2\xb9.\x1f5\xadD\x93\xf8\x0cv\x0f\xb6\xcdY\xea/f\xac\xec\xf4}\x9c\x92\xd4xJ>HvCh_\xfaI\x1e\xfcq\xda\xbb\xf4\x93\xaf`<\x08\xdb\xee\x8c=\xc1"\r{\xe4\xe3\xe9\xfc\xa5x\xcb\xcb\xa1k\x07\xbfv_\xff\xd9'



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

    #爬虫获取远程图片并保存_建立本地图片路径
    def saveSpiderImage(self):
        tStr = self.getTimeStr()   #获取当前时间串
        currentny = self.getTimeStrNY()   #获取当前时间的年月
        firedir = r'%s/media/report/%s/screenshots/' % (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),currentny)
        self.createdir(firedir)
        path = '%s%s_%s.png' % (firedir,self.prenum,tStr)
        return path

    #爬虫获取远程图片并保存_获取远程图片
    def get_remote_image(self,imgremotesrc):
        try:
            import requests
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Remote Address': '104.26.1.213:443',
                'Referrer Policy': 'no-referrer-when-downgrade',
            }
            for i in range(1,6):
                try:
                    imagewe = requests.get(url=imgremotesrc,headers=headers,timeout=5,verify=False)
                    break
                except Exception as e:
                    print("获取远程图片（头像）请求超时异常：%s" % e)
                    print("第%s次请求超时..."% i)
                    continue
            image_content = imagewe.content
            print(image_content)
        except Exception as e:
            print("获取远程图片失败,暂时不获取图片")
            print("以默认图片代替")
            image_content = self.init_image
        return image_content


    #爬虫获取远程图片并保存_把第三方地址的图片转化为本地图片和返回远程图片
    def get_image_from_imgsrc(self,imgsrc):
        image_list = []
        image_content = self.get_remote_image(imgsrc)
        print(image_content)
        image_list.append(image_content)
        if image_content == self.init_image:
            print("获取远程图片失败,暂时不获取图片")
            image_xpath = "erroraddress"
            print("使用赋予的字符串做路径，路径为：%s" % image_xpath)
        else:
            imageend = self.saveSpiderImage()
            with open(imageend, 'wb') as f:
                f.write(image_content)
            imageend_list = imageend.split("media")
            from wanwenyc.settings import DJANGO_SERVER_YUMING
            image_xpath = "%s/media%s"%(DJANGO_SERVER_YUMING,imageend_list[1])
            print("转化成的本地图：%s" % image_xpath)
        # image_xpath = "%s/media/report/202004/screenshots/screenpicture_20200413102350.png" % DJANGO_SERVER_YUMING
        image_list.append(image_xpath)
        return image_list

    #获取补传封面图片
    def get_back_front_cover_img(self):
        front_cover_img = self.get_image()
        front_cover_img_url = front_cover_img.attrs["src"]
        print(front_cover_img_url)
        image_list = self.get_image_from_imgsrc(front_cover_img_url)
        print("封面图内容和本地地址：")
        # image_xpath = "%s/media/report/202004/screenshots/screenpicture_20200413102329.png"% DJANGO_SERVER_YUMING
        # image_xpath = "%s/media/report/202004/screenshots/screenpicture_20200413102329.png"% DJANGO_SERVER_YUMING
        return image_list

    #获取封面图片
    def get_front_cover_img(self):
        front_cover_img = self.get_image()
        front_cover_img_url = front_cover_img.attrs["src"]
        print(front_cover_img_url)
        try:
            import requests
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Remote Address': '104.26.1.213:443',
                'Referrer Policy': 'no-referrer-when-downgrade',
            }
            for i in range(1,6):
                try:
                    imagewe = requests.get(url=front_cover_img_url, headers=headers,timeout=5,verify=False)
                    break
                except Exception as e:
                    print("获取封面图请求超时异常：%s" % e)
                    print("第%s次请求超时..."% i)
                    continue

            image_content = imagewe.content
            print(image_content)
            imageend = self.saveSpiderImage()
            with open(imageend, 'wb') as f:
                f.write(image_content)
            imageend_list = imageend.split("media")
            from wanwenyc.settings import DJANGO_SERVER_YUMING
            image_xpath = "%s/media%s"%(DJANGO_SERVER_YUMING,imageend_list[1])
        except Exception as e:
            print("获取封面图片失败,暂时不获取图片")
            image_xpath = "erroraddress"
        print("封面图：%s" % image_xpath)
        # image_xpath = "%s/media/report/202004/screenshots/screenpicture_20200413102329.png"% DJANGO_SERVER_YUMING
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
                print(one_href)
        return direcotr_and_studio_and_label_list #返回列表

    #获取导演，制作商，发行商,系列
    def get_direcotr_and_studio_and_label_and_series(self):
        # 使用xpath的方法获取类名为col-md-3 info的div标签下的所有P标签的a标签元素集合
        direcotr_and_studio_and_label_and_series_eles = self.response.html.xpath("//div[@class='col-md-3 info']/p/a")
        direcotr_and_studio_and_label_and_series_list = []
        direcotr_list = []
        studio_list = []
        label_list = []
        series_list = []
        for one in direcotr_and_studio_and_label_and_series_eles:
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
                direcotr_one_list = []
                direcotr_one_list.append(one_text)
                direcotr_one_list.append(one_href)
                direcotr_list.append(direcotr_one_list)

            elif "studio" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_STUDIO.txt"%base_dir)
                ht.add_content(one_href)
                studio_one_list = []
                studio_one_list.append(one_text)
                studio_one_list.append(one_href)
                studio_list.append(studio_one_list)
            elif "label" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_LABEL.txt"%base_dir)
                ht.add_content(one_href)
                label_one_list = []
                label_one_list.append(one_text)
                label_one_list.append(one_href)
                label_list.append(label_one_list)
            elif "series" in one_href:
                ht = HandleTxt("%s/ONEWEBURL_SERIES.txt"%base_dir)
                ht.add_content(one_href)
                series_one_list = []
                series_one_list.append(one_text)
                series_one_list.append(one_href)
                series_list.append(series_one_list)
            else:
                ht = HandleTxt("%s/ONEWEBURL.txt"%base_dir)
                ht.add_content(one_href)
                print(one_href)
        direcotr_and_studio_and_label_and_series_list.append(direcotr_list)
        direcotr_and_studio_and_label_and_series_list.append(studio_list)
        direcotr_and_studio_and_label_and_series_list.append(label_list)
        direcotr_and_studio_and_label_and_series_list.append(series_list)
        print("导演，制作商，发行商,系列:")
        print(direcotr_and_studio_and_label_and_series_list)
        return direcotr_and_studio_and_label_and_series_list #返回列表

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
            start_photo_list = self.get_image_from_imgsrc(one_href)
            start_photo_image_content = start_photo_list[0]
            star_and_photo_one_list.append(start_photo_image_content)
            local_image_url = start_photo_list[1]
            print(local_image_url)
            star_and_photo_one_list.append(local_image_url)
            star_and_photo_list.append(star_and_photo_one_list)
        return star_and_photo_list #演员数据依次为演员名称，演员图片内容，演员本地图片地址

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

    #获取时长
    def get_long_time(self):
        # 使用xpath的方法获取类名为col-md-3 info的div标签下的第一个P标签下的第二个span元素集合
        respose_text = self.get_obj_full_text(self.response)
        long_time_re = self.get_re_content(pipei=".*長度:.*", content=respose_text)
        # print(long_time_re)
        long_time_re_list = str(long_time_re).split("長度:")[1]
        # print(long_time_re_list)
        long_time_re_list_two = str(long_time_re_list).split("<")[1]
        # print(long_time_re_list_two)
        long_time_re_list_three = str(long_time_re_list_two).split(">")[1]
        # print(long_time_re_list_three)
        long_time = long_time_re_list_three.strip(" ")
        print(long_time)
        return long_time



    #获取下载地址链接
    def get_down_load(self):
        try:
            #使用ajax请求获取链接地址
            print("进入下载函数")
            gid_and_uc_and_img_list = self.get_gid_and_uc_and_img()
            ajax_url = "https://www.busdmm.one/ajax/uncledatoolsbyajax.php?gid=%s&lang=zh&img=%s&uc=%s&floor=236" %(gid_and_uc_and_img_list[0],gid_and_uc_and_img_list[2],gid_and_uc_and_img_list[1])
            headers = {
                # 'x-requested-with': 'XMLHttpRequest',  #这个说明是ajax请求，没有这个，也会识别
                # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                'referer': '%s' % self.web_url,  # 此处要根据来源网址做出相应，没有就不会获取到相应内容
            }
            for i in range(1,6):
                try:
                    print("进行ajax请求")
                    myresponse = self.hs.get(ajax_url, headers=headers,timeout=5,verify=False)
                    break
                except Exception as e:
                    print("获取下载链接请求超时异常：%s" % e)
                    print("第%s次请求超时..."% i)
                    continue
            # print(myresponse.status_code)
            # print(myresponse.content)
            # print(myresponse.text)
            links_list = myresponse.html.absolute_links  #获取所有链接的绝对路径
            print("即将打印链接：")
            for i in links_list:
                print(i)
        except Exception as e:
            print("获取下载链接出现问题：%s"% e)
            print("暂无下载链接")
            links_list = ['errorlist']
        return links_list

class RunSpiderBase(object):
    def __init__(self,yuming,prenum,range_num_down,range_num_up):
        self.yu_ming = yuming   #网址域名
        self.prenum = prenum    #编号基础内容
        self.range_num_down = int(range_num_down)   #编号之编号下限
        self.range_num_up = int(range_num_up)  # 编号之编号上限

    def run(self):
        error_url_list = []
        for i in range(self.range_num_down, self.range_num_up):
            if len(str(i)) == 1:
                fcount_i = '00%s' % i
            elif len(str(i)) == 2:
                fcount_i = '0%s' % i
            else:
                fcount_i = i

            url = "%s/%s-%s" % (self.yu_ming,self.prenum,fcount_i)

            from spiderdata.models import SpiderData
            is_exist_url_count = SpiderData.objects.filter(splider_url=url).count()
            print(is_exist_url_count)
            if is_exist_url_count != 0:
                print("已经爬取过网站：%s" % url)
            else:
                try:
                    sb = SpiderBase(url)
                    # 获取标题
                    splider_title = sb.get_splider_title()
                    print("标题：")
                    print(splider_title)
                    # 获取封面图路径
                    front_cover_img_list = sb.get_back_front_cover_img()
                    front_cover_img_local_xpath = front_cover_img_list[1]
                    back_front_cover_img = front_cover_img_list[0]
                    print("封面图路径：")
                    print(front_cover_img_local_xpath)
                    print("封面图内容：")
                    print(back_front_cover_img)
                    # 获取编号
                    prenum = sb.get_prenum()
                    print("编号：")
                    print(prenum)
                    long_time = sb.get_long_time()
                    print("时长：")
                    print(long_time)
                    # 获取导演，制作商，发行商,系列
                    direcotr_and_studio_and_label_and_series_list = sb.get_direcotr_and_studio_and_label_and_series()
                    print("导演，制作商，发行商,系列：")
                    print(direcotr_and_studio_and_label_and_series_list)
                    # 获取类别和演员
                    genres_and_stars_list = sb.get_genres_and_stars()
                    print("类别和演员：")
                    print(genres_and_stars_list)
                    # 获取演员和头像
                    star_and_photo_list = sb.get_star_and_photo()
                    print("演员和头像:")
                    print(star_and_photo_list)

                    # 进行ajax异步请求获取下载链接
                    print("获取下载链接")
                    sb2 = SpiderBase(url)
                    # 获取下载链接
                    down_load_list = sb2.get_down_load()
                    print("下载链接:")
                    print(down_load_list)

                    # 保存数据前，先保存导演，制作商，发行商，系列：
                    from spiderdata.models import SpiderDirector, SpiderStudio, SpiderLabel, SpiderSeries
                    for i in range(0, 4):
                        # #保存导演
                        # ------------------------------------------------------------------------------
                        if i == 0:  # 为导演
                            director_all_list = direcotr_and_studio_and_label_and_series_list[i]
                            for director_one_list in director_all_list:
                                director_save = director_one_list[0]
                                is_exist_director_count = SpiderDirector.objects.filter(director=director_save).count()
                                if is_exist_director_count != 0:
                                    print("导演[%s]已经存在" % director_save)
                                else:
                                    spiderdirector = SpiderDirector()
                                    spiderdirector.director = director_save
                                    spiderdirector.director_url = director_one_list[1]
                                    spiderdirector.save()
                                    print("已经成功保存导演【%s】到相应数据库中" % director_save)
                            print("已经处理完所有导演")
                        # 保存制作商
                        # ------------------------------------------------------------------------------
                        elif i == 1:  # 为制作商
                            studio_all_list = direcotr_and_studio_and_label_and_series_list[i]
                            for studio_one_list in studio_all_list:
                                studio_save = studio_one_list[0]
                                is_exist_studio_count = SpiderStudio.objects.filter(studio=studio_save).count()
                                if is_exist_studio_count != 0:
                                    print("制作商[%s]已经存在" % studio_save)
                                else:
                                    spiderstudio = SpiderStudio()
                                    spiderstudio.studio = studio_save
                                    spiderstudio.studio_url = studio_one_list[1]
                                    spiderstudio.save()
                                    print("已经成功保存制作商【%s】到相应数据库中" % studio_save)
                            print("已经处理完所有制作商")
                        # 保存发行商
                        # ------------------------------------------------------------------------------
                        elif i == 2:  # 为发行商
                            label_all_list = direcotr_and_studio_and_label_and_series_list[i]
                            for label_one_list in label_all_list:
                                label_save = label_one_list[0]
                                is_exist_label_count = SpiderLabel.objects.filter(label=label_save).count()
                                if is_exist_label_count != 0:
                                    print("发行商[%s]已经存在" % label_save)
                                else:
                                    spiderlabel = SpiderLabel()
                                    spiderlabel.label = label_save
                                    spiderlabel.label_url = label_one_list[1]
                                    spiderlabel.save()
                                    print("已经成功保存发行商【%s】到相应数据库中" % label_save)
                            print("已经处理完所有发行商")
                        # 保存系列
                        # ------------------------------------------------------------------------------
                        elif i == 3:  # 为系列
                            series_all_list = direcotr_and_studio_and_label_and_series_list[i]
                            for series_one_list in series_all_list:
                                series_save = series_one_list[0]
                                is_exist_series_count = SpiderSeries.objects.filter(series=series_save).count()
                                if is_exist_series_count != 0:
                                    print("系列[%s]已经存在" % series_save)
                                else:
                                    spiderseries = SpiderSeries()
                                    spiderseries.series = series_save
                                    spiderseries.series_url = series_one_list[1]
                                    spiderseries.save()
                                    print("已经成功保存系列【%s】到相应数据库中" % series_save)
                            print("已经处理完所有系列")
                    print("已经处理完所有导演，制作商，发行商，系列")

                    # 保存数据前，先保存类别，演员：
                    # 保存类别
                    for genre_one_list in genres_and_stars_list[0]:
                        from spiderdata.models import SpiderGenre

                        genre_save = genre_one_list[0]
                        is_exist_genre_count = SpiderGenre.objects.filter(genre=genre_save).count()
                        if is_exist_genre_count != 0:
                            print("类别[%s]已经存在" % genre_save)
                        else:
                            spidergenre = SpiderGenre()
                            spidergenre.genre = genre_save
                            spidergenre.genre_url = genre_one_list[1]
                            spidergenre.save()
                            print("已经成功保存类别【%s】到相应数据库中" % genre_save)

                    # 保存演员
                    for star_one_list in genres_and_stars_list[1]:
                        from spiderdata.models import SpiderStar

                        star_save = star_one_list[0]
                        is_exist_star_count = SpiderStar.objects.filter(star=star_save).count()
                        if is_exist_star_count != 0:
                            print("演员[%s]已经存在" % star_save)
                        else:
                            spiderstar = SpiderStar()
                            spiderstar.star = star_save
                            print("star_one_list[1]:")
                            print(star_one_list[1])
                            spiderstar.star_url = star_one_list[1]
                            spiderstar.save()
                            print("已经成功保存演员【%s】到相应数据库中" % star_save)

                    # 保存演员头像到相应的数据库
                    for star_and_photo_one_list in star_and_photo_list:
                        from spiderdata.models import SpiderStar
                        star_search = star_and_photo_one_list[0]
                        star_find_list = SpiderStar.objects.filter(star=star_search)
                        for star_one in star_find_list:
                            star_one.star_photo = star_and_photo_one_list[2]  # 保存本地路图片路径

                            start_photo_name = "%s.png" % star_search
                            from django.core.files import File  # 使用django的File文件类
                            from io import BytesIO  # BytesIO读取字节类型数据使用
                            start_photo_image_content = star_and_photo_one_list[1]  # 远程获取的演员图片，字节类型
                            pre_back_start_photo = File(BytesIO(start_photo_image_content))
                            star_one.back_start_photo.save(name=start_photo_name,
                                                           content=pre_back_start_photo)  # 保存图片到ImageField实例中

                            star_one.save()
                            print("已经成功保存演员头像【%s】到相应数据库中" % star_and_photo_one_list[0])

                    # 保存除下载链接外的数据
                    # 保存数据到数据库
                    spiderdata = SpiderData()
                    print("实例化数据库")
                    # 保存url
                    spiderdata.splider_url = url
                    print("保存url")
                    # 保存title
                    spiderdata.splider_title = splider_title
                    print("保存title")
                    # 保存封面图
                    spiderdata.front_cover_img = front_cover_img_local_xpath
                    fengmian_image_name = "%s.png" % prenum
                    from django.core.files import File
                    from io import BytesIO
                    pre_back_front_cover_img = File(BytesIO(back_front_cover_img))
                    spiderdata.back_front_cover_img.save(name=fengmian_image_name,
                                                         content=pre_back_front_cover_img)  # 保存图片到ImageField实例中
                    print("保存封面图")
                    # 保存编号
                    spiderdata.prenum = prenum
                    print("保存编号")
                    spiderdata.long_time = long_time
                    print("保存时长")
                    spiderdata.save()

                    # 处理多对多的保存,多对多可以保存成功的前提是两个都已经有有效的id
                    spiderdata_manytomany_list = SpiderData.objects.filter(splider_url=url)
                    for spiderdata_manytomany in spiderdata_manytomany_list:
                        # 保存导演，制作商，发行商
                        # 保存导演
                        director_all_list = direcotr_and_studio_and_label_and_series_list[0]
                        for director_one_list in director_all_list:
                            director_save = director_one_list[0]
                            print("director_save:")
                            print(director_save)
                            sd_director_list = SpiderDirector.objects.filter(director=director_save)
                            for sd_director in sd_director_list:
                                print("sd_director:")
                                print(sd_director)
                                spiderdata_manytomany.director.add(sd_director)
                            print("多对多保存导演")
                        print("多对多保存所有导演完成")
                        # 保存制作商
                        studio_all_list = direcotr_and_studio_and_label_and_series_list[1]
                        for studio_one_list in studio_all_list:
                            studio_save = studio_one_list[0]
                            sd_studio_list = SpiderStudio.objects.filter(studio=studio_save)
                            for sd_studio in sd_studio_list:
                                spiderdata_manytomany.studio.add(sd_studio)
                            print("多对多保存制作商")
                        print("多对多保存所有制作商完成")
                        # 保存发行商
                        label_all_list = direcotr_and_studio_and_label_and_series_list[1]
                        for label_one_list in label_all_list:
                            label_save = label_one_list[0]
                            sd_label_list = SpiderLabel.objects.filter(label=label_save)
                            for sd_label in sd_label_list:
                                spiderdata_manytomany.label.add(sd_label)
                            print("多对多保存发行商")
                        print("多对多保存所有发行商完成")
                        # 保存系列
                        series_all_list = direcotr_and_studio_and_label_and_series_list[1]
                        for series_one_list in series_all_list:
                            series_save = series_one_list[0]
                            for series_one_list in series_all_list:
                                series_save = series_one_list[0]
                                sd_series_list = SpiderSeries.objects.filter(series=series_save)
                                for sd_series in sd_series_list:
                                    spiderdata_manytomany.series.add(sd_series)
                                print("多对多保存系列")
                        print("多对多保存所有系列完成")

                        # 保存类别
                        for genre_one_list in genres_and_stars_list[0]:
                            from spiderdata.models import SpiderGenre
                            genre_save = genre_one_list[0]
                            sd_genre_list = SpiderGenre.objects.filter(genre=genre_save)
                            for sd_genre in sd_genre_list:
                                spiderdata_manytomany.genre.add(sd_genre)
                        print("保存类别")

                        # 保存演员
                        for star_one_list in genres_and_stars_list[1]:
                            from spiderdata.models import SpiderStar
                            star_save = star_one_list[0]
                            sd_star_list = SpiderStar.objects.filter(star=star_save)
                            for sd_star in sd_star_list:
                                spiderdata_manytomany.star.add(sd_star)
                        print("保存演员")
                        spiderdata_manytomany.save()

                    # 保存下载地址
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



if __name__ == "__main__":
    # yuming_list = ["https://www.javbus.com","https://www.busdmm.one","https://www.dmmbus.zone","https://www.seedmm.one"]
    # pre_number = ["HUNT","HUNTA","MKMP","YMDD","NASH","ZMEN","UMSO","MDTM","MDBK","BAZX","NASH","BAZX","BOKD","XRW","BNJC"]
    yuming_out = "https://www.busdmm.one"
    prenum_out = "HUNTA"
    range_num_down_out = 35
    range_num_up_out = 100

    rsb = RunSpiderBase(yuming=yuming_out,prenum=prenum_out,range_num_down=range_num_down_out,range_num_up=range_num_up_out)
    rsb.run()

    #
    # yuming = "https://www.busdmm.one"
    # error_url_list=[]
    # for i in range(10,100):
    #     if len(str(i)) == 1:
    #         fcount_i = '00%s' % i
    #     elif len(str(i)) == 2:
    #         fcount_i = '0%s' % i
    #     else:
    #         fcount_i = i
    #
    #     url = "https://www.busdmm.one/HUNTA-%s" % fcount_i
    #
    #     from spiderdata.models import SpiderData
    #     is_exist_url_count = SpiderData.objects.filter(splider_url=url).count()
    #     print(is_exist_url_count)
    #     if is_exist_url_count != 0:
    #         print("已经爬取过网站：%s" % url)
    #     else:
    #         try:
    #             sb = SpiderBase(url)
    #             #获取标题
    #             splider_title = sb.get_splider_title()
    #             print("标题：")
    #             print(splider_title)
    #             # 获取封面图路径
    #             front_cover_img_list = sb.get_back_front_cover_img()
    #             front_cover_img_local_xpath = front_cover_img_list[1]
    #             back_front_cover_img = front_cover_img_list[0]
    #             print("封面图路径：")
    #             print(front_cover_img_local_xpath)
    #             print("封面图内容：")
    #             print(back_front_cover_img)
    #             # 获取编号
    #             prenum = sb.get_prenum()
    #             print("编号：")
    #             print(prenum)
    #             # 获取导演，制作商，发行商,系列
    #             direcotr_and_studio_and_label_and_series_list = sb.get_direcotr_and_studio_and_label_and_series()
    #             print("导演，制作商，发行商,系列：")
    #             print(direcotr_and_studio_and_label_and_series_list)
    #             # 获取类别和演员
    #             genres_and_stars_list = sb.get_genres_and_stars()
    #             print("类别和演员：")
    #             print(genres_and_stars_list)
    #             # 获取演员和头像
    #             star_and_photo_list = sb.get_star_and_photo()
    #             print("演员和头像:")
    #             print(star_and_photo_list)
    #
    #             # 进行ajax异步请求获取下载链接
    #             print("获取下载链接")
    #             sb2 = SpiderBase(url)
    #             # 获取下载链接
    #             down_load_list = sb2.get_down_load()
    #             print("下载链接:")
    #             print(down_load_list)
    #
    #             #保存数据前，先保存导演，制作商，发行商，系列：
    #             from spiderdata.models import SpiderDirector,SpiderStudio, SpiderLabel,SpiderSeries
    #             for i in range(0,4):
    #                 # #保存导演
    #                 # ------------------------------------------------------------------------------
    #                 if i==0: #为导演
    #                     director_all_list = direcotr_and_studio_and_label_and_series_list[i]
    #                     for director_one_list in director_all_list:
    #                         director_save = director_one_list[0]
    #                         is_exist_director_count = SpiderDirector.objects.filter(director=director_save).count()
    #                         if is_exist_director_count != 0:
    #                             print("导演[%s]已经存在" % director_save)
    #                         else:
    #                             spiderdirector = SpiderDirector()
    #                             spiderdirector.director = director_save
    #                             spiderdirector.director_url = director_one_list[1]
    #                             spiderdirector.save()
    #                             print("已经成功保存导演【%s】到相应数据库中" % director_save)
    #                     print("已经处理完所有导演")
    #                 # 保存制作商
    #                 # ------------------------------------------------------------------------------
    #                 elif i==1: #为制作商
    #                     studio_all_list = direcotr_and_studio_and_label_and_series_list[i]
    #                     for studio_one_list in studio_all_list:
    #                         studio_save = studio_one_list[0]
    #                         is_exist_studio_count = SpiderStudio.objects.filter(studio=studio_save).count()
    #                         if is_exist_studio_count != 0:
    #                             print("制作商[%s]已经存在" % studio_save)
    #                         else:
    #                             spiderstudio = SpiderStudio()
    #                             spiderstudio.studio = studio_save
    #                             spiderstudio.studio_url = studio_one_list[1]
    #                             spiderstudio.save()
    #                             print("已经成功保存制作商【%s】到相应数据库中" % studio_save)
    #                     print("已经处理完所有制作商")
    #                 # 保存发行商
    #                 # ------------------------------------------------------------------------------
    #                 elif i==2: #为发行商
    #                     label_all_list = direcotr_and_studio_and_label_and_series_list[i]
    #                     for label_one_list in label_all_list:
    #                         label_save = label_one_list[0]
    #                         is_exist_label_count = SpiderLabel.objects.filter(label=label_save).count()
    #                         if is_exist_label_count != 0:
    #                             print("发行商[%s]已经存在" % label_save)
    #                         else:
    #                             spiderlabel = SpiderLabel()
    #                             spiderlabel.label = label_save
    #                             spiderlabel.label_url = label_one_list[1]
    #                             spiderlabel.save()
    #                             print("已经成功保存发行商【%s】到相应数据库中" % label_save)
    #                     print("已经处理完所有发行商")
    #                 # 保存系列
    #                 # ------------------------------------------------------------------------------
    #                 elif i == 3:  # 为系列
    #                     series_all_list = direcotr_and_studio_and_label_and_series_list[i]
    #                     for series_one_list in series_all_list:
    #                         series_save = series_one_list[0]
    #                         is_exist_series_count = SpiderSeries.objects.filter(series=series_save).count()
    #                         if is_exist_series_count != 0:
    #                             print("系列[%s]已经存在" % series_save)
    #                         else:
    #                             spiderseries = SpiderSeries()
    #                             spiderseries.series = series_save
    #                             spiderseries.series_url = series_one_list[1]
    #                             spiderseries.save()
    #                             print("已经成功保存系列【%s】到相应数据库中" % series_save)
    #                     print("已经处理完所有系列")
    #             print("已经处理完所有导演，制作商，发行商，系列")
    #
    #             #保存数据前，先保存类别，演员：
    #             #保存类别
    #             for genre_one_list in genres_and_stars_list[0]:
    #                 from spiderdata.models import SpiderGenre
    #
    #                 genre_save = genre_one_list[0]
    #                 is_exist_genre_count = SpiderGenre.objects.filter(genre=genre_save).count()
    #                 if is_exist_genre_count != 0:
    #                     print("类别[%s]已经存在"% genre_save)
    #                 else:
    #                     spidergenre = SpiderGenre()
    #                     spidergenre.genre = genre_save
    #                     spidergenre.genre_url = genre_one_list[1]
    #                     spidergenre.save()
    #                     print("已经成功保存类别【%s】到相应数据库中"% genre_save)
    #
    #             #保存演员
    #             for star_one_list in genres_and_stars_list[1]:
    #                 from spiderdata.models import SpiderStar
    #
    #                 star_save = star_one_list[0]
    #                 is_exist_star_count = SpiderStar.objects.filter(star=star_save).count()
    #                 if is_exist_star_count != 0:
    #                     print("演员[%s]已经存在"% star_save)
    #                 else:
    #                     spiderstar = SpiderStar()
    #                     spiderstar.star = star_save
    #                     print("star_one_list[1]:")
    #                     print(star_one_list[1])
    #                     spiderstar.star_url = star_one_list[1]
    #                     spiderstar.save()
    #                     print("已经成功保存演员【%s】到相应数据库中"% star_save)
    #
    #             #保存演员头像到相应的数据库
    #             for star_and_photo_one_list in star_and_photo_list:
    #                 from spiderdata.models import SpiderStar
    #                 star_search = star_and_photo_one_list[0]
    #                 star_find_list = SpiderStar.objects.filter(star=star_search)
    #                 for star_one in star_find_list:
    #                     star_one.star_photo=star_and_photo_one_list[2]  #保存本地路图片路径
    #
    #                     start_photo_name = "%s.png" % star_search
    #                     from django.core.files import File  #使用django的File文件类
    #                     from io import BytesIO  # BytesIO读取字节类型数据使用
    #                     start_photo_image_content = star_and_photo_one_list[1] #远程获取的演员图片，字节类型
    #                     pre_back_start_photo = File(BytesIO(start_photo_image_content))
    #                     star_one.back_start_photo.save(name=start_photo_name,
    #                                                          content=pre_back_start_photo)  # 保存图片到ImageField实例中
    #
    #                     star_one.save()
    #                     print("已经成功保存演员头像【%s】到相应数据库中" % star_and_photo_one_list[0])
    #
    #             #保存除下载链接外的数据
    #             #保存数据到数据库
    #             spiderdata = SpiderData()
    #             print("实例化数据库")
    #             #保存url
    #             spiderdata.splider_url = url
    #             print("保存url")
    #             #保存title
    #             spiderdata.splider_title = splider_title
    #             print("保存title")
    #             #保存封面图
    #             spiderdata.front_cover_img = front_cover_img_local_xpath
    #             fengmian_image_name = "%s.png"%prenum
    #             from django.core.files import File
    #             from io import BytesIO
    #             pre_back_front_cover_img = File(BytesIO(back_front_cover_img))
    #             spiderdata.back_front_cover_img.save(name=fengmian_image_name,content=pre_back_front_cover_img) #保存图片到ImageField实例中
    #             print("保存封面图")
    #             #保存编号
    #             spiderdata.prenum = prenum
    #             print("保存编号")
    #             spiderdata.save()
    #
    #             #处理多对多的保存,多对多可以保存成功的前提是两个都已经有有效的id
    #             spiderdata_manytomany_list = SpiderData.objects.filter(splider_url=url)
    #             for spiderdata_manytomany in spiderdata_manytomany_list:
    #                 #保存导演，制作商，发行商
    #                 #保存导演
    #                 director_all_list = direcotr_and_studio_and_label_and_series_list[0]
    #                 for director_one_list in director_all_list:
    #                     director_save = director_one_list[0]
    #                     print("director_save:")
    #                     print(director_save)
    #                     sd_director_list = SpiderDirector.objects.filter(director=director_save)
    #                     for sd_director in sd_director_list:
    #                         print("sd_director:")
    #                         print(sd_director)
    #                         spiderdata_manytomany.director.add(sd_director)
    #                     print("多对多保存导演")
    #                 print("多对多保存所有导演完成")
    #                 #保存制作商
    #                 studio_all_list = direcotr_and_studio_and_label_and_series_list[1]
    #                 for studio_one_list in studio_all_list:
    #                     studio_save = studio_one_list[0]
    #                     sd_studio_list = SpiderStudio.objects.filter(studio=studio_save)
    #                     for sd_studio in sd_studio_list:
    #                         spiderdata_manytomany.studio.add(sd_studio)
    #                     print("多对多保存制作商")
    #                 print("多对多保存所有制作商完成")
    #                 # 保存发行商
    #                 label_all_list = direcotr_and_studio_and_label_and_series_list[1]
    #                 for label_one_list in label_all_list:
    #                     label_save = label_one_list[0]
    #                     sd_label_list = SpiderLabel.objects.filter(label=label_save)
    #                     for sd_label in sd_label_list:
    #                         spiderdata_manytomany.label.add(sd_label)
    #                     print("多对多保存发行商")
    #                 print("多对多保存所有发行商完成")
    #                 # 保存系列
    #                 series_all_list = direcotr_and_studio_and_label_and_series_list[1]
    #                 for series_one_list in series_all_list:
    #                     series_save = series_one_list[0]
    #                     for series_one_list in series_all_list:
    #                         series_save = series_one_list[0]
    #                         sd_series_list = SpiderSeries.objects.filter(series=series_save)
    #                         for sd_series in sd_series_list:
    #                             spiderdata_manytomany.series.add(sd_series)
    #                         print("多对多保存系列")
    #                 print("多对多保存所有系列完成")
    #
    #
    #                 #保存类别
    #                 for genre_one_list in genres_and_stars_list[0]:
    #                     from spiderdata.models import SpiderGenre
    #                     genre_save = genre_one_list[0]
    #                     sd_genre_list = SpiderGenre.objects.filter(genre=genre_save)
    #                     for sd_genre in sd_genre_list:
    #                         spiderdata_manytomany.genre.add(sd_genre)
    #                 print("保存类别")
    #
    #                 #保存演员
    #                 for star_one_list in genres_and_stars_list[1]:
    #                     from spiderdata.models import SpiderStar
    #                     star_save = star_one_list[0]
    #                     sd_star_list = SpiderStar.objects.filter(star=star_save)
    #                     for sd_star in sd_star_list:
    #                         spiderdata_manytomany.star.add(sd_star)
    #                 print("保存演员")
    #                 spiderdata_manytomany.save()
    #
    #             #保存下载地址
    #             for down_load in down_load_list:
    #                 from spiderdata.models import SpiderDownLoad
    #
    #                 sdl_sd_list = SpiderData.objects.filter(splider_url=url)
    #                 for sdl_sd in sdl_sd_list:
    #                     spiderdownload = SpiderDownLoad()
    #                     spiderdownload.spiderdata_id = sdl_sd.id
    #                     spiderdownload.down_load = down_load
    #                     spiderdownload.save()
    #                     break
    #
    #         except Exception as e:
    #             print("报错：%s" % e)
    #             error_url_list.append(url)
    #
    # print("失败网址：")
    # print(error_url_list)




