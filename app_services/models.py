import uuid
import os
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Base(models.Model):
    user = models.ForeignKey(
        User, related_name='Usuário', on_delete=models.CASCADE)
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


class Service(Base):
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('icon', filename)

    image = models.ImageField(
        'Imagem', upload_to=get_file_path, blank=True, null=True)
    name = models.CharField('Titulo', max_length=255, editable=True)
    description = models.TextField(
        'Descrição', editable=True)

    class Meta:
        db_table = 'tbl_service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return f'{self.name}'
