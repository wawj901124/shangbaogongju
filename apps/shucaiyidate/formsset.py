from django import forms    #导入django中的forms
# from .forms import ConfigControlSendPorsConvertruleForm


class ConfigControlSendPorsConvertruleFormset(forms.models.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ConfigControlSendPorsConvertruleFormset, self).__init__(*args, **kwargs)
        print("self.user:")
        print(self.user)

