from django.core.management import BaseCommand

from myhwapp2.models import Client


class Command(BaseCommand):
    help = "create user"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='username')
        parser.add_argument('email', type=str, help='email')
        parser.add_argument('phone', type=str, help='phone')
        parser.add_argument('address', type=str, help='address')

    def handle(self, *args, **kwargs):
        new_client = Client.objects.create(
            name=kwargs['name'],
            email=kwargs['email'],
            phone=kwargs['phone'],
            address=kwargs['address'])
        new_client.save()
        self.stdout.write(f'{new_client}')
