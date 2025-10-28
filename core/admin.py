from django.contrib import admin
from .models import Alert, Subscription, SymptomReport, GuidanceQuery, Clinic

# Register all models so they show up in the Django Admin panel
@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ("region", "hazard", "risk", "date_created")
    search_fields = ("region", "hazard", "risk")
    list_filter = ("risk", "date_created")

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("name", "district", "channel", "date_subscribed")
    search_fields = ("name", "district", "channel")
    list_filter = ("channel", "district")

@admin.register(SymptomReport)
class SymptomReportAdmin(admin.ModelAdmin):
    list_display = ("symptoms", "possible_conditions", "date_reported")
    search_fields = ("symptoms", "possible_conditions")

@admin.register(GuidanceQuery)
class GuidanceQueryAdmin(admin.ModelAdmin):
    list_display = ("message", "response", "date_created")
    search_fields = ("message", "response")

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ("name", "district", "type", "phone", "date_added")
    search_fields = ("name", "district", "type")
    list_filter = ("type",)
