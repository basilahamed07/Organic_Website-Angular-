# Generated by Django 3.2.19 on 2024-09-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shipping_Table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping_table',
            name='shipping_status',
            field=models.CharField(choices=[('P', 'Pending'), ('D', 'Delivered')], default='P', max_length=1),
        ),
    ]
