# Generated by Django 4.0.3 on 2022-03-25 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apppedido', '0014_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='camadao',
            new_name='camada',
        ),
    ]
