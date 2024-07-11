from django.urls import path
from . import views
from employees.views import employee_dashboard
urlpatterns = [
    
    path('',views.home,name='home'),
    path('employee_dashboard',employee_dashboard,name='employee_dashboard'),
   
]
