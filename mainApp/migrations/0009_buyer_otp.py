# Generated by Django 4.1.2 on 2022-12-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='otp',
            field=models.IntegerField(default=-1151515),
        ),
    ]