from django.contrib import admin
from .models import Vehicle
# Register your models here.


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'fuell', 'year',
                    'odomitter', 'plate', 'user')
    # exclude = ['user', ]
    list_display_links = ('plate',)
    readonly_fields = ['created_at', 'updated_at']

    def usuario(self, instance):
        return f'{instance.user.get_full_name()}'

    """
    Show result user by id
    """

    def get_queryset(self, request):
        queryset = super(VehicleAdmin, self).get_queryset(request)
        if (request.user.is_superuser):
            return queryset
        else:
            return queryset.filter(user_id=request.user)

    """
    Change Method for save Vehicle data on Database
    """

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
