from rest_framework import serializers
from employees.models import EmployeeInformationModel

class EmployeeInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeInformationModel
        fields = '__all__'