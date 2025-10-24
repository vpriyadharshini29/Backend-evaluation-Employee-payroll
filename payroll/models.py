from django.db import models
from django.urls import reverse

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=150, blank=True)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_joined = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    present = models.BooleanField(default=True)

    class Meta:
        unique_together = ('employee','date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee} - {self.date} - {'P' if self.present else 'A'}"

class PayrollRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payrolls')
    month = models.DateField(help_text='Use any date within the month (e.g., 2025-10-01)')
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-month']
