from django import forms
from .models import User, Review

# 회원가입 폼에 닉네임 쓰도록 추가하기
# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["nickname"]
        
#     def signup(self, request, user): # 폼으로 입력받는 데이터를 유저 인스턴스에 저장해주는 메소드
#         user.nickname = self.cleaned_data['nickname'] # Form에 저장된 데이터는 cleaned_data로 가져올 수 있음
#         user.save()
        
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "restaurant_name",
            "restaurant_link",
            "rating",
            "image1",
            "image2",
            "image3",
            "content",
        ]
        widgets = {
            "rating": forms.RadioSelect,
        }
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'nickname',
            'profile_pic',
            'intro'
        ]
        widgets = {
            'intro':forms.Textarea,
        }