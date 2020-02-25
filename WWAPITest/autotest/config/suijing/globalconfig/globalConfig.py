class GlobalConfig(object):
    ISONLINE = False
    ONLINE_WEB_YUMING= ""
    ONLINE_LOGIN_ACCOUNT = ""
    ONLINE_LOGIN_PASSWORD = ""
    ONLINE_REQUESTS_YU_MING = "http://111.207.18.22:40660"

    TEST_WEB_YUMING = "http://111.207.18.22:40660/app/common/toIndex"
    TEST_LOGIN_ACCOUNT = "admin"
    TEST_LOGIN_PASSWORD = "admin123"
    TEST_REQUESTS_YU_MING = "http://111.207.18.22:40660"

    COOKIE_FILE_NAME = "sunjinglogincookie.json"

gc = GlobalConfig()

