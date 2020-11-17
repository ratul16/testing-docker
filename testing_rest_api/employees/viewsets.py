from rest_framework import viewsets
from employees.models import EmployeeInformationModel
from employees.serializers import EmployeeInformationSerializer


class EmployeeInformationViewSet(viewsets.ModelViewSet):

    queryset = EmployeeInformationModel.objects.all()
    serializer_class = EmployeeInformationSerializer