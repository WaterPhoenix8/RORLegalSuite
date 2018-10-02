from django.contrib import admin

from .models import Suffix, Seafarer, LocalAgent, Principal, Correspondent, CaseHandler, Vessel, TypeOfClaim, CounselOfSeafarer, Club, Case

admin.site.register(Suffix)
admin.site.register(Seafarer)
admin.site.register(LocalAgent)
admin.site.register(Principal)
admin.site.register(Correspondent)
admin.site.register(CaseHandler)
admin.site.register(Vessel)
admin.site.register(TypeOfClaim)
admin.site.register(CounselOfSeafarer)
admin.site.register(Club)
admin.site.register(Case)

# Register your models here.
