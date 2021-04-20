from django.conf.urls import url
from django.urls import path
from helloworld import views, testdb, search
 
urlpatterns = [
    url(r'^$', views.hello),
    path('start/', views.start),
    path('one', views.one),
    path('two', views.two),
    path('three', views.three),
    path('four', views.four),
    path('five', views.five),
    path('six', views.six),
    path('seven', views.seven),
    path('eight', views.eight),
    path('nine', views.nine),
    path('ten', views.ten),
    path('elven', views.elven),
    path('twelve', views.twelve),
    path('testdb', testdb.testdb),
    path('getdata', testdb.getdata),
    path('update', testdb.update),
    path('delete', testdb.delete),
    path('search-form', search.search_form),
    path('search', search.search),
    path('search-post', search.search_post),
    path('search-request', search.search_request),
]
