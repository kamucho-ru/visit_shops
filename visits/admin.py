from django.contrib import admin
from django.contrib.auth.models import Group

from visits.models import Outlet, Visit, Worker


admin.site.register(Worker)
admin.site.register(Outlet)
admin.site.register(Visit)
admin.site.unregister(Group)
