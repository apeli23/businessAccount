# Generated by Django 2.2 on 2020-06-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps4', '0005_auto_20200519_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsandservices',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
