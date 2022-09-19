# Generated by Django 4.0.5 on 2022-09-19 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bills', '0005_september'),
    ]

    operations = [
        migrations.CreateModel(
            name='October',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_bills', models.CharField(max_length=255)),
                ('fixed_bills_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_date', models.DateField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]