from django.urls import path

from employees_app.employees.views import department_details, list_departments, create_department

urlpatterns = [
    path('create/', create_department),
    path('<int:id>/', department_details, name='department details'),
    path('', list_departments, name='list departments'),
]
