# Generated by Django 4.0.5 on 2022-06-23 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataDesocupacao', models.DateField(max_length=100)),
                ('periodo', models.DateField(max_length=100)),
            ],
        ),
    ]
