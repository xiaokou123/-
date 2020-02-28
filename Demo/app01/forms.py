from django import forms

class User(forms.Form):
    username=forms.CharField(min_length=3,max_length=10,label='用户名',required=True)
    password=forms.CharField(min_length=3,max_length = 10,required=True,label='密码')
    def clean_username(self):
        username= self.cleaned_data.get('username')
        if '?' in username:
            self.add_error('username','不能有特殊符号')
        else:
            return username