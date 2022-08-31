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


class Address(Base):
    SEXO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espirito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MS", "Mato Grosso do Sul"),
        ("MT", "Mato Grosso"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )
    cep = models.CharField('Cep', max_length=10)
    user = models.ForeignKey(
        User, verbose_name='Usuário', on_delete=models.CASCADE)
    logradouro = models.CharField(
        'Logradouro', max_length=255, blank=False, null=False)
    complemento = models.CharField(
        'Complemento', max_length=255, blank=False, null=False)
    bairro = models.CharField(
        'Bairro', max_length=255, blank=False, null=False)
    localidade = models.CharField(
        'Cidade', max_length=255, blank=False, null=False)
    uf = models.CharField('Estado', max_length=2, choices=SEXO_CHOICES,
                          blank=False, null=False, editable=True)

    class Meta:
        db_table = 'tbl_address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.cep}'
