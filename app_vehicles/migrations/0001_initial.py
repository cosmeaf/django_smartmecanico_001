# Generated by Django 4.1.1 on 2022-09-12 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo:')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização')),
                ('deleted_at', models.DateTimeField(auto_now=True, verbose_name='Data de Exclusão')),
                ('brand', models.CharField(max_length=255, verbose_name='Marca Veículo')),
                ('model', models.CharField(max_length=255, verbose_name='Modelo Veículo')),
                ('fuell', models.CharField(max_length=255, verbose_name='Combustível')),
                ('year', models.CharField(max_length=4, verbose_name='Ano Fabricação')),
                ('odomitter', models.CharField(max_length=9, verbose_name='Hodometro')),
                ('plate', models.CharField(max_length=10, verbose_name='Placa Veículo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'vehicle',
                'verbose_name_plural': 'vehicles',
                'db_table': 'tbl_vehicle',
            },
        ),
    ]