from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class Ansform(forms.Form):
	ans=forms.CharField(max_length=255)



class Customusercreationform(UserCreationForm):

	class Meta:
		model=CustomUser
		fields = ('username', 'clg','email', 'mob', )

class Customuserchangeform(UserChangeForm):  
	class Meta:	
		model=CustomUser
		fields=('username','clg','email','mob',)



	



