from django import forms    #导入django中的forms

from .modelsdev import TagContent
from .models import XieyiConfigDate


class TagContentForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = TagContent   #指明转换的QSLoginAndCheck
        fields = "__all__"




class XieyiConfigDateForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = XieyiConfigDate   #指明转换的XieyiConfigDate
        fields = "__all__"


