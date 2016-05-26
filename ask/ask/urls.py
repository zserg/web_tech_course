from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from django.contrib import admin
from qa import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.question_list, name='question-list'),
    url(r'^popular/$', views.popular_list, name='popular_list'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^login/$', auth_views.login, {'template_name': 'qa/login.html'}),
    url(r'^signup/$', views.signup,  name='signup'),
    url(r'^question/(\d+)/', views.question_details, name='question-details'),

)
