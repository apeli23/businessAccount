# Generated by Django 2.2 on 2021-02-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps4', '0025_auto_20210212_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
