# Generated by Django 2.2 on 2020-11-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps4', '0015_auto_20201029_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]