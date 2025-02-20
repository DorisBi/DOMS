# Generated by Django 2.2.4 on 2019-08-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(max_length=20)),
                ('customer_address', models.TextField()),
                ('creation_date', models.DateField(blank=True)),
                ('product_id', models.TextField()),
                ('payment_option', models.CharField(max_length=50)),
                ('number_of_packets', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('inventory_warehouse', models.CharField(max_length=200)),
                ('transportation_vender', models.CharField(max_length=200)),
                ('delivery_order_id', models.CharField(max_length=50)),
                ('order_status', models.CharField(max_length=50)),
            ],
        ),
    ]
