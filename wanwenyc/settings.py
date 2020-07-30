"""
Django settings for wanwenyc project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys   #导入sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #获取项目根目录
sys.path.insert(0,BASE_DIR)  #将项目根目录加入到python根目录中
sys.path.insert(0,os.path.join(BASE_DIR, 'apps'))  #配置apps路径
sys.path.insert(0,os.path.join(BASE_DIR, 'extra_apps'))  #配置extra_apps路径


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5tjx38wld=d74vhdm9l42tv625f5^fkd)=p4=ctdo5ztkimp-='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    #DEBUG为True，静态资源可以用，例如js样式，DEBUG为False则所有静态样式均不可用
# DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']  #在这里请求的host添加了*可以使用域名访问

AUTH_USER_MODEL = 'users.UserProfile'   #在setting中重载AUTH_USER_MODEL，用于自定义user模块


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',  # 注册xadmin
    'crispy_forms',  # 注册xadmin的依赖应用crispy_forms
    'users.apps.UsersConfig',  #注册user
    'testdatas.apps.TestdatasConfig', #注册testdatas
    'reportdatas.apps.ReportdatasConfig', #注册reportdatas
    'testapidatas.apps.TestapidatasConfig',#注册testapidatas
    'reportpageloadtime.apps.ReportpageloadtimeConfig',#注册testapidatas
    'dependallshow.apps.DependallshowConfig',#注册dependallshow
    'testupdatadb.apps.TestupdatadbConfig',#注册testupdatadb
    'shangbaoshuju.apps.ShangbaoshujuConfig', #注册shangbaoshuju
    'spiderdata.apps.SpiderdataConfig',  # 注册spiderdata
    'shucaiyidate.apps.ShucaiyidateConfig',  #注册shucaiyidate
    'debug_toolbar',  # 注册debug_toolbar，放在django.contrib.staticfiles后面
]



MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  #debug_toolbar中间件配置，尽可能配置到最前面，但是，必须要要放在处理编码和响应内容的中间件后面，比如我们要是使用了GZipMiddleware，就要把DebugToolbarMiddleware放在GZipMiddleware后面
    'django.middleware.cache.UpdateCacheMiddleware',   #缓存全站之开始缓存 注意： update中间件必须放在列表的开始位置，而fectch中间件，必须放在最后。 这是Django使用中间件的规则，它们是有顺序关系的。
    'shucaiyidate.localuser.middleware.simple_middleware',  #自定义中间键获取IP内容
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',#缓存全站之结束缓存 注意： update中间件必须放在列表的开始位置，而fectch中间件，必须放在最后。 这是Django使用中间件的规则，它们是有顺序关系的。
]

ROOT_URLCONF = 'wanwenyc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # 导入media上下文的处理器，为了使配置的{{MEDIA_URL}}生效
            ],
        },
    },
]


TEMPLATE_CONTEXT_PROCESSORS = (

    "django.core.context_processors.request",

)


WSGI_APPLICATION = 'wanwenyc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#数据库字符集和排序规则：https://www.cnblogs.com/tlz888/p/7067835.html
#默认定义的字符集：utf8
# 默认定义的排序规则：utf8_general_ci
#数据库配置
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'wwyc',
#         'USER':'root',
#         'PASSWORD':'root',
#         'HOST':'127.0.0.1',
#         'OPTIONS':{'init_command':'SET storage_engine=INNODB;'}  #设置数据库为INNODB，为第三方数据库登录用
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shucaiyi',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'PORT': '3306',         # 数据库使用的端口
        'OPTIONS':{'init_command':'SET sql_mode="STRICT_TRANS_TABLES",storage_engine=INNODB;'}  #设置数据库为INNODB，为第三方数据库登录用
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'wanwei',
#         'USER':'lepus_user',
#         'PASSWORD':'123456',
#         'HOST':'192.168.100.187',
#         'PORT': '3306',         # 数据库使用的端口
#         'OPTIONS':{'init_command':'SET sql_mode="STRICT_TRANS_TABLES",storage_engine=INNODB;'}  #设置数据库为INNODB，为第三方数据库登录用
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True


#设置时区
LANGUAGE_CODE = 'zh-hans'  #中文支持，django1.8以后支持；1.8以前是zh-cn
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False   #默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = '/static/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]   #将static加入python根搜索路径

MEDIA_URL = '/media/'   #配置上传文件跟目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    #MEDIA_ROOT只能设置一个，根目录,把media与根目录BASE_DIR连接起来

DJANGO_SERVER_YUMING = "http://192.168.9.77:8000"   #配置服务域名，用于某些页面跳转配置，此处定义便于统一管理

INTERNAL_IPS = ['192.168.9.77']   #debug_toolbar设置访问的IP地址，只有这个IP地址访问网站时，才会展示，其他任何IP访问都会不展示
DEBUG_TOOLBAR_PANELS = [   #debug_toolbar 面板显示设置
    'debug_toolbar.panels.versions.VersionsPanel', # 代表是哪个django版本
    'debug_toolbar.panels.timer.TimerPanel',# 用来计时的，判断加载当前页面总共花的时间
    'debug_toolbar.panels.settings.SettingsPanel', # 读取django中的配置信息
    'debug_toolbar.panels.headers.HeadersPanel', #看到当前请求头和响应头信息
    'debug_toolbar.panels.request.RequestPanel', #当前请求的想信息（视图函数，Cookie信息，Session信息等）
    'debug_toolbar.panels.sql.SQLPanel', # 查看SQL语句
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',# 静态文件
    'debug_toolbar.panels.templates.TemplatesPanel',# 模板文件
    'debug_toolbar.panels.cache.CachePanel',# 缓存
    'debug_toolbar.panels.signals.SignalsPanel',# 信号
    'debug_toolbar.panels.logging.LoggingPanel',# 日志
    'debug_toolbar.panels.redirects.RedirectsPanel',# 重定向

    'pympler.panels.MemoryPanel'  # 内存统计
]

GUOLVNAME = "wanwei"

#缓存值常配置
# CACHE_MIDDLEWARE_ALIAS = "quanzhanhuancun"               #用于存储的缓存的别名
CACHE_MIDDLEWARE_SECONDS = 300            #每个page需要被缓存多少秒.,超时时间设定为300秒
# CACHE_MIDDLEWARE_KEY_PREFIX=         #密钥前缀

# #基于本地（服务器）内存的缓存，缓存保存在服务器的内存中
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#         'TIMEOUT': 600,
#         'OPTIONS': {
#             'MAX_ENTRIES': 2000
#         }
#     }
# }

# #将数据缓存在指定的目录中
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         # 'LOCATION': '/var/tmp/django_cache',    #linux路径
#         'LOCATION': 'E:\djangocache',   #windows路径
#         'TIMEOUT': 600,
#         'OPTIONS': {
#             'MAX_ENTRIES': 1000
#         }
#     }
# }

#利用数据库来缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',   #利用 python manage.py createcachetable my_cache_table 创建的“my_cache_table”表
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 2000
        }
    }
}

# #Memcache来缓存之settings配置
# #使用前需要安装一些内容：
# #1.  sudo apt-get install libevent ibevent-dev         自动下载安装（Ubuntu/Debian）
# #    yum install libevent libevent-devel                    自动下载安装（Redhat/Fedora/Centos）
# #2.  sudo apt-get install memcached             Ubuntu/Debian
# #    yum install memcached                     Redhat/Fedora/Centos
# # 3. pip安装Memcached的插件Python-mencached和pylibmc
# #         pip install python-memcached
# #        pip install pylibmc
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',  #根据你安装的Python依赖库不同，将CACHES的BACKEND设置为django.core.cache.backends.memcached.MemcachedCache或者django.core.cache.backends.memcached.PyLibMCCache
#         'LOCATION': '127.0.0.1:11211',   #设置LOCATION为你的Memecached守护进程所在的主机IP和进程端口，格式为ip:port的字符串。或者unix:path的形式，在Unix操作系统中。
#         'TIMEOUT': 600,
#         'OPTIONS': {
#             'MAX_ENTRIES': 2000
#         }
#     }
# }
