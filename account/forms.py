from django import forms
from account.models import user_data

class UserDataForm(forms.ModelForm):

	class Meta:
		model = user_data
		fields = ('user_image', 'date_of_birth', 'gender', 'country', 'about')