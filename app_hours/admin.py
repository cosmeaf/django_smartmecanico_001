from django.contrib import admin
from .models import HourAvailable
# Register your models here.


@admin.register(HourAvailable)
class HourAvailableAdmin(admin.ModelAdmin):
    list_display = ('hourAvailable', 'user')
    # exclude = ['user', ]
    list_display_links = ('hourAvailable',)
    readonly_fields = ['user', 'created_at', 'updated_at', 'deleted_at']

    def usuario(self, instance):
        return f'{instance.user.get_full_name()}'

    def get_queryset(self, request):
        """
        Show result user by id
        """
        queryset = super(HourAvailableAdmin, self).get_queryset(request)
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
