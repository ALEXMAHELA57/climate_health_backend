from django.urls import path
from . import views

urlpatterns = [
    path("alerts/", views.alerts_api, name="alerts_api"),
    path("symptoms/", views.symptom_checker_api, name="symptom_checker_api"),
    path("guidance/", views.guidance_api, name="guidance_api"),
    path("clinics/", views.clinics_list, name="clinics_list"),
    path("education/", views.education_list, name="education_list"),
    path("youth/", views.youth_list, name="youth_list"),
    path("subscribe/", views.subscribe_api, name="subscribe_api"),
    path("admin/", views.admin_stats, name="admin_stats"),
]
