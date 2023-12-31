# Generated by Django 4.1.7 on 2023-04-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=50)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('S', 'Shipped'), ('D', 'Delivered')], max_length=1)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=40)),
                ('product', models.CharField(default='', max_length=40)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
