# Generated by Django 4.1 on 2022-08-30 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_vehicle', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_service', '0001_initial'),
        ('app_address', '0001_initial'),
        ('app_hour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo:')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização')),
                ('deleted_at', models.DateTimeField(auto_now=True, verbose_name='Data de Exclusão')),
                ('day', models.DateField(help_text='Escolha data disponível', verbose_name='Data do Serviço')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Address', related_query_name='Addres', to='app_address.address', verbose_name='Endereço')),
                ('hour', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='HourAvailable', related_query_name='HourAvailable', to='app_hour.houravailable', verbose_name='Hora')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Service', related_query_name='Service', to='app_service.service', verbose_name='Serviço')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Vehicle', related_query_name='Vehicle', to='app_vehicle.vehicle', verbose_name='Veículo')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
                'db_table': 'tbl_schedule',
            },
        ),
    ]
