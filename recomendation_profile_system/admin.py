from django.contrib import admin

from recomendation_profile_system.models import ProfessionalOffer, Settings
from student.models import Ability

# Register your models here.
admin.site.register(ProfessionalOffer)
admin.site.register(Settings)
