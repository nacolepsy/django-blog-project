from django.conf.urls.defaults import *

urlpatterns = patterns('',
    #url(r'^$', 'reg.views.home'),
    url(r'^login/$', 'reg.views.do_login'),
    url(r'^logout/$', 'reg.views.do_logout'),
    url(r'^error/$', 'reg.views.do_error'),


    
    #url(r'^$', 'reg.views.do_login'),


    #url(r'^$/login/?$', 'reg.views.do_logout'),
    #url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail', name='post_detail'),
    #url(r'^$', 'reg.views.do_login', name='do_login'),
    #url(r'^$', 'reg.views.do_logout', name='do_logout'),
    #url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),
    #url(r'^posts/search/(?P<mysearch>\w+)/$', 'blog.views.post_search'),
    # add your url here
)


