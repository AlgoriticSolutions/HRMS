from django.shortcuts import render

# Create your views here.
def employee_dashboard(request):
    return render(request,'employees/employee_templates/employee_dashboard.html')