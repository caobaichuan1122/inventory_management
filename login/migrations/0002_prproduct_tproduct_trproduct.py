# Generated by Django 3.2.13 on 2022-05-31 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_product', models.CharField(max_length=256)),
                ('pr_product_name', models.CharField(max_length=256)),
                ('pr_product_description', models.CharField(max_length=256)),
                ('pr_product_state', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Tproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tp_product', models.CharField(max_length=256)),
                ('tr_product', models.CharField(max_length=256)),
                ('pr_product', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Trproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tr_product', models.CharField(max_length=256)),
                ('tr_product_name', models.CharField(max_length=256)),
                ('tr_product_description', models.CharField(max_length=256)),
            ],
        ),
    ]
