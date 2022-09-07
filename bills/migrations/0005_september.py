# Generated by Django 4.0.5 on 2022-09-06 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0004_august_july_june'),
    ]

    operations = [
        migrations.CreateModel(
            name='September',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_bills', models.CharField(max_length=255)),
                ('fixed_bills_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_date', models.DateField(blank=True)),
            ],
        ),
    ]
