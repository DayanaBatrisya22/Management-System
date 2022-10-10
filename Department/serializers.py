from rest_framework import serializers
from .models import SystemAnalyst
from .models import SoftwareTester
from .models import DataScientist
from .models import BackEnd
from .models import FrontEnd
from .models import UiUx
from .models import SalesMarketing

#Json for SA
class SystemAnalystSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAnalyst
        fields = ['id', 'Name', 'EmployeeID',  'MonthlySalary']

#Json for ST
class SoftwareTesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareTester
        fields = ['id', 'Name', 'EmployeeID',  'MonthlySalary']

#Json for DS
class DataScientistSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataScientist
        fields = ['id', 'Name', 'EmployeeID', 'MonthlySalary']
    
#Json for BE
class BackEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackEnd
        fields = ['id', 'Name', 'EmployeeID', 'MonthlySalary']

#Json for FE
class FrontEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontEnd
        fields = ['id', 'Name', 'EmployeeID', 'MonthlySalary']

#Json for UiUx
class UiUxSerializer(serializers.ModelSerializer):
    class Meta:
        model = UiUx
        fields = ['id', 'Name', 'EmployeeID',  'MonthlySalary']
    
#Json for SM
class SalesMarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesMarketing
        fields = ['id', 'Name', 'EmployeeID', 'MonthlySalary']