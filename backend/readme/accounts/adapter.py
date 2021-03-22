from allauth.account.adapter import DefaultAccountAdapter


#AbstractUser에서 내가 지정한 칼럼을 입력시 DB에 저장되게 하기 - settings.py추가해야함
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.nickname = data.get('nickname')
        user.introduction = data.get('introduction')
        user.gender = data.get('gender')
        user.mbti_id = data.get('mbti_id')
        user.save()
        return user
