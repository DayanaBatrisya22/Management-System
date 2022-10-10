from django.contrib import admin
from .models import SystemAnalyst
from .models import SoftwareTester
from .models import DataScientist
from .models import BackEnd
from .models import FrontEnd
from .models import UiUx
from .models import SalesMarketing

admin.site.register(SystemAnalyst)
admin.site.register(SoftwareTester)
admin.site.register(DataScientist)
admin.site.register(BackEnd)
admin.site.register(FrontEnd)
admin.site.register(UiUx)
admin.site.register(SalesMarketing)