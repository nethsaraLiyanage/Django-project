# Generated by Django 3.1.1 on 2020-09-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0003_fooditem_ingrediants_utilcost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='costMargin',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='netProfit',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='salesPrice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='totalCost',
            field=models.FloatField(null=True),
        ),
    ]
