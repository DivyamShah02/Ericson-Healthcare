from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PADeathReport)
admin.site.register(TTDReport)
admin.site.register(HealthClaimReport)
admin.site.register(CashlessClaimReport)
admin.site.register(ClaimReport)
admin.site.register(HDCClosureReport)
admin.site.register(ICLMClosureReport)
admin.site.register(SecureMindCriticalIllnessReport)
