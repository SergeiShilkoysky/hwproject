from django.core.management import BaseCommand

from myhwapp2.models import Client


class Command(BaseCommand):
    help = "Update name&phone client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='username')
        parser.add_argument('phone', type=str, help='phone')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        phone = kwargs.get('phone')
        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.phone = phone
        client.save()
        self.stdout.write(f'{client}')

# Выполним команду

# >python manage.py update_user 2 Smith


# Здесь мы получаем пользователя с первичным ключом 2, изменяем его имя на
# "Smith" и сохраняем изменения в базе данных с помощью метода "save()".
