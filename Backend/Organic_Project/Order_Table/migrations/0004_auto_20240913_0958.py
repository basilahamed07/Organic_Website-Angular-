# Generated by Django 3.2.19 on 2024-09-13 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order_Table', '0003_auto_20240909_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_table',
            name='latitude',
            field=models.FloatField(default=46.8182),
        ),
        migrations.AddField(
            model_name='order_table',
            name='longitude',
            field=models.FloatField(default=8.2275),
        ),
    ]
