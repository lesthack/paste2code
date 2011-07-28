from django.forms import ModelForm
from django import forms
from django.db import models

class language(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class codes(models.Model):	
	owner = models.CharField(max_length=100)
	name = models.CharField(max_length=200) 
	description = models.CharField(max_length=500)
	code = models.TextField()
	date = models.DateField()
	language = models.ForeignKey(language)
	
	
	def __str__(self):
		return self.name

class codesForm(forms.Form):
	owner = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text','size':'20'}))
	name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'text','size':'20'}))
	description = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':'text','size':'20'}))
	code = forms.CharField(widget=forms.Textarea())