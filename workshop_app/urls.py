from django.urls import path

from workshop_app import views

urlpatterns = [
    # path('',views.front,name='test1'),
    path('',views.landing_page,name='home'),
    path('dash',views.dash,name='dash'),

    path('cus_reg',views.customer_reg,name='customer_reg'),
    path('manager_reg',views.workmanager_reg,name='manager_reg'),
    path('login_view',views.login_view1,name='login_view'),
    path('admin',views.admin,name='admin'),
    path('customer',views.customer,name='customer'),
    path('manager',views.manager,name='manager')
]