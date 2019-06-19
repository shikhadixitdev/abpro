from django.contrib import admin
from .models import Customer, Emp, Student


class AdminCustomer(admin.ModelAdmin):
    list_display = ['name', 'loc', 'sales']


class AdminEmp(admin.ModelAdmin):
    list_display = ['name', 'loc', 'salary']


class AdminStudent(admin.ModelAdmin):
    list_display = ['name', 'loc', 'fee']


admin.site.register(Customer, AdminCustomer)
admin.site.register(Emp, AdminEmp)
admin.site.register(Student, AdminStudent)

# Register your models here.

