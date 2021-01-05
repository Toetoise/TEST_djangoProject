from django.conf.urls import url
from django.urls import path
from helloworld import views
 
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
]
