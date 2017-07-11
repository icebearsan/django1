from django.conf.urls import url
from everyday import views

urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^register_vaild/$', views.register_vaild),
    url(r'^login/$',views.login),
    url(r'^login_handle/$',views.login_handle),
    url(r'^$',views.center),
    url(r'^order/$',views.order),
    url(r'^site/$',views.site),
    url(r'^login_out',views.log_out),
]