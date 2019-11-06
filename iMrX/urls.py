from django.conf.urls import url
from iMrX.view.main import api


app_name ='[iMrX]'
urlpatterns = [
    url(r'^api',api,name="api"),
]