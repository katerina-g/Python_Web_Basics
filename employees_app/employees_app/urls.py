from django.contrib import admin
from django.urls import path, include

from employees_app.employees.views import home, go_to_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('go-to-home/', go_to_home, name='go to home'),

    path('departments/', include('employees_app.employees.urls'))
]
