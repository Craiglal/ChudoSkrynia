# Generated by Django 2.1.7 on 2019-04-28 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bizhuteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(verbose_name='Наявність')),
                ('time', models.CharField(default='2-3 дні', max_length=50, verbose_name='Час виготовлення')),
                ('price', models.FloatField(max_length=20, verbose_name='Ціна')),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='pic_folder/', verbose_name='Фото')),
                ('special', models.TextField(max_length=100, verbose_name='Особливості')),
            ],
            options={
                'verbose_name': 'Біжутерія',
                'verbose_name_plural': 'Біжутерія',
            },
        ),
        migrations.CreateModel(
            name='Dekupazh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(verbose_name='Наявність')),
                ('time', models.CharField(default='2-3 дні', max_length=50, verbose_name='Час виготовлення')),
                ('price', models.FloatField(max_length=20, verbose_name='Ціна')),
                ('size_height', models.FloatField(max_length=25, verbose_name='Висота')),
                ('size_width', models.FloatField(max_length=25, verbose_name='Ширина')),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='pic_folder/', verbose_name='Фото')),
                ('special', models.TextField(max_length=100, verbose_name='Особливості')),
            ],
            options={
                'verbose_name': 'Виріб декупаж',
                'verbose_name_plural': 'Вироби декупаж',
            },
        ),
        migrations.CreateModel(
            name='Dekupazh_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Категорія декупажу',
                'verbose_name_plural': 'Категорії декупажу',
            },
        ),
        migrations.CreateModel(
            name='Doll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(verbose_name='Наявність')),
                ('time', models.CharField(default='2-3 дні', max_length=50, verbose_name='Час виготовлення')),
                ('price', models.FloatField(max_length=20, verbose_name='Ціна')),
                ('size_height', models.FloatField(max_length=25, verbose_name='Висота')),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='pic_folder/', verbose_name='Фото')),
                ('special', models.TextField(max_length=100, verbose_name='Особливості')),
            ],
            options={
                'verbose_name': 'Лялька',
                'verbose_name_plural': 'Ляльки',
            },
        ),
        migrations.CreateModel(
            name='Doll_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Категорія ляльок',
                'verbose_name_plural': 'Категорії ляльок',
            },
        ),
        migrations.CreateModel(
            name='Mylo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(verbose_name='Наявність')),
                ('time', models.CharField(default='2-3 дні', max_length=50, verbose_name='Час виготовлення')),
                ('price', models.FloatField(max_length=20, verbose_name='Ціна')),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='pic_folder/', verbose_name='Фото')),
                ('special', models.TextField(max_length=100, verbose_name='Особливості')),
            ],
            options={
                'verbose_name': 'Мило',
                'verbose_name_plural': 'Мило',
            },
        ),
        migrations.CreateModel(
            name='Other_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Інша категорія',
                'verbose_name_plural': 'Інші категорії',
            },
        ),
        migrations.CreateModel(
            name='Servetky',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(verbose_name='Наявність')),
                ('time', models.CharField(default='2-3 дні', max_length=50, verbose_name='Час виготовлення')),
                ('price', models.FloatField(max_length=20, verbose_name='Ціна')),
                ('quantity', models.IntegerField(verbose_name='Кількість')),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='pic_folder/', verbose_name='Фото')),
                ('special', models.TextField(max_length=100, verbose_name='Особливості')),
            ],
            options={
                'verbose_name': 'Серветка',
                'verbose_name_plural': 'Серветки',
            },
        ),
        migrations.CreateModel(
            name='Servetky_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Категорія серветок',
                'verbose_name_plural': 'Категорії серветок',
            },
        ),
        migrations.CreateModel(
            name='Skrapbuking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(verbose_name='Наявність')),
                ('time', models.CharField(default='2-3 дні', max_length=50, verbose_name='Час виготовлення')),
                ('price', models.FloatField(max_length=20, verbose_name='Ціна')),
                ('size_height', models.FloatField(max_length=25, verbose_name='Висота')),
                ('size_width', models.FloatField(max_length=25, verbose_name='Ширина')),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='pic_folder/', verbose_name='Фото')),
                ('special', models.TextField(max_length=100, verbose_name='Особливості')),
            ],
            options={
                'verbose_name': 'Виріб скрапбукінгу',
                'verbose_name_plural': 'Вироби скрапбукінгу',
            },
        ),
        migrations.CreateModel(
            name='Skrapbuking_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Категорія скрапбукінгу',
                'verbose_name_plural': 'Категорії скрапбукінгу',
            },
        ),
        migrations.AddField(
            model_name='skrapbuking',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Skrapbuking_Category', verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='servetky',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Servetky_Category', verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='mylo',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Other_Category', verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='doll',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Doll_Category', verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='dekupazh',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Dekupazh_Category', verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='bizhuteria',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Other_Category', verbose_name='Категорія'),
        ),
    ]