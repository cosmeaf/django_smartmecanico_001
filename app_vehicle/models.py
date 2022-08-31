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


class Vehicle(Base):
    """Model definition for Vehicle."""
    brand = models.CharField(
        'Marca Veículo', max_length=255, blank=False, null=False)
    model = models.CharField(
        'Modelo Veículo', max_length=255, blank=False, null=False)
    fuell = models.CharField(
        'Combustível', max_length=255, blank=False, null=False)
    year = models.CharField(
        'Ano Fabricação', max_length=4, blank=False, null=False)
    odomitter = models.CharField(
        'Hodometro', max_length=9, blank=False, null=False)
    plate = models.CharField(
        'Placa Veículo', max_length=10, blank=False, null=False)
    user = models.ForeignKey(
        User, verbose_name='Usuário', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Vehicle."""
        db_table = 'tbl_vehicle'
        verbose_name = 'vehicle'
        verbose_name_plural = 'vehicles'

    def __str__(self):
        """Unicode representation of Vehicle."""
        return self.brand
