from django import forms    #导入django中的forms

from .models import UpdateDbData  #导入ClickAndBack模块



class UpdateDbDataForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = UpdateDbData   #指明转换的QSUpdateDbData
        fields = "__all__"


