# Generated by Django 2.2 on 2020-10-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps4', '0014_auto_20201025_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_type',
            field=models.CharField(choices=[('Income', 'income'), ('Expense', 'expense'), ('Liability', 'liability')], default='Income', max_length=10),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='unit_price',
            field=models.IntegerField(default=0),
        ),
    ]
