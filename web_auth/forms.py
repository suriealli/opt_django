#coding=utf8

from django import forms
from web_auth.models import UserProfile
from django.contrib.auth.models import User

# User 模型
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # 设置密码栏输入不可见
    username = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    def as_myp(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = '<p%(html_class_attr)s>%(label)s%(field)s</p>',
            error_row = '%s',
            row_ender = '</p>',
            help_text_html = ' <span class="helptext">%s</span>',
            errors_on_separate_row = True)


# 扩充User 模型
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
    def as_myp(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = '<p%(html_class_attr)s>%(label)s%(field)s</p>',
            error_row = '%s',
            row_ender = '</p>',
            help_text_html = ' <span class="helptext">%s</span>',
            errors_on_separate_row = True)