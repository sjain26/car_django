# Generated by Django 4.1.4 on 2023-01-03 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sold_car',
            fields=[
                ('buyer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='seller.buyer')),
            ],
            bases=('seller.buyer',),
        ),
    ]
