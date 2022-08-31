from django.contrib import admin
from django.utils.html import format_html

from .models import Schedule, HourAvailable
from django.contrib.auth import get_user_model
User = get_user_model()


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('address', 'vehicle', 'service', 'hour', 'day',
                    'updated_at', 'deleted_at', 'is_active', 'user')

    # exclude = ['user', ]
    list_display_links = ('day',)
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']

    def get_queryset(self, request):
        """
        Show result user by id
        """
        queryset = super(ScheduleAdmin, self).get_queryset(request)
        if (request.user.is_superuser):
            return queryset
        else:
            return queryset.filter(user_id=request.user)

    def save_model(self, request, obj, form, change):
        """
        Change Method for save Service data on Database
        """
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(HourAvailable)
class HourAvailableAdmin(admin.ModelAdmin):
    list_display = ('user', 'hourAvailable',
                    'updated_at', 'deleted_at', 'is_active', 'user')
    exclude = ['user', ]
    list_display_links = ('hourAvailable',)
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']

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
        Change Method for save Service data on Database
        """
        obj.user = request.user
        super().save_model(request, obj, form, change)
