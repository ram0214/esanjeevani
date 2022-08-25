from django.forms import ModelForm
from mainapp.models import UserInfo

class UserForm(ModelForm):
    class Meta:
        model = UserInfo
        fields="__all__"
        