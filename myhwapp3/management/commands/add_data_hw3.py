import logging
import math
from decimal import Decimal
from random import choice, randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Client, Order, Product
from ...random_date import gen_datetime

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
            logger.info(f'-------- created {cnt_clients} client - completed---------')
            client.save()
            lst_clients.append(client)
        print(lst_clients)

        """Generate products"""
        # words = ['sugar', 'meat', 'cloud', 'blood', 'kidney', 'papaya']
        for k in range(cnt_products):
            prod = Product(name_product=f'{fake.word()}_{k}',
                           description=f'{fake.text().replace('\n', ' ')[:30]}_{k}',
                           # price=(f'{fake.random_int(min=0, max=9999)}.{fake.random_int(min=0, max=99)}'),
                           price=Decimal(randint(10, 10000) / math.pi).quantize(Decimal("1.00")),
                           quantity=f'{randint(0, MAX_PRODUCT)}',
                           # date_add=f'{datetime.strptime("2024-01-10", "%Y-%m-%d").date() + timedelta(days=k ** 2)}')
                           date_add=gen_datetime())
            # print(prod.price)
            # print(type(prod.price))
            logger.info(f'for log: created {cnt_products} products - completed')
            prod.save()
            lst_products.append(prod)
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
            logger.info(f'created {cnt_orders} orders - completed')
            lst_orders.append(order)
        print(lst_orders)
        self.stdout.write(f'created test data: {cnt_clients} clients, {cnt_products} products, {cnt_orders} orders')

        # """Generate orders"""
        # for client in lst_clients:
        #     for _ in range(cnt_clients):
        #         order = Order(client_store=choice(lst_clients), date_ordered=gen_datetime())
        #         lst_orders.append(order)
        # print(lst_orders)
        # for order in lst_orders:
        #     count_prod_in_basket = randint(1, cnt_products)
        #     for prod_in_basket in range(count_prod_in_basket):
        #         rnd_prod = choice(lst_products)
        #         order.basket_products.add(rnd_prod)
        #         # print(type(rnd_product.price))
        #         quantity_prod = randint(0, 10)
        #         backet = BasketProduct.objects.create(order_client=order, product=rnd_prod, quantity=quantity_prod)
        #         order.order_total += quantity_prod * rnd_prod.price
        #     backet.save()
        #     order.save()
        #     logger.info(f'created {cnt_orders} orders - completed')
        #
        #     lst_orders.append(order)
        # print(lst_orders)
        # self.stdout.write(f'created test data: {cnt_clients} clients,'
        #                   f' {cnt_products} products,'
        #                   f'{cnt_orders} orders')
