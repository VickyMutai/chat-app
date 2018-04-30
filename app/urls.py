from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'chats/$', views.ChatView.as_view()),
    url(r'chats/(?P<uri>\w+)/$', views.ChatView.as_view()),
    url(r'chats/(?P<uri>\w+)/messages/$', views.ChatMessageView.as_view()),
]