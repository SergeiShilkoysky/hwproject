import logging

from django.core.management.base import BaseCommand

from ...models import Client, Product, Order

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """ table cleaning_hw3 """
    help = "Clean all tables"

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            order.delete()
        logger.info('clear all data in order table - complete successfully')

        products = Product.objects.all()
        for product in products:
            product.delete()
        logger.info('clear all data in product table - complete successfully')

        clients = Client.objects.all()
        for client in clients:
            client.delete()
        logger.info('clear all data in product table - complete successfully')
        self.stdout.write('clear all bd - complete!')
