# Generated by Django 4.2 on 2024-10-12 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_passphrase'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Passphrase',
        ),
    ]
