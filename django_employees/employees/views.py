from django.shortcuts import render, get_object_or_404
from . models import Employee
from .forms import EmployeeForm

# Decide with url pattern to create
# created url patter in the main urls. and forward it to emlpoyees.urls
# created the view
# created the template

def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    print(employee)
    context = {
        'employee':employee
    }
    return render(request, 'employee_detail.html', context)


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form = EmployeeForm()
    context = {
        'form' : form,
    }
    return render(request, 'add_employee.html', context)
