# Generated by Django 4.0.5 on 2022-10-08 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0007_june_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='August',
        ),
        migrations.DeleteModel(
            name='Bills',
        ),
        migrations.DeleteModel(
            name='January',
        ),
        migrations.DeleteModel(
            name='July',
        ),
        migrations.RemoveField(
            model_name='october',
            name='user',
        ),
        migrations.DeleteModel(
            name='September',
        ),
        migrations.DeleteModel(
            name='October',
        ),
    ]
