from django.urls import path
from unicodedata import name

from recomendation_profile_system.views import SearchRecommendationProfile, search_professional_profiles

urlpatterns = [
    path('', SearchRecommendationProfile.as_view(), name='SearchRecommendationProfile'),
    path('search/', search_professional_profiles, name='search_recommendation_profile'),

]
