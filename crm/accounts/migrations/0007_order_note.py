# Generated by Django 4.2 on 2023-07-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_order_customer_alter_order_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
