import logging
from datetime import datetime, timedelta
from random import choice, randint

from django.core.management.base import BaseCommand

from ...models import Client, Order, Product

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate fake objects: Client, Product, Order"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count of client')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        lst_clients = []
        lst_products = []
        lst_orders = []
        """Generate clients"""
        for i in range(1, count + 1):
            client = Client(name=f'client_{i}', email=f'mail{i}@gmail.com',
                            phone=f'+37529{randint(100_000, 999_999)}',
                            address=f'town_{i}, street_{i}')
            logger.info('created client - completed')
            client.save()
            lst_clients.append(client)
        print(lst_clients)

        """Generate products"""
        for k in range(1, (count * 2) + 1):
            prod = Product(name_product=f'Title_product{k}', description=f'some_description_prod_{k}',
                           price=randint(10, 1000),
                           quantity=f'{randint(0, 20)}',
                           date_added=f'{datetime.strptime("2024-03-10", "%Y-%m-%d").date() + timedelta(days=k ** 2)}')
            logger.info('created products - completed')
            prod.save()
            lst_products.append(prod)
            # print(prod.price)
            # print(type(prod.price))
        print(lst_products)

        """Generate orders"""
        for j in range(1, count + 1):
            order = Order(client_store=choice(lst_clients),
                          # basket_products=choices(lst_products, k=3),
                          date_ordered=f'{datetime.strptime("2024-03-10", "%Y-%m-%d").date() + timedelta(days=j ** 2)}',
                          order_total=0)
            order.save()
            sum_ = 0
            for i in range(1, count + 1):
                rnd_product = choice(lst_products)
                sum_ += rnd_product.price
                # print(type(rnd_product.price))
                order.basket_products.add(rnd_product)
                order.save()
            order.order_total = sum_
            order.save()
            logger.info('created orders - completed')
            lst_orders.append(order)
        self.stdout.write(f'created test data: clients, products, orders')
