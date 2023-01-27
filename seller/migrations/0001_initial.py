# Generated by Django 4.1.4 on 2023-01-03 11:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=50)),
                ('seller_mobile', models.IntegerField()),
                ('model_name', models.CharField(max_length=50)),
                ('manufactured_date', models.DateField()),
                ('description', models.TextField(max_length=200)),
                ('condtion_car', models.CharField(choices=[('P', 'poor'), ('F', 'fair'), ('G', 'good'), ('E', 'excellent')], max_length=1)),
                ('asking_price', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1000)])),
                ('make_available', models.BooleanField(default=False)),
            ],
            managers=[
                ('custom', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=50)),
                ('buyer_mobile', models.IntegerField()),
                ('car_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='seller.car_list')),
            ],
        ),
    ]
