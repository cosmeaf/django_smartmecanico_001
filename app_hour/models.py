from django.db import models
from django.contrib.auth.models import User


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


class HourAvailable(Base):
    user = models.ForeignKey(
        User, verbose_name='Usuário', on_delete=models.CASCADE)
    hourAvailable = models.CharField('Hora Serviço', max_length=8)

    class Meta:
        db_table = 'tbl_hour'
        verbose_name = 'HourAvailable'
        verbose_name_plural = 'HourAvailables'

    def __str__(self):
        return f'{self.hourAvailable}'
