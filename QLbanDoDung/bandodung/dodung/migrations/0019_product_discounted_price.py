# Generated by Django 4.2.15 on 2024-09-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dodung', '0018_order_bank_transfer_image_alter_order_payment_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discounted_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
