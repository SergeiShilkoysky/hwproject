import logging

from django.core.management.base import BaseCommand

from ...models import Client, Product, Order
from ...random_date import gen_datetime

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create order hw3"

    def add_arguments(self, parser):  # python manage.py create_orders_hw3 -c 4 -p 7

        parser.add_argument('-c', '--id_client', type=int, help="id_client")
        parser.add_argument('-p', '--id_product', type=int, help="id_product")
        # parser.add_argument('-p', '--id_product', nargs='+', type=int, help="id_product")

    def handle(self, *args, **kwargs):
        id_client = kwargs.get('id_client')
        lst_id_input_products = [kwargs.get('id_product')]
        # print(lst_id_input_products)
        # print(type(lst_id_input_products))

        order = Order(client_store=Client.objects.filter(pk=id_client).first(), date_ordered=gen_datetime(), )

        sum_ = 0
        for i in range(len(lst_id_input_products)):
            new_product = Product.objects.filter(pk=lst_id_input_products[i]).first()
            # print(new_product)
            sum_ += float(new_product.price)
            order.order_total = sum_
            order.save()
            order.basket_products.add(new_product)
            logger.info('created orders - ok')
            self.stdout.write(f'{order}')
