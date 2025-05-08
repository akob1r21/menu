from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_viev, name='reg'),
    path('login',views.login_view,name='log'),
    path('logout',views.logout_view, name='logout'),
    path('home',views.home,name='home'),
    path('my-orders/', views.my_order, name='my_order'),
    path('order/<int:id>/', views.order, name='order'),
]