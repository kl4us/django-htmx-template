from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import Group

from groupadmin_users.forms import GroupAdminForm

admin.site.unregister(Group)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    filter_horizontal = ['permissions']