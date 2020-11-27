"""Define URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name= 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page for topics
    path('topics/', views.topics, name='topics'),
    #Page for each topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
