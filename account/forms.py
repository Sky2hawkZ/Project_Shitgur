from django import forms
from account.models import user_data
from django.contrib.auth.models import User

class UserDataForm(forms.ModelForm):
	user_image = forms.ImageField(widget=forms.FileInput)

	class Meta:
		model = user_data
		fields = ('user_image', 'date_of_birth', 'gender', 'country', 'about')

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name')