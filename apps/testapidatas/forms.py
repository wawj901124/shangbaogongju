from django import forms    #导入django中的forms

from .models import ApiRequestData  #导入ApiRequestData模块


class ApiRequestDataForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = ApiRequestData   #指明转换的QSApiRequestData
        fields = "__all__"
        # fields = ['test_project','test_module','test_page','requirement_function','case_priority',
        #          'case_process_type', 'case_title','case_precondition', 'case_step', 'case_expected_result',
        #           'write_comments','write_user','write_case_time']  #指明要转换的字段


