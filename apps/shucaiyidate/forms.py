from django import forms    #导入django中的forms

from .modelsdev import TagContent
from .models import XieyiConfigDate
from .modelsnewdev import NodeConfig,ConfigCollectSendCmd,\
    ConfigCollectFactor, \
    ConfigControlSendPorsSection,\
    ConfigControlSendPorsConvertrule
from .modelsorder import XieyiConfigDateOrder,\
    XieyiTestCase,FtpUploadFileOrder,\
    SenderHexDataOrder,\
    RecriminatDataOrder

global guolu_name_id
guolu_name_id = 1
print(guolu_name_id)




class TagContentForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = TagContent   #指明转换的QSLoginAndCheck
        fields = "__all__"


class XieyiConfigDateForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = XieyiConfigDate   #指明转换的XieyiConfigDate
        fields = "__all__"


class ConfigCollectFactorForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if not kwargs.get('initial'):
    #         return self.uid = kwargs.get('initial').get('uid')


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.request = kwargs("request")
    #     print("self.request:")
    #     print(self.request)
    #
    #     self.fields['configcollectsendcmd'].queryset = ConfigCollectSendCmd.objects.filter(nodeconfig_id=1)

    class Meta:
        model = ConfigCollectFactor
        # exclude = ('user', 'recurring',)
        fields = "__all__"

#测试用例表单
class XieyiTestCaseForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = XieyiTestCase   #指明转换的XieyiTestCase
        fields = "__all__"

#测试用例依赖配置表单
class XieyiConfigDateOrderForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = XieyiConfigDateOrder   #指明转换的XieyiConfigDateOrder
        fields = "__all__"


#测试用例串口收发数据表单配置
class SenderHexDataOrderForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = SenderHexDataOrder   #指明转换的SenderHexDataOrder
        fields = "__all__"

#测试用例反控收发数据表单配置
class RecriminatDataOrderForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = RecriminatDataOrder   #指明转换的RecriminatDataOrder
        fields = "__all__"


#测试用例反控收发数据表单配置
class ConfigControlSendPorsConvertruleForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库

    print(" ConfigControlSendPorsConvertruleForm初始化")

    # configcontrolsendporssection = forms.ModelChoiceField(ConfigControlSendPorsSection.objects.filter(write_user_id=guolu_name_id))

    # def __init__(self,*args, **kwargs):
    #     super(ConfigControlSendPorsConvertruleForm,self).__init__(*args, **kwargs)
    #
    #     self.fields['configcontrolsendporssection'].queryset = ConfigControlSendPorsSection.objects.filter(write_user_id=self.instance.writer_user_id)

    class Meta:
        model = ConfigControlSendPorsConvertrule  #指明转换的RecriminatDataOrder
        fields = "__all__"




