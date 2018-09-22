from django.conf.urls import url
from django.contrib.staticfiles.templatetags.staticfiles import static

from Homeword import settings
from backweb import views
urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^index/',views.index,name='index'),
    url(r'^article/',views.article,name='article'),
    url(r'^add-article/', views.add_article, name='add_article'),
    url(r'^del_article/(?P<num>\d+)',views.del_article,name='del_article'),
    url(r'^show_article/(?P<num>\d+)',views.show_article,name='show_article'),
    url(r'^update_article/(?P<num>\d+)',views.update_article,name='update_article'),
    url(r'^del_img',views.del_img,name='del_img'),
    url(r'^notice/',views.notice,name='notice'),
    url(r'^add_notice/',views.add_notice,name='add_notice'),
    url(r'^del_notice/(?P<num>\d+)',views.del_notice,name='del_notice'),
    url(r'^show_notice/(?P<num>\d+)',views.show_notice,name='show_notice'),
    url(r'^comment/',views.comment,name='comment'),
    url(r'^del_comment/(?P<num>\d+)',views.del_comment,name='del_comment'),
    url(r'^category/',views.category,name='category'),
    url(r'^add-category/',views.add_category,name='add_category'),
    url(r'^del-category/(?P<num>\d+)/',views.del_category,name='del_category'),
]
