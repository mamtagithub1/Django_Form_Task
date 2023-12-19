from django.contrib import admin
from .models import Employee
from .forms import EmployeeForm
# Register your models here.
class emp_admin(admin.ModelAdmin):
    list_display=('eid','ename','eemail','econtact')

admin.site.register(Employee,emp_admin)