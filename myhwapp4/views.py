import logging
from datetime import date, timedelta

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
from .models import Client, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    logger.info('hw3 page accessed')
    return render(request, 'myhwapp4/base.html')


def get_clients(request):
    """get all clients"""

    logger.info(f'{request} request received')
    clients = Client.objects.all()
    context = {'title': 'Clients_store',
               'items': clients}
    return render(request, 'myhwapp4/all_clients.html', context)


def get_products(request):
    """get all products"""

    logger.info(f'{request} request received')
    products = Product.objects.all()
    context = {'title': 'Store products ',
               # 'name': 'product_by_id',
               'items': products}
    return render(request, 'myhwapp4/products_list.html', context)


def get_orders(request):
    """get all orders"""

    logger.info(f'{request} request received')
    orders = Order.objects.all()
    context = {'title': 'Orders',
               'items': orders}
    return render(request, 'myhwapp4/orders_list.html', context)


def client_orders(request, client_id: int):  # http://127.0.0.1:8000/hw3/client_orders/6/
    """get orders of client"""  # http://127.0.0.1:8000/hw3/client_orders/37

    logger.info(f'{request} request received')
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_store=client).all()
    context = {'title': client_id,
               'name': client.name,
               'items': orders}
    return render(request, 'myhwapp4/client_order.html', context)


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
    return render(request, 'myhwapp4/client_prod.html', context)


def update_product(request):
    """Creating a form for editing products in the database"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name_product = form.cleaned_data['name_product']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            date_add = form.cleaned_data['date_add']
            image_product = form.cleaned_data['image_product']
            file_product = form.cleaned_data['file_product']
            fss = FileSystemStorage()
            fss.save(image_product.name, image_product)
            fs = FileSystemStorage()
            fs.save(file_product.name, file_product)
            logger.info(f' update {name_product=}, {description=},'
                        f' {price=}, {quantity=}, {date_add=}')
            product = Product(name_product=name_product, description=description, price=price,
                              quantity=quantity, date_add=date_add, image_product=image_product,
                              file_product=file_product)
            if 'id_product' in request.POST:
                id_product = request.POST['id_product']
                product = Product.objects.filter(pk=id_product).first()
                product.name_product = name_product
                product.description = description
                product.price = price
                product.quantity = quantity
                product.date_add = date_add  # datetime.date.today()
                product.image_product = image_product
                product.file_product = file_product
            product.save()
            message = 'product add successfully'
            return render(request, 'myhwapp4/card_product.html',
                          {'title': 'Card product', 'product': product, 'message': message})
        else:
            message = 'Error input data'
    else:
        form = ProductForm()
        message = 'fill in the form'
    return render(request, 'myhwapp4/form_product.html',
                  {'title': 'Update product', 'form': form, 'message': message})
