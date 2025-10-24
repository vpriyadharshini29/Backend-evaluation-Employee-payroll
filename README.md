# Employee Payroll & Attendance System (Django)

## Overview
Simple Django app that demonstrates:
- Employee management (Admin + UI)
- Attendance marking and monthly salary slip calculation
- Export payroll as PDF (ReportLab) and Excel (openpyxl)

## How to run (quick)
1. Create a Python virtual environment and activate it.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Apply migrations and create superuser:
   ```
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Run the dev server:
   ```
   python manage.py runserver
   ```
5. Open http://127.0.0.1:8000/ and login as the superuser to access the admin.

## Notes
- This project uses SQLite by default; no extra DB setup required.
- For PDF export we use ReportLab; for Excel export we use openpyxl.
- Static files use Bootstrap CDN in templates for better UI.

