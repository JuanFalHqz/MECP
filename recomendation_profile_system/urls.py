from django.urls import path
from unicodedata import name

from recomendation_profile_system.view_ import AddProfessionalOffer, DetailProfessionalOffer, add_professional_offer, ListProfessionalOffers, UpdateProfessionalOffer, \
    update_professional_offer, DeleteProfessionalOffer, UpdateSettings
from recomendation_profile_system.views import ListOffertProfessionalByGraduateProfile, UpdateSettingsForGraduate

urlpatterns = [
    path('add_job_offer/', AddProfessionalOffer.as_view(), name='add_job_offer_root'),
    path('add_job_offer_post/', add_professional_offer, name='add_job_offer_post_root'),
    path('show_job_offer/<int:pk>/', DetailProfessionalOffer.as_view(), name='detail_job_offer_root'),
    path('update_job_offer/<int:pk>/', UpdateProfessionalOffer.as_view(), name='update_job_offer_root'),
    path('update_job_offer_post/', update_professional_offer, name='update_job_offer_post_root'),
    path('list_job_offers', ListProfessionalOffers.as_view(), name='list_job_offers_root'),
    path('delete', DeleteProfessionalOffer.as_view(), name='delete_job_offers_root'),

    path('settings/<int:pk>/', UpdateSettings.as_view(), name='settings_root'),
    path('settings2/<int:pk>/', UpdateSettingsForGraduate.as_view(), name='settings_root_student'),

    path('list_job_offers_by_preferences/', ListOffertProfessionalByGraduateProfile.as_view(),
         name='list_job_offers_by_user_preferences_root'),

]
