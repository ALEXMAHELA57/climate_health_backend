from django.db import models

class Alert(models.Model):
    region = models.CharField(max_length=100)
    hazard = models.CharField(max_length=100)
    risk = models.CharField(max_length=50)
    advice = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.region} - {self.hazard} ({self.risk})"

class SymptomReport(models.Model):
    symptoms = models.TextField()
    possible_conditions = models.TextField()
    advice = models.TextField(default="Seek medical attention if symptoms persist or worsen.")
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.id}"

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    channel = models.CharField(max_length=50)  # sms | email | whatsapp
    contact = models.CharField(max_length=120, blank=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.channel})"

class GuidanceQuery(models.Model):
    message = models.TextField()
    response = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Q{self.id}"

class Clinic(models.Model):
    name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Hospital / Clinic / Health Center
    phone = models.CharField(max_length=50, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
