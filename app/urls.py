from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('chats/', views.ChatSessionView.as_view()),
    url('chats/<uri>/', views.ChatSessionView.as_view()),
    url('chats/<uri>/messages/', views.ChatSessionMessageView.as_view()),
]
