# Generated by Django 4.1.2 on 2022-12-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_checkout_checkoutproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproduct',
            name='qty',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='checkoutproduct',
            name='total',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]