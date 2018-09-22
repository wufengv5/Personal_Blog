from django.conf.urls import url
from web import views
urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^show_article/(?P<num>\d+)', views.show_article, name='show_article'),
    url(r'^category_article/(?P<num>\d+)',views.category_article,name='category_article'),
    url(r'^add_comment/(?P<num>\d+)',views.add_comment,name='add_comment'),
    url(r'^list/',views.list,name='list'),


]