from django.forms import ModelForm, TextInput, Textarea, HiddenInput
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

class codesForm(ModelForm):
	class Meta:
		model = codes
		fields = ('owner', 'name', 'description', 'code', 'language', 'date')		
		widgets = {
			'name': TextInput(attrs={'class':'text', 'size':'20'}),
			'owner': TextInput(attrs={'class':'text', 'size':'20'}),
			'description': TextInput(attrs={'class':'text', 'size':'50'}),
			'code': Textarea(),
			'date': HiddenInput(),
		}

class languageForm(ModelForm):
	class Meta:
		model = language
		