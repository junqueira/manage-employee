from django.contrib import admin

from .models import User, Department, Employee, Photo


admin.site.register(User)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Photo)
