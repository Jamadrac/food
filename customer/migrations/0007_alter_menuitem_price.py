# Generated by Django 4.1.3 on 2023-01-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_menuitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.IntegerField(),
        ),
    ]
