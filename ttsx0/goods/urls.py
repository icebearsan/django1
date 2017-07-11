from django.conf.urls import url
from goods import  views
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.goods_list),
    url(r'^(\d+)/$',views.detail)
]