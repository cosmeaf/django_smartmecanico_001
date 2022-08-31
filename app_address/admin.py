from django.contrib import admin
from .models import Address
# Register your models here.


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'complemento',
                    'bairro', 'localidade', 'created_at', 'updated_at', 'deleted_at', 'user')
    # exclude = ['user', ]
    list_display_links = ('cep',)
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']

    def usuario(self, instance):
        return f'{instance.user.get_full_name()}'

    def get_queryset(self, request):
        """
        Show result user by id
        """
        queryset = super(AddressAdmin, self).get_queryset(request)
        if (request.user.is_superuser):
            return queryset
        else:
            return queryset.filter(user_id=request.user)

    def save_model(self, request, obj, form, change):
        """
        Change Method for save Vehicle data on Database
        """
        obj.user = request.user
        super().save_model(request, obj, form, change)
