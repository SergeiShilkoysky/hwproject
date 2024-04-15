import logging

from django.core.management.base import BaseCommand

from myhwapp2.models import Client, Product, Order

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("id_client", type=int, help="id_client")
        parser.add_argument("id_product", type=int, help="id_product")
        # parser.add_argument('--id_input_product', nargs='+', type=int, help="id_input_product")

    def handle(self, *args, **kwargs):
        id_client = kwargs.get('id_client')
        lst_id_input_products = [kwargs.get('id_product')]
        # print(lst_id_input_products)
        # print(type(lst_id_input_products))

        order = Order(client_store=Client.objects.filter(pk=id_client).first())

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
