from django import forms


class Userform(forms.Form):
    username=forms.CharField(max_length=10,min_length=4,label='用户名',required=True)#是否为空
    password=forms.CharField(max_length=10,min_length=4,label='密码')

    def clean_username(self):
        username=self.cleaned_data.get('username')
        if "?" in username:
            self.add_error('username','用户名不能有特殊符号')
        else:
            return username
