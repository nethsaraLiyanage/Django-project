# Generated by Django 3.1.1 on 2020-09-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0004_auto_20200917_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='date',
        ),
        migrations.AddField(
            model_name='fooditem',
            name='fday',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='fmonth',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='fyear',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
