from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Hod, Principal, Student, Staff

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    list_display = UserAdmin.list_display + ('role',)
    list_filter = UserAdmin.list_filter + ('role',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Hod)
admin.site.register(Principal)
admin.site.register(Student)
admin.site.register(Staff)
