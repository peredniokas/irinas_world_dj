# Generated by Django 4.1.3 on 2022-12-05 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
