from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^question/(\d+)/', views.question_details, name='question-details'),
    # url(r'^$', 'qa.views.test', name='test'),
    # url(r'^login/', 'qa.views.test', name='test'),
    # url(r'^signup/', 'qa.views.test', name='test'),
    # url(r'^ask/', 'qa.views.test', name='test'),
    # url(r'^popular/', 'qa.views.test', name='test'),
    # url(r'^new/', 'qa.views.test', name='test'),
    # url(r'^question/(\d+)/', qa.views.question_details, name='question-details'),
)
