from django.contrib import admin
from django.contrib.auth.models import Group

from visits.models import Outlet, Visit, Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Outlet)
class OutletAdmin(admin.ModelAdmin):
    search_fields = ("title",)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    search_fields = ("outlet__title", "outlet__worker__name")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.unregister(Group)
