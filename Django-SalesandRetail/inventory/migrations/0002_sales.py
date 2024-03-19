# Generated by Django 5.0.3 on 2024-03-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('customer_name', models.CharField(max_length=40)),
                ('customer_email', models.CharField(max_length=20)),
                ('PS_Type', models.CharField(max_length=20)),
                ('PS_Name', models.CharField(max_length=15)),
                ('PS_Brand', models.CharField(max_length=10)),
                ('QuantitySold', models.IntegerField()),
                ('PS_Date', models.DateField(blank=True, null=True)),
                ('SellingPrice', models.IntegerField()),
            ],
        ),
    ]