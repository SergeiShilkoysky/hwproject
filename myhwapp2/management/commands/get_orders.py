from django.core.management.base import BaseCommand

from myhwapp2.models import Order


class Command(BaseCommand):
    help = "Get all orders"

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            self.stdout.write(f'{order}')
