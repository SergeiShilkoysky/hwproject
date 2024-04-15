from django.core.management.base import BaseCommand

from myhwapp2.models import Product


class Command(BaseCommand):
    help = "Get all products"

    def handle(self, *args, **kwargs):
        all_products = Product.objects.all()
        for prod in all_products:
            self.stdout.write(f'{prod}')
