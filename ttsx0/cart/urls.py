from django.conf.urls import url
from cart import  views
urlpatterns= [
    url(r'^$',views.cart),
    url(r'^add/$',views.add),
    url(r'^count/$',views.count),
]