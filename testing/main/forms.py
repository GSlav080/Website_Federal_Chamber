from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from .models import *


class RegisterUserForms(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'from-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'from-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'from-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'from-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'from-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'from-input'}),

        }


class FormForm(ModelForm):
    class Meta:
        model = Form
        fields = ['nikname', 'USER_NAME', 'Birthday', 'Froms', 'Pasport',
                  'Data_pasport', 'INFO',  'Number', 'email','razdel', 'status'
                  ]
        widgets = {
            'nikname': TextInput(attrs={'readonly':"readonly", 'display':'nons'}),
            'razdel': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),
            'status': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),

        }

class Form2Form(ModelForm):
    class Meta:
        model = Form2
        fields = ['nikname', 'USER_NAME', 'Birthday', 'Froms', 'Pasport','Data_pasport', 'INFO',  'Number', 'email','razdel', 'status'
                  ]
        widgets = {
            'nikname': TextInput(attrs={'readonly':"readonly", 'display':'nons'}),
            'razdel': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),
            'status': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),

        }
class Form3Form(ModelForm):
    class Meta:
        model = Form3
        fields = ['nikname', 'USER_NAME', 'Birthday', 'Froms', 'Pasport','Data_pasport', 'INFO',  'Number', 'email','razdel', 'status'
                  ]
        widgets = {
            'nikname': TextInput(attrs={'readonly':"readonly", 'display':'nons'}),
            'razdel': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),
            'status': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),

        }
class Form4Form(ModelForm):
    class Meta:
        model = Form4
        fields = ['nikname', 'USER_NAME', 'Birthday', 'Froms', 'Pasport','Data_pasport', 'INFO',  'Number', 'email','razdel', 'status'
                  ]
        widgets = {
            'nikname': TextInput(attrs={'readonly':"readonly", 'display':'nons'}),
            'razdel': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),
            'status': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),

        }
class Form5Form(ModelForm):
    class Meta:
        model = Form5
        fields = ['nikname', 'USER_NAME', 'Birthday', 'Froms', 'Number', 'email', 'razdel', 'status'
                  ]
        widgets = {
            'nikname': TextInput(attrs={'readonly':"readonly", 'display':'nons'}),
            'razdel': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),
            'status': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),

        }
class Form6Form(ModelForm):
    class Meta:
        model = Form6
        fields = ['nikname', 'USER_NAME', 'Birthday',   'Number', 'email','razdel', 'status'
                  ]
        widgets = {
            'nikname': TextInput(attrs={'readonly':"readonly", 'display':'nons'}),
            'razdel': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),
            'status': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),
        }

