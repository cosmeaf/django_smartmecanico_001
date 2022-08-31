from django.contrib import admin
from django.utils.html import format_html

from .models import Service
from django.contrib.auth import get_user_model
User = get_user_model()


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'name', 'created_at',
                    'updated_at', 'deleted_at', 'is_active', 'user')

    exclude = ['user', ]
    list_display_links = ('name',)
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']

    def image_tag(self, obj):
        return format_html('<img src="{0}", style="width: 40px;" />'.format(obj.image.url))

    def delete(self, *args, **kwargs):
        """
        Delete Image From Media
        """
        storage, path = self.image.storage, self.image.path
        super(Service, self).delete(*args, **kwargs)
        storage.delete(path)

    def get_queryset(self, request):
        """
        Show result user by id
        """
        queryset = super(ServiceAdmin, self).get_queryset(request)
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
