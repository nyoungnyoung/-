from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User 이렇게 쓰면 안된다!!
        # get_user_model 활용해서 가져오기
        model = get_user_model()
