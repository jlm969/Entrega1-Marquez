# Generated by Django 4.0.3 on 2022-03-22 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppedido', '0006_rename_id_repartdir_repartidor_id_repartidor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repartidor',
            name='num_celular',
            field=models.CharField(max_length=40),
        ),
    ]