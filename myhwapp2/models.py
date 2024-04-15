"""Задание №8
- Создайте три модели Django: клиент, товар и заказ. Клиент
может иметь несколько заказов. Заказ может содержать
несколько товаров. Товар может входить в несколько
заказов.
    Поля модели "Клиент":
- имя клиента
- электронная почта клиента
- номер телефона клиента
- адрес клиента
- дата регистрации клиента
      Поля модели "Товар":
- название товара
- описание товара
- цена товара
- количество товара
- дата добавления товара
      Поля модели "Заказ":
- связь с моделью "Клиент", указывает на клиента, сделавшего заказ
- связь с моделью "Товар", указывает на товары,
- общая сумма заказа
- дата оформления заказа
 *Допишите несколько функций CRUD для работы с моделями по желанию.
  Что по вашему мнению актуально в такой базе данных."""

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_reg = models.DateField(auto_now_add=True)

    def __repr__(self):
        return f'client {self.name}, email: {self.email} phone: {self.phone} address: {self.address}'

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, phone: {self.phone}'


class Product(models.Model):
    name_product = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    date_added = models.DateField()

    def __repr__(self):
        return f'{self.name_product}, price: {self.price}, quantity: {self.quantity}'

    def __str__(self):
        return f'{self.name_product}, price: {self.price}'


class Order(models.Model):
    client_store = models.ForeignKey(Client, on_delete=models.CASCADE)
    basket_products = models.ManyToManyField(Product)
    order_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    # date_ordered = models.DateField(auto_now=True)
    date_ordered = models.DateField()

    # def __str__(self):
    # return (f'№{self.pk} - client: {self.client_store}, date_ordered: {self.date_ordered},'
    #         f'basket_products: {self.basket_products}')

    def __str__(self):
        return (f'{self.pk}.client: {self.client_store}, date_ordered: {self.date_ordered},'
                f'basket_products: {list(map(str, self.basket_products.all()))}')
