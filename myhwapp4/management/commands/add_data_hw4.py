import logging
import math
from decimal import Decimal
from random import choice, randint

from django.core.management.base import BaseCommand
from faker import Faker

from myhwapp4.models import Client, Order, Product
from myhwapp4.random_date import gen_datetime

logger = logging.getLogger(__name__)

MAX_PRODUCT = 100


class Command(BaseCommand):
    help = "Generate fake objects: Client, Product, Order"

    """:param cnt_clients - the count of clients,
    cnt_products and cnt_orders - similarly"""

    def add_arguments(self, parser):
        parser.add_argument('-c', '--cnt_clients', type=int, help='count of clients')
        parser.add_argument('-p', '--cnt_products', type=int, help='count of products')
        parser.add_argument('-o', '--cnt_orders', type=int, help='count of orders')

    def handle(self, *args, **kwargs):
        cnt_clients = kwargs.get('cnt_clients')
        cnt_products = kwargs.get('cnt_products')
        cnt_orders = kwargs.get('cnt_orders')

        fake = Faker(locale="en_US")  # English (по умолчанию!), для ru: locale="ru_RU"

        lst_clients = []
        lst_products = []
        lst_orders = []

        """Generate clients"""
        for i in range(cnt_clients):
            client = Client(name=f' {fake.name()}_{i}',
                            email=f'{fake.email()}',
                            phone=f'{fake.phone_number()}',
                            address=f'{fake.address()}')
            client.save()
            lst_clients.append(client)
        logger.info(f'-------- created {cnt_clients} client - completed---------')
        print(lst_clients)

        """Generate products"""
        # words = ['sugar', 'meat', 'cloud', 'blood', 'kidney', 'papaya']
        for k in range(cnt_products):
            prod = Product(name_product=f'{fake.word()}_{k}',
                           description=f'{fake.text().replace('\n', ' ')[:30]}_{k}',
                           price=Decimal(randint(10, 10000) / math.pi).quantize(Decimal("1.00")),
                           quantity=f'{randint(0, MAX_PRODUCT)}',
                           # date_add=f'{datetime.strptime("2024-01-10", "%Y-%m-%d").date() + timedelta(days=k ** 2)}')
                           date_add=gen_datetime())
            # print(prod.price)
            # print(type(prod.price))
            prod.save()
            lst_products.append(prod)
        logger.info(f'for log: created {cnt_products} products - completed')
        print(lst_products)

        """Generate orders"""
        for j in range(1, cnt_orders):
            order = Order(client_store=choice(lst_clients),
                          date_ordered=gen_datetime(),
                          # date_ordered=f'{fake.date_time_between('-1y', tzinfo=timezone(timedelta(hours=3), name='МСК'))}',
                          order_total=0)

            order.save()
            sum_ = 0
            for i in range(cnt_clients):
                rnd_product = choice(lst_products)
                # print(type(rnd_product.price))
                sum_ += rnd_product.price
                order.basket_products.add(rnd_product)
                # basket.product.add(rnd_product)
                # basket.quantity += 1
                # order.save()
            order.order_total = sum_
            order.save()
            lst_orders.append(order)
        print(lst_orders)
        logger.info(f'created {cnt_orders} orders - completed')
        self.stdout.write(f'created test data: {cnt_clients} clients, {cnt_products} products, {cnt_orders} orders')
