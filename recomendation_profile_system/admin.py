from django.contrib import admin

from recomendation_profile_system.models import JobOffer, Settings
from student.models import Ability

# Register your models here.
admin.site.register(JobOffer)
admin.site.register(Settings)
