from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User >>> Django에서는 User클래스는 가져올때 요래 쓰믄 안돼요
# get_user_model() 함수를 이용해서 user 클래스 얻어오기 
# 니가 사용하고 있는 User 클래스 대신에.. 내가 가지고 있는걸로 바꿔줄게
class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = get_user_model()
    fields =  UserCreationForm.Meta.fields + ('email',)
    

class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = get_user_model()
    fields = ('email', 'first_name', 'last_name',)