from django.contrib import admin
from .models import Alert, Subscription, SymptomReport, GuidanceQuery, Clinic

# ----------------------------------------------------------------------
# ✅ Register all models to show them in the Django Admin dashboard
# ----------------------------------------------------------------------

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ("region", "hazard", "risk", "date_created")
    search_fields = ("region", "hazard", "risk")
    list_filter = ("risk", "date_created")
    ordering = ("-date_created",)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("name", "district", "channel", "contact", "date_subscribed")
    search_fields = ("name", "district", "channel", "contact")
    list_filter = ("channel", "district")
    ordering = ("-date_subscribed",)


@admin.register(SymptomReport)
class SymptomReportAdmin(admin.ModelAdmin):
    list_display = ("symptoms", "possible_conditions", "advice", "date_reported")
    search_fields = ("symptoms", "possible_conditions")
    ordering = ("-date_reported",)


@admin.register(GuidanceQuery)
class GuidanceQueryAdmin(admin.ModelAdmin):
    list_display = ("message", "response", "date_created")
    search_fields = ("message", "response")
    ordering = ("-date_created",)


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ("name", "district", "type", "phone", "latitude", "longitude", "date_added")
    search_fields = ("name", "district", "type", "phone")
    list_filter = ("type",)
    ordering = ("-date_added",)


# ----------------------------------------------------------------------
# ✅ Optional customization for admin panel branding
# ----------------------------------------------------------------------

admin.site.site_header = "ClimHealth AI – Admin Dashboard"
admin.site.site_title = "ClimHealth AI Admin"
admin.site.index_title = "Manage Alerts, Clinics, Subscriptions & Reports"
