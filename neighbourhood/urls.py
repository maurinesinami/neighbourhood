from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url(r'^new/community',views.new_community,name='new-community'),
    url(r'^new/post/(\d+)$', views.new_post, name='new-post'),
    url(r'^post/(\d+)$', views.post, name='post'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new/profile/(\d+)$', views.new_profile, name='new-profile'), 
    url(r'^new/business/(\d+)$', views.new_business, name='new-business'),
    url(r'^business/(\d+)$', views.business, name='business'), 
    url(r'^search/', views.search_results, name='search_results')  , 
    url(r'^leave/hood$', views.leave_hood, name='left')       
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)