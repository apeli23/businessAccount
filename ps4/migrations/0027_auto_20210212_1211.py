# Generated by Django 2.2 on 2021-02-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps4', '0026_auto_20210212_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
