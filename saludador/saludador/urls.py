from django.conf.urls import patterns, include, url
from django.contrib import admin
from saludos.views import saludo

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', saludo)
)
