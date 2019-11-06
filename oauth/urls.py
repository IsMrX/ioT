from django.conf.urls import url
from oauth.view.code.view import AuthorizeView
from oauth.view.token.view import GetToken

app_name ='[oauth]'
urlpatterns = [
    url(r'code$',AuthorizeView.as_view(),name="GetCode"),
    url(r'^token$',GetToken,name="GetToken"),
]