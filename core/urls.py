from django.urls import path
from . import views

urlpatterns = [
    path('alerts/', views.alerts_api, name='alerts_api'),
    path('symptoms/', views.symptom_checker_api, name='symptom_checker_api'),
    path('subscribe/', views.subscribe_api, name='subscribe_api'),
    path('riskmap/', views.riskmap_api, name='riskmap_api'),
    path('youth/', views.youth_api, name='youth_api'),
    path('education/', views.education_api, name='education_api'),
]
