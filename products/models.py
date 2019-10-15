from django.db import models


class Doll_Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва")

    class Meta:
        verbose_name = 'Категорія ляльок'
        verbose_name_plural = 'Категорії ляльок'

    def __str__(self):
        return str(self.name)


class Doll(models.Model):
    product_category = models.ForeignKey(Doll_Category, verbose_name="Категорія", on_delete=models.CASCADE, null=True)
    availability = models.BooleanField(verbose_name="Наявність")
    time = models.CharField(default="2-3 дні", max_length=50, verbose_name="Час виготовлення")
    price = models.FloatField(max_length=20, verbose_name="Ціна")
    size_height = models.FloatField(max_length=25, verbose_name="Висота")
    pictures = models.ImageField(upload_to='pic_folder/', verbose_name="Фото", null=True, blank=True)
    special = models.TextField(max_length=100, verbose_name='Особливості')

    class Meta:
        verbose_name = 'Лялька'
        verbose_name_plural = 'Ляльки'

    def __str__(self):
        return f'ID - {self.id}, Категорія  - {self.product_category} , Ціна -  {self.price} , Наявність - {self.availability}'


class Dekupazh_Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва")

    class Meta:
        verbose_name = 'Категорія декупажу'
        verbose_name_plural = 'Категорії декупажу'

    def __str__(self):
        return str(self.name)


class Dekupazh(models.Model):
    product_category = models.ForeignKey(Dekupazh_Category, verbose_name="Категорія", on_delete=models.CASCADE, null=True)
    availability = models.BooleanField(verbose_name="Наявність")
    time = models.CharField(default="2-3 дні", max_length=50, verbose_name="Час виготовлення")
    price = models.FloatField(max_length=20, verbose_name="Ціна")
    size_height = models.FloatField(max_length=25, verbose_name="Висота")
    size_width = models.FloatField(max_length=25, verbose_name="Ширина")
    pictures = models.ImageField(upload_to='pic_folder/', verbose_name="Фото", null=True, blank=True)
    special = models.TextField(max_length=100, verbose_name='Особливості')

    class Meta:
        verbose_name = 'Виріб декупаж'
        verbose_name_plural = 'Вироби декупаж'

    def __str__(self):
        return f'ID - {self.id}, Категорія  - {self.product_category} , Ціна -  {self.price} , Наявність - {self.availability}'


class Skrapbuking_Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва")

    class Meta:
        verbose_name = 'Категорія скрапбукінгу'
        verbose_name_plural = 'Категорії скрапбукінгу'

    def __str__(self):
        return str(self.name)


class Skrapbuking(models.Model):
    product_category = models.ForeignKey(Skrapbuking_Category, verbose_name="Категорія", on_delete=models.CASCADE, null=True)
    availability = models.BooleanField(verbose_name="Наявність")
    time = models.CharField(default="2-3 дні", max_length=50, verbose_name="Час виготовлення")
    price = models.FloatField(max_length=20, verbose_name="Ціна")
    size_height = models.FloatField(max_length=25, verbose_name="Висота")
    size_width = models.FloatField(max_length=25, verbose_name="Ширина")
    pictures = models.ImageField(upload_to='pic_folder/', verbose_name="Фото", null=True, blank=True)
    special = models.TextField(max_length=100, verbose_name='Особливості')

    class Meta:
        verbose_name = 'Виріб скрапбукінгу'
        verbose_name_plural = 'Вироби скрапбукінгу'

    def __str__(self):
        return f'ID - {self.id}, Категорія  - {self.product_category} , Ціна -  {self.price} , Наявність - {self.availability}'


class Servetky_Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва")

    class Meta:
        verbose_name = 'Категорія серветок'
        verbose_name_plural = 'Категорії серветок'

    def __str__(self):
        return str(self.name)


class Servetky(models.Model):
    product_category = models.ForeignKey(Servetky_Category, verbose_name="Категорія", on_delete=models.CASCADE, null=True)
    availability = models.BooleanField(verbose_name="Наявність")
    time = models.CharField(default="2-3 дні", max_length=50, verbose_name="Час виготовлення")
    price = models.FloatField(max_length=20, verbose_name="Ціна")
    quantity = models.IntegerField(verbose_name="Кількість")
    pictures = models.ImageField(upload_to='pic_folder/', verbose_name="Фото", null=True, blank=True)
    special = models.TextField(max_length=100, verbose_name='Особливості')

    class Meta:
        verbose_name = 'Серветка'
        verbose_name_plural = 'Серветки'

    def __str__(self):
        return f'ID - {self.id}, Категорія  - {self.product_category} , Ціна -  {self.price} , Наявність - {self.availability}'


class Other_Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва")

    class Meta:
        verbose_name = 'Інша категорія'
        verbose_name_plural = 'Інші категорії'

    def __str__(self):
        return str(self.name)


class Mylo(models.Model):
    product_category = models.ForeignKey(Other_Category, verbose_name="Категорія", on_delete=models.CASCADE, null=True)
    availability = models.BooleanField(verbose_name="Наявність")
    time = models.CharField(default="2-3 дні", max_length=50, verbose_name="Час виготовлення")
    price = models.FloatField(max_length=20, verbose_name="Ціна")
    pictures = models.ImageField(upload_to='pic_folder/', verbose_name="Фото", null=True, blank=True)
    special = models.TextField(max_length=100, verbose_name='Особливості')

    class Meta:
        verbose_name = 'Мило'
        verbose_name_plural = 'Мило'

    def __str__(self):
        return f'ID - {self.id}, Категорія  - {self.product_category} , Ціна -  {self.price} , Наявність - {self.availability}'


class Bizhuteria(models.Model):
    product_category = models.ForeignKey(Other_Category, verbose_name="Категорія", on_delete=models.CASCADE, null=True)
    availability = models.BooleanField(verbose_name="Наявність")
    time = models.CharField(default="2-3 дні", max_length=50, verbose_name="Час виготовлення")
    price = models.FloatField(max_length=20, verbose_name="Ціна")
    pictures = models.ImageField(upload_to='pic_folder/', verbose_name="Фото", null=True, blank=True)
    special = models.TextField(max_length=100, verbose_name='Особливості')

    class Meta:
        verbose_name = 'Біжутерія'
        verbose_name_plural = 'Біжутерія'

    def __str__(self):
        return f'ID - {self.id}, Категорія  - {self.product_category} , Ціна -  {self.price} , Наявність - {self.availability}'
