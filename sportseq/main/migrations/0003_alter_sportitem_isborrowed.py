# Generated by Django 4.0.4 on 2022-04-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_sportitem_isborrowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportitem',
            name='isBorrowed',
            field=models.BooleanField(),
        ),
    ]