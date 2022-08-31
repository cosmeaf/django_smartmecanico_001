from app_hour.models import HourAvailable
from app_service.models import Service
from app_vehicle.models import Vehicle
from app_address.models import Address
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Base(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField('Ativo:', default=True)
    created_at = models.DateTimeField(
        'Data de Criação', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        'Ultima Atualização', auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(
        'Data de Exclusão', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Bases Models'


class Schedule(Base):
    user = models.ForeignKey(
        User, verbose_name='Usuário', on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name='Endereço', on_delete=models.PROTECT,
                                related_name='Address', related_query_name="Addres")
    vehicle = models.ForeignKey(Vehicle, verbose_name='Veículo', on_delete=models.PROTECT,
                                related_name='Vehicle', related_query_name="Vehicle")
    service = models.ForeignKey(Service, verbose_name='Serviço', on_delete=models.PROTECT,
                                related_name='Service', related_query_name="Service")
    hour = models.ForeignKey(HourAvailable, verbose_name='Hora', on_delete=models.PROTECT,
                             related_name='HourAvailable', related_query_name="HourAvailable")
    day = models.DateField(
        'Data do Serviço', help_text='Escolha data disponível')

    class Meta:
        db_table = 'tbl_schedule'
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return f'{self.service}'
