from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .forms import Customusercreationform,Customuserchangeform
from .models import CustomUser,Game

########################export########################
#from import_export.admin import ImportExportModelAdmin

from import_export import resources


class Gameresource(resources.ModelResource):
	class Meta:
		model=Game




class Customuseradmin(UserAdmin):
	add_form=Customusercreationform
	form=Customuserchangeform
	model=CustomUser
	list_display = ['email','username','mob','clg','date_joined','is_superuser']

class Gameadmin(admin.ModelAdmin):
	model=Game
	list_display = ['email','username','mob','clg',"q1","q2","q3","q4","q5","q6","q1_ans_on","q2_ans_on","q3_ans_on","q4_ans_on","q5_ans_on","q6_ans_on"]


admin.site.register(CustomUser,Customuseradmin)	

admin.site.register(Game,Gameadmin)
