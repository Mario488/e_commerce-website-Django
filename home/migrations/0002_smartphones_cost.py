# Generated by Django 4.1.7 on 2023-04-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphones',
            name='Cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
