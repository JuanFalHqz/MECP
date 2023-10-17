from django.urls import path
from unicodedata import name

from recomendation_profile_system.view_ import AddJobOffer, DetailJobOffer, add_job_offer, ListJobOffer, UpdateJobOffer, \
    update_job_offer, DeleteJobOffer, ListProfileProfessionals, UpdateSettings
from recomendation_profile_system.views import ListOffertProfessionalByUserPreferences, UpdateSettingsToUser

urlpatterns = [
    path('add_job_offer/', AddJobOffer.as_view(), name='add_job_offer_root'),
    path('add_job_offer_post/', add_job_offer, name='add_job_offer_post_root'),
    path('show_job_offer/<int:pk>/', DetailJobOffer.as_view(), name='detail_job_offer_root'),
    path('update_job_offer/<int:pk>/', UpdateJobOffer.as_view(), name='update_job_offer_root'),
    path('update_job_offer_post/', update_job_offer, name='update_job_offer_post_root'),
    path('list_job_offers', ListJobOffer.as_view(), name='list_job_offers_root'),
    path('list_profiles', ListProfileProfessionals.as_view(), name='list_profiles_root'),
    path('delete', DeleteJobOffer.as_view(), name='delete_job_offers_root'),

    path('settings/<int:pk>/', UpdateSettings.as_view(), name='settings_root'),
    path('settings2/<int:pk>/', UpdateSettingsToUser.as_view(), name='settings_root_student'),

    path('list_job_offers_by_preferences/', ListOffertProfessionalByUserPreferences.as_view(),
         name='list_job_offers_by_user_preferences_root'),

]
