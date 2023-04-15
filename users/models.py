from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
	clg=models.CharField(max_length=255)
	mob=models.CharField(max_length=255)

class Game(models.Model):
	username=models.CharField(max_length=255)
	email=models.EmailField(max_length=255)
	clg=models.CharField(max_length=255)
	mob=models.CharField(max_length=255)
	q1_ans_on=models.DateTimeField(null=True)
	q2_ans_on=models.DateTimeField(null=True)
	q3_ans_on=models.DateTimeField(null=True)
	q4_ans_on=models.DateTimeField(null=True)
	q5_ans_on=models.DateTimeField(null=True)
	q6_ans_on=models.DateTimeField(null=True)
	q1=models.BooleanField(default=False)
	q2=models.BooleanField(default=False)
	q3=models.BooleanField(default=False)
	q4=models.BooleanField(default=False)
	q5=models.BooleanField(default=False)
	q6=models.BooleanField(default=False)

	def __str__(self):
		return self.username
				


