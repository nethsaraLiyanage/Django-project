# Generated by Django 3.1.1 on 2020-09-13 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'managed': False},
        ),
    ]
