from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_clients/', views.get_clients, name='get_clients'),
    path('get_products/', views.get_products, name='get_products'),
    path('get_orders/', views.get_orders, name='get_orders'),
    path('client_orders/<int:client_id>/', views.client_orders, name='client_orders'),
    path('prod_for_the_period/<int:client_id>/<int:period>/', views.prod_for_the_period, name='prod_for_the_period'),
    # path('prod_for_the_period2/<int:period>/', views.prod_for_the_period2, name='prod_for_the_period2'),
]
