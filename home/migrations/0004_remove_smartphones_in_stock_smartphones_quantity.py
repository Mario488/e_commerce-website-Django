# Generated by Django 4.1.7 on 2023-04-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_smartphones_in_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphones',
            name='In_stock',
        ),
        migrations.AddField(
            model_name='smartphones',
            name='Quantity',
            field=models.IntegerField(default=0),
        ),
    ]
