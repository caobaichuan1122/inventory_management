# Generated by Django 3.2.13 on 2022-06-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=256)),
                ('customer_name', models.CharField(max_length=256)),
                ('customer_phone', models.CharField(max_length=256)),
                ('customer_address', models.CharField(max_length=256)),
                ('customer_email', models.CharField(max_length=256)),
                ('customer_type', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='fix_tp_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_id', models.CharField(max_length=256)),
                ('tp_product_id', models.CharField(max_length=256)),
                ('tp_product_name', models.CharField(max_length=256)),
                ('tp_product_description', models.CharField(max_length=256)),
                ('fix_state', models.CharField(max_length=256)),
                ('fixed_detail', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='fix_tr_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_id', models.CharField(max_length=256)),
                ('tr_product_id', models.CharField(max_length=256)),
                ('tr_product_name', models.CharField(max_length=256)),
                ('tr_product_description', models.CharField(max_length=256)),
                ('fix_state', models.CharField(max_length=256)),
                ('fixed_detail', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Prproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_product_id', models.CharField(max_length=256)),
                ('pr_product_name', models.CharField(max_length=256)),
                ('pr_product_num', models.CharField(max_length=256)),
                ('pr_product_price', models.CharField(max_length=256)),
                ('pr_product_time', models.DateField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Tproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tp_product_id', models.CharField(max_length=256)),
                ('tp_product_name', models.CharField(max_length=256)),
                ('tp_product_num', models.CharField(max_length=256)),
                ('tp_product_price', models.CharField(max_length=256)),
                ('tp_product_time', models.DateField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Trproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tr_product_id', models.CharField(max_length=256)),
                ('tr_product_name', models.CharField(max_length=256)),
                ('tr_product_num', models.CharField(max_length=256)),
                ('tr_product_price', models.CharField(max_length=256)),
                ('tr_product_time', models.DateField(max_length=6)),
            ],
        ),
    ]
