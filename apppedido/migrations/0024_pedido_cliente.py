# Generated by Django 4.0.3 on 2022-03-28 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apppedido', '0023_alter_pedido_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apppedido.cliente'),
        ),
    ]