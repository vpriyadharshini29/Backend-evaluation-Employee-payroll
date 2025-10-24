from django.contrib import admin
from .models import Employee, Attendance, PayrollRecord

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','designation','basic_salary','date_joined')
    search_fields = ('first_name','last_name','email')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee','date','present')
    list_filter = ('present','date','employee')

@admin.register(PayrollRecord)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee','month','gross_salary','net_salary','created_at')
    list_filter = ('month','employee')
