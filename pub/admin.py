from django.contrib import admin
from paste2code.pub.models import *

class codesAdmin(admin.ModelAdmin):
	list_display = ('owner', 'code')

class languageAdmin(admin.ModelAdmin):
	list_display = ('name')


admin.site.register(codes)
admin.site.register(language)