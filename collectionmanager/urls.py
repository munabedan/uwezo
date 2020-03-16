
from django.conf.urls import url
from .views import *
urlpatterns=[
    url(r'^$',index,name='index'),
    url(r'^display_customers$',display_customers,name="display_customers"),
    url(r'^display_products$',display_products,name="display_products"),
    url(r'^display_payments$',display_payments,name="display_payments"),

    url(r'^display_login$',display_login,name="display_login"),
    url(r'^user_auth_login$',user_auth_login,name="user_auth_login"),
    url(r'^user_auth_logout$',user_auth_logout,name="user_auth_logout"),

       url(r'^dashboard$',dashboard,name="dashboard"),

    url(r'^add_customer$',add_customer,name="add_customer"),
    url(r'^add_product$',add_product,name="add_product"),
    url(r'^add_payment$',add_payment,name="add_payment"),

    url(r'^edit_customer/(?P<pk>\d+)$',edit_customer,name="edit_customer"),
    url(r'^edit_product/(?P<pk>\d+)$',edit_product,name="edit_product"),
    url(r'^edit_payment/(?P<pk>\d+)$',edit_payment,name="edit_payment"),

    url(r'^delete_customer/(?P<pk>\d+)$',delete_customer,name="delete_customer"),
    url(r'^delete_product/(?P<pk>\d+)$',delete_product,name="delete_product"),
    url(r'^delete_payment/(?P<pk>\d+)$',delete_payment,name="delete_payment"),


]