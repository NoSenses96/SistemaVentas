# Generated by Django 3.1.3 on 2020-12-04 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20201204_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='hora',
        ),
    ]
