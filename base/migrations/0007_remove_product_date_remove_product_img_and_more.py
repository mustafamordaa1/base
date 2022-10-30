# Generated by Django 4.1.2 on 2022-10-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_date_purchase_buy_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='content',
            field=models.CharField(default='none', max_length=10000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
