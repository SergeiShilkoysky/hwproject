import logging
from datetime import date, timedelta

from django.shortcuts import render, get_object_or_404

from .models import Client, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    logger.info('hw3 page accessed')
    return render(request, 'myhwapp3/base.html')


def get_clients(request):
    """get all clients"""

    logger.info(f'{request} request received')
    clients = Client.objects.all()
    context = {'title': 'Clients_store',
               'items': clients}
    return render(request, 'myhwapp3/all_clients.html', context)


def get_products(request):
    """get all products"""

    logger.info(f'{request} request received')
    products = Product.objects.all()
    context = {'title': 'Store products ',
               # 'name': 'product_by_id',
               'items': products}
    return render(request, 'myhwapp3/products_list.html', context)


def get_orders(request):
    """get all orders"""

    logger.info(f'{request} request received')
    orders = Order.objects.all()
    context = {'title': 'Orders',
               'items': orders}
    return render(request, 'myhwapp3/orders_list.html', context)


def client_orders(request, client_id: int):  # http://127.0.0.1:8000/hw3/client_orders/6/
    """get orders of client"""  # http://127.0.0.1:8000/hw3/client_orders/37

    logger.info(f'{request} request received')
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_store=client).all()
    context = {'title': client_id,
               'name': client.name,
               'items': orders}
    return render(request, 'myhwapp3/client_order.html', context)


def prod_for_the_period(request, client_id: int, period: int):  # http://127.0.0.1:8000/hw3/prod_for_the_period/17/1/
    """get products of orders client for the n-days"""  # http://127.0.0.1:8000/hw3/prod_for_the_period/37/1/

    logger.info(f'{request} request received')
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_store=client,
                                  # date_ordered__gt=(timezone.now() - timezone.timedelta(days=period))).all()
                                  date_ordered__gt=date.today() - timedelta(days=period))
    products = [product for order in orders for product in order.basket_products.all()]
    context = {'title': client.id,
               'list': 'Client',
               'name': client.name,
               'period': period,
               'items': products}
    return render(request, 'myhwapp3/client_prod.html', context)
