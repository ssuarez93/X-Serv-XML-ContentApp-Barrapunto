from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages', 'ContentAappBarraPunto.views.lista_paginas'),
    url(r'^update$', 'ContentAappBarraPunto.views.update'),
    url(r'^(\d+)', 'ContentAappBarraPunto.views.identificador'),
    url(r'^(.*)$', 'ContentAappBarraPunto.views.recurso')
)
