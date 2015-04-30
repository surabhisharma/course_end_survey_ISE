from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.survey.views.base', name='base'),
    url(r'^complete/', 'mysite.survey.views.end', name='end' ),
    url(r'^store/(?P<product>[a-z]*)','mysite.survey.views.store',name='store'),
    url(r'^login/','mysite.survey.views.log', name='log'),
    url(r'^subject/','mysite.survey.views.sub', name='sub'),
    url(r'^db/','mysite.survey.views.form_store', name='form_store'),
    url(r'^sub/','mysite.survey.views.sub', name='sub'),
    #url(r'^example/','mysite.survey.views.example', name='example'),
     url(r'^logout/','mysite.survey.views.out', name='out'),
    url(r'^admin/', include(admin.site.urls)),
)
