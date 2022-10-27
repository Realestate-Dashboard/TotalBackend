# Generated by Django 4.1.2 on 2022-10-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinInforamtionally',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('k_name', models.CharField(default='', max_length=20)),
                ('e_name', models.CharField(default='', max_length=50)),
                ('market_name', models.CharField(default='', max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'coin',
            },
        ),
        migrations.CreateModel(
            name='RealstateInformationlly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50, verbose_name='지역')),
                ('price', models.BigIntegerField(verbose_name='가격')),
            ],
            options={
                'db_table': 'real',
            },
        ),
        migrations.CreateModel(
            name='StockInformationally',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('k_name', models.CharField(default='', max_length=20)),
                ('e_name', models.CharField(default='', max_length=50)),
                ('market_name', models.CharField(default='', max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'stock',
            },
        ),
    ]
