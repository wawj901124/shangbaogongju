from django.urls import  path

# from .views import TestCaseView, DisplayTestCaseView,MoreTestCaseView,AllTestCaseSiderView,SiderCaseDisplayView,SiderCaseDetailsView   #导入TestCaseView
from .views import ClickAndBackView,NewAddAndCheckView,SearchAndCheckView   #导入ClickAndBackView
from .views import NewAddAndCheckWithRelevanceView,SearchAndCheckWithRelevanceView
from .views import DeleteAndCheckView,EditAndCheckView
from .views import LoginAndCheckView


urlpatterns = [
    # 登录场景的复制页面的url配置
    path('loginandcheckcopy/<path:loginandcheck_id>/', LoginAndCheckView.as_view(), name="login_and_check_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    #相同参数的路径名一定不能一样。比如copy/<path:testcase_id>/与<path:testcase_id>/不能并列存在
    path('clickandbackcopy/<path:clickandback_id>/', ClickAndBackView.as_view(), name="click_and_back_id"),  # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    #新增场景的复制页面的url配置
    path('newaddandcheckcopy/<path:newaddandcheck_id>/', NewAddAndCheckView.as_view(), name="new_add_and_check_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 新增场景的复制页面的url配置,带关联新增
    path('newaddandcheckcopywithrelevance/<path:newaddandcheck_id>/', NewAddAndCheckWithRelevanceView.as_view(), name="new_add_and_check_with_relevance_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 查询场景的复制页面的url配置
    path('searchandcheckcopy/<path:searchandcheck_id>/', SearchAndCheckView.as_view(), name="search_and_check_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 查询场景的复制页面的url配置,带关联新增
    path('searchandcheckcopywithrelevance/<path:searchandcheck_id>/', SearchAndCheckWithRelevanceView.as_view(), name="search_and_check_with_relevance_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 删除场景的复制页面的url配置
    path('deleteandcheckcopy/<path:deleteandcheck_id>/', DeleteAndCheckView.as_view(), name="delete_and_check_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 修改场景的复制页面的url配置
    path('editandcheckcopy/<path:editandcheck_id>/', EditAndCheckView.as_view(), name="edit_and_check_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定



]

app_name = 'clickandback'