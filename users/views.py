from django.shortcuts import render,redirect
#from . forms import SignupForm 
#from django.contrib.auth import login,authenticate
from .forms import Customusercreationform,Ansform
from django.views import generic
from django.urls import reverse_lazy
import datetime
from .models import CustomUser,Game
from django.utils import timezone
from itertools import chain
import string


# Create your views here.

keys=['a','b','c','d','e','f']

fut=datetime.datetime(2019,3,26,20,30)


def compare(s1, s2):

	s1=s1.replace(" ","")
	s1=s1.replace(".","")


	s2=s2.replace(" ","")
	s2=s2.replace(".","")
	return s1==s2

    



def board(request):
	g6=Game.objects.filter(q6=True).values_list('username', flat=True).order_by('q6_ans_on')
	g5=Game.objects.filter(q5=True,q6=False).values_list('username', flat=True).order_by('q5_ans_on')
	g4=Game.objects.filter(q4=True,q5=False).values_list('username', flat=True).order_by('q4_ans_on')
	g3=Game.objects.filter(q3=True,q4=False).values_list('username', flat=True).order_by('q3_ans_on')
	g2=Game.objects.filter(q2=True,q3=False).values_list('username', flat=True).order_by('q2_ans_on')
	g1=Game.objects.filter(q1=True,q2=False).values_list('username', flat=True).order_by('q1_ans_on')

	res=list(chain(g6,g5,g4,g3,g2,g1))
	context={
	# 'res':list(g6)+g5+g4+g3+g2+g1
	'res':res,

	}

	print(res)
	return render(request,'board.html',context)









def auth(request,no):
	qstn_no=no
	msg="Oops! Try again"

	print(request.user,'name')
	user=CustomUser.objects.get(username=request.user) 
	# print(user.mob) 

	game_obj=Game.objects.filter(username=user.username)
	print(len(game_obj),'length')
	
	if request.method=="POST":
		form=Ansform(request.POST)
		if(form.is_valid()):
			ans=form.cleaned_data['ans']
			print(ans)

			if(len(game_obj)==0):
				print("loop")
				if( compare(ans.lower(),keys[no-1].lower()) ):
					msg="bla"
					print('correct',no)
					try:
						Game.objects.create(username=user.username,email=user.email,clg=user.clg,mob=user.mob,q1_ans_on=timezone.now(),q1=True)
						print("object created")
					except Exception as e:
						print(e)
					qstn_no=2
			
					
							

			else : 
				if( compare(ans.lower(),keys[no-1].lower())):
					msg="bla"
					print('correct',no)
					game_obj=game_obj[0]
					print(game_obj.q2)

					
					try:

						

						if(not game_obj.q2 and no==2): 
				
							game_obj.q2=True
							game_obj.q2_ans_on=timezone.now()
							game_obj.save()
							print("object value added 2")
							

						elif(not game_obj.q3 and no==3): 
				
							game_obj.q3=True
							game_obj.q3_ans_on=timezone.now()
							game_obj.save()
							print("object value added 3")


						elif(not game_obj.q4 and no==4): 
				
							game_obj.q4=True
							game_obj.q4_ans_on=timezone.now()
							game_obj.save()
							print("object value added 4")

						elif(not game_obj.q5 and no==5): 
				
							game_obj.q5=True
							game_obj.q5_ans_on=timezone.now()
							game_obj.save()
							print("object value added 5")
					

						elif(not game_obj.q6 and no==6): 
				
							game_obj.q6=True
							game_obj.q6_ans_on=timezone.now()
							game_obj.save()
							print("object value added 6")			
							




					except Exception as e:
						print(e)
					
					qstn_no=no+1 
					if(qstn_no==7):

						return render(request,'winner.html',{'u':user.username})


					
								


			

			form=Ansform()	

			return render(request,'game.html',{'form':form,'qstn_no':qstn_no,'msg':msg})	


	return redirect('home')		

	# print(no,ans,'last')

def game(request):

	prop="hide"
	pre=datetime.datetime.now()
	#pre=pre.replace(tzinfo=datetime.timezone(datetime.timedelta(0, 19800))).isoformat()

	dif=fut-pre
	print(pre,fut,dif.days)
	if dif.days <0 :
		prop="show"
	print(prop,"game")

	qstn_no=1

	if(request.user.is_authenticated): 
		if prop=="show": 

			user=CustomUser.objects.get(username=request.user)
			game_obj=Game.objects.filter(username=user.username)


			if(len(game_obj)!=0): 
				game_obj=game_obj[0]
				if(not game_obj.q2 ): 
					qstn_no=2
					

				elif(not game_obj.q3): 
					qstn_no=3
		
					


				elif(not game_obj.q4 ): 
					qstn_no=4
		
					
				elif(not game_obj.q5 ): 
					qstn_no=5
		
				elif(not game_obj.q6 ): 
					qstn_no=6
		
				




			form=Ansform()
			return render(request,'game.html',{'form':form,'qstn_no':qstn_no})
	
			
		else : 
			return render(request,'home.html',{'prop':prop})	
			
	else:
		return redirect('login')


	
class Signup(generic.CreateView):
	form_class=Customusercreationform
	success_url=reverse_lazy('login')
	template_name='signup.html'

	


def home(request):
	prop="hide"
	pre=datetime.datetime.now()
	#pre=pre.replace(tzinfo=datetime.timezone(datetime.timedelta(0, 19800))).isoformat()

	dif=fut-pre
	print(pre,fut,dif.days)
	if dif.days <0 :
		prop="show"
	print(prop)	
	return render(request,'home.html',{'prop':prop})

# def signup(request):
# 	if request.method == "POST":
# 		form=SignupForm(request.POST)
# 		p1=request.POST["password1"]
# 		p2=request.POST["password2"]
# 		print(p1,'|'*5,p2)
# 		msg="bla"

# 		if p1 != p2:
# 			msg="Passwords didn't match!!!"
# 		else : 
# 			msg="Password conditions not met!!!"
			

# 		try:
# 			if(form.is_valid):
# 			 form.save()
# 			 username=form.cleaned_data.get("username")
# 			 raw_pass=form.cleaned_data.get("password1")
# 			 user=authenticate(username=username,password=raw_pass)
# 			 login(request,user)
# 			 return redirect('home')
			
# 		except Exception as e:
# 			return render(request,'signup.html',{"signup":form,'msg':msg})
			
# 	else: 
# 		form=SignupForm()
# 	return render(request,'signup.html',{"signup":form})





