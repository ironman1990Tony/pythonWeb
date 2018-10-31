""""define url mode in learning_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #main page
    url(r'^$', views.index, name='index'),

    #all topics
    url(r'^topics/$', views.topics, name='topics'),

    #specific topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$' , views.new_entry, name='new_entry'),
]
