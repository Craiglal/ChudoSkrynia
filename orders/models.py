from django.db import models
from products.models import Doll as Product


class Order(models.Model):
    first_name = models.CharField(verbose_name='Им''я', max_length=50)
    last_name = models.CharField(verbose_name='Фамілія', max_length=50)
    telephone = models.CharField(verbose_name='Телефон', max_length=10, help_text='(099-111-22-33)')
    email = models.EmailField(verbose_name='Email')
    city = models.CharField(verbose_name='Місто', max_length=100)
    created = models.DateTimeField(verbose_name='Створенний', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Оновленний', auto_now=True)
    comp = models.BooleanField(verbose_name='Виполнен', default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return 'Замовлення: {}'.format(self.id)

    def get_total_cost(self):
        return sum(elem.get_cost() for elem in self.elements.all())


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(verbose_name='Ціна', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity