from django.conf.urls import url 
from . import views


urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url(r'^new/community',views.new_community,name='new-community'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)