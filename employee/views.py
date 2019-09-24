from rest_framework_mongoengine import viewsets as meviewsets

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeView(meviewsets.ModelViewSet):
    lookup_field = 'employeeId'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
