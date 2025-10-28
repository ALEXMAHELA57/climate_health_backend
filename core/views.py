from django.http import JsonResponse
from datetime import datetime
import random

# --- ALERTS API ---
def alerts_api(request):
    hazards = ["Heavy Rain", "Heatwave", "Flood Risk", "Cholera Risk", "Drought Alert"]
    data = {
        "district": "Dar es Salaam",
        "hazard": random.choice(hazards),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "risk": random.choice(["Low", "Medium", "High"]),
        "advice": "Avoid stagnant water, use bed nets, and drink boiled water."
    }
    return JsonResponse(data)


# --- SYMPTOM CHECKER API ---
def symptom_checker_api(request):
    symptoms = request.GET.get('symptoms', '')
    if not symptoms:
        return JsonResponse({"error": "Please provide symptoms (e.g., ?symptoms=fever,diarrhea)"})

    text = symptoms.lower()
    possible_conditions = []
    if 'fever' in text:
        possible_conditions.append("Malaria")
    if 'diarrhea' in text:
        possible_conditions.append("Cholera")
    if 'rash' in text:
        possible_conditions.append("Measles")

    result = {
        "symptoms": symptoms,
        "possible_conditions": possible_conditions or ["Unknown condition"],
        "advice": "Seek medical attention if symptoms persist or worsen."
    }
    return JsonResponse(result)


# --- SUBSCRIBE API ---
def subscribe_api(request):
    name = request.GET.get('name', 'Anonymous')
    channel = request.GET.get('channel', 'email')
    district = request.GET.get('district', 'Unknown')

    return JsonResponse({
        "message": f"Subscription saved for {name} via {channel} in {district}.",
        "status": "ok"
    })


# --- RISK MAP API ---
def riskmap_api(request):
    regions = [
        {"region": "Dar es Salaam", "risk": "High", "hazard": "Flood"},
        {"region": "Dodoma", "risk": "Low", "hazard": "Drought"},
        {"region": "Mwanza", "risk": "Medium", "hazard": "Heatwave"},
        {"region": "Zanzibar", "risk": "Low", "hazard": "Normal"},
    ]
    return JsonResponse({"data": regions})


# --- YOUTH API ---
def youth_api(request):
    activities = [
        {"title": "Clean Water Awareness", "region": "Morogoro", "participants": 120},
        {"title": "Tree Planting", "region": "Arusha", "participants": 85},
        {"title": "Climate Health Debate", "region": "Dar es Salaam", "participants": 60},
    ]
    return JsonResponse({"activities": activities})


# --- EDUCATION API ---
def education_api(request):
    lessons = [
        {"topic": "Malaria Prevention", "quiz": ["What causes malaria?", "How do mosquitoes breed?"]},
        {"topic": "Clean Water", "quiz": ["Why boil water?", "What diseases are waterborne?"]},
        {"topic": "Heat Safety", "quiz": ["What is heatstroke?", "How can you stay hydrated?"]},
    ]
    return JsonResponse({"lessons": lessons})
