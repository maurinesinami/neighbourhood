from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url(r'^new/community',views.new_community,name='new-community'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^post$', views.post, name='post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)