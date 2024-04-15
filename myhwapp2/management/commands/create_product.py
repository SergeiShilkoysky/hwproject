from django.core.management.base import BaseCommand

from myhwapp2.models import Product


class Command(BaseCommand):
    help = "create product"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='name_product')
        parser.add_argument("description", type=str, help="description")
        parser.add_argument("price", type=float, help="price")
        parser.add_argument("quantity", type=int, help="quantity")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')

        product = Product(name_product=name, description=description, price=price, quantity=quantity)
        product.save()

        self.stdout.write(f'{product}')
