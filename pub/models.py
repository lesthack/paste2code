from django.forms import ModelForm, TextInput, Textarea, HiddenInput 
from django import forms
from django.db import models
from time import strftime

class language(models.Model):
	name = models.CharField(max_length=50)	
	def __str__(self):
		return self.name

class codes(models.Model):	
	owner = models.CharField(max_length=100, blank=True)
	name = models.CharField(max_length=200, blank=True) 
	description = models.CharField(max_length=500, blank=True)
	code = models.TextField()
	date = models.DateTimeField()
	language = models.ForeignKey(language)

	def __str__(self):
		return self.name

class codesForm(ModelForm):
	class Meta:
		model = codes
		fields = ('owner', 'name', 'description', 'code', 'language','date')		
		widgets = {
			'name': TextInput(attrs={'class':'text', 'size':'20'}),
			'owner': TextInput(attrs={'class':'text', 'size':'20'}),
			'description': TextInput(attrs={'class':'text', 'size':'50'}),
			'code': Textarea(attrs={'class':'textarea'}),
			'date': HiddenInput(),
		}
		
	def clean_date(self):
		return strftime("%Y-%m-%d %H:%M:%S")		
			
class languageForm(ModelForm):
	class Meta:
		model = language
		