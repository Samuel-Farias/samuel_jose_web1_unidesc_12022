# Generated by Django 4.0.5 on 2022-06-23 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mareicula_Imo', models.IntegerField(max_length=100)),
                ('vaor', models.IntegerField(max_length=100)),
            ],
        ),
    ]
