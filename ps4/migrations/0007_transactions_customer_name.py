# Generated by Django 2.2 on 2020-06-03 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps4', '0006_auto_20200602_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='customer_name',
            field=models.CharField(default='client', max_length=15),
        ),
    ]
