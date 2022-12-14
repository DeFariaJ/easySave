# Generated by Django 4.0.5 on 2022-08-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_bills', models.CharField(max_length=255)),
                ('fixed_bills_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_date', models.DateField(blank=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
