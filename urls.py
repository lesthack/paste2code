from django.conf.urls.defaults import *
from paste2code.view import *
from paste2code import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', new),
    (r'^list/$', list),
    (r'^add/$', add),
    (r'^code/$', list),
    (r'^code/(\d+)/$', code),
    (r'^about/$', about),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root': settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

