from rest_framework import routers
from employees.viewsets import EmployeeInformationViewSet

router = routers.DefaultRouter()

router.register(r'employee_information', EmployeeInformationViewSet)
