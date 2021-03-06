# Generated by Django 4.0.4 on 2022-05-05 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('rollNo', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SportItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('isBorrowed', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
