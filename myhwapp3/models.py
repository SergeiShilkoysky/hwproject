"""Задание №7
📌 Доработаем задачу 8 из прошлого семинара про клиентов,
товары и заказы.
📌 Создайте шаблон для вывода всех заказов клиента и
списком товаров внутри каждого заказа.
📌 Подготовьте необходимый маршрут и представление."""

"""📌 Продолжаем работать с товарами и заказами.
📌 Создайте шаблон, который выводит список заказанных
клиентом товаров из всех его заказов с сортировкой по
времени:
○ за последние 7 дней (неделю)
○ за последние 30 дней (месяц)
○ за последние 365 дней (год)
📌 *Товары в списке не должны повторятся."""

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_reg = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    # def __repr__(self):
    #     return (f'client <{self.name}>, email: <{self.email}>,'
    #             f' phone: <{self.phone}>, address: <{self.address}>')

    def __repr__(self):
        return (f'client <{self.name}>, email: <{self.email}>, phone: <{self.phone}>, address: <{self.address}>, '
                f'registered <{self.date_reg}>')


class Product(models.Model):
    name_product = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    date_add = models.DateField()

    # def __repr__(self):
    #     return f'<prod_name: <{self.name_product}>, price: <{self.price}>, quantity: <{self.quantity}>'

    def __str__(self):
        return (f'name_prod: <{self.name_product}>,'
                f' description: <{self.description}>'
                f' price: <{self.price}>,'
                f' quantity: <{self.quantity}>,'
                f' manufacture date: <{self.date_add}>')


class Order(models.Model):
    client_store = models.ForeignKey(Client, on_delete=models.CASCADE)
    basket_products = models.ManyToManyField(Product)
    order_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    # date_ordered = models.DateField(auto_now_add=True)
    date_ordered = models.DateField()
    date_change = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # def __str__(self):
    #     return (f' заказ №_{self.pk}, client: <{self.client_store.name}>,'
    #             f' basket_products: <{list(map(str, self.basket_products.all()))}>,'
    #             f' order_total: <{self.order_total}>,'
    #             f' date_ordered: <{self.date_ordered}>')

    def __str__(self):
        return f'{list(map(str, self.basket_products.all()))}'


class BasketProduct(models.Model):
    order_client = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return (f'{self.order_client.primary_key}:'
                f' {self.product.name} - количество {self.quantity}) ')
