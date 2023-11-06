from django.urls import path
from . import views
from recomendation_content_system.views import DetailContent

urlpatterns = [
    #path('add-contenido/', views.AddContenido.as_view(), name='add_contenido_root'),
    #path('update-contenido/<int:pk>/', views.UpdateContenido.as_view(), name='update_contenido_root'),
    #path('detail-contenido/<int:pk>/', views.DetailContenido.as_view(), name='detail_contenido_root'),
    #path('list_job_offers', ListProfessionalOffers.as_view(), name='detail_contenido_to_student'),
    path('recommender_contentl/<int:pk>/', DetailContent.as_view(), name='detail_contenido_to_student'),
    #path('detail_contenido_to_student/<int:contenido_id>/', views.detail_contenido_to_student_view,
    #     name='detail_contenido_to_student'),
    #path('detail_contenido/<int:contenido_id>/', views.detail_contenido_view, name='detail_contenido'),
    #path('ad_contenido/', views.ad_contenido_view, name='ad_content'),
    path('list_contenidos/', views.ListContent.as_view(), name='list_contenidos'),
]
