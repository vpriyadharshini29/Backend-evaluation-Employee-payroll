from django.urls import path
from . import views

app_name = 'payroll'
urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_create, name='employee_add'),
    path('employees/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/mark/', views.attendance_mark, name='attendance_mark'),
    path('payrolls/', views.payroll_list, name='payroll_list'),
    path('payrolls/generate/', views.generate_payroll, name='generate_payroll'),
    path('payrolls/<int:pk>/pdf/', views.payroll_pdf, name='payroll_pdf'),
    path('payrolls/export/excel/', views.export_payroll_excel, name='export_payroll_excel'),
]
