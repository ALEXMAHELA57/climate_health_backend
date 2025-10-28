from django.db import models

class Alert(models.Model):
    region = models.CharField(max_length=100)
    hazard = models.CharField(max_length=100)
    risk = models.CharField(max_length=50)
    advice = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

class SymptomReport(models.Model):
    symptoms = models.TextField()
    possible_conditions = models.TextField()
    advice = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    channel = models.CharField(max_length=50)
    date_subscribed = models.DateTimeField(auto_now_add=True)

class GuidanceQuery(models.Model):
    message = models.TextField()
    response = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

class Clinic(models.Model):
    name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
