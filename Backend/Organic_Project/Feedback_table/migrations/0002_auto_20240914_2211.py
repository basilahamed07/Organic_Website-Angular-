# Generated by Django 3.2.19 on 2024-09-14 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback_table', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='remarks',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='rating',
        ),
    ]
