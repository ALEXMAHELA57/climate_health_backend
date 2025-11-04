from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Alert, Subscription, SymptomReport, GuidanceQuery, Clinic

# ---------- Alerts ----------
def alerts_api(request):
    # Return the latest 30 alerts (or seed if empty)
    if Alert.objects.count() == 0:
        Alert.objects.create(region="Dar es Salaam", hazard="Heavy Rain", risk="High",
                             advice="Avoid stagnant water; boil water; use bed nets.")
        Alert.objects.create(region="Dodoma", hazard="Heatwave", risk="Medium",
                             advice="Avoid sun 11am-3pm; hydrate; check elderly.")
    data = list(Alert.objects.order_by("-date_created")[:30].values(
        "region", "hazard", "risk", "advice", "date_created"
    ))
    return JsonResponse(data, safe=False)

# ---------- Symptom Checker ----------
def symptom_checker_api(request):
    q = request.GET.get("q", "")  # symptoms text
    text = q.lower()
    conds = []
    if "fever" in text or "homa" in text or "fièvre" in text:
        conds.append("Malaria")
    if "diarrhea" in text or "kuharisha" in text or "diarrhée" in text:
        conds.append("Cholera")
    if "rash" in text or "upele" in text or "éruption" in text:
        conds.append("Measles")

    if conds:
        risk = "medium" if len(conds) <= 2 else "high"
    else:
        risk = "low"

    advice = "Use bed nets, boil water, and visit a facility if symptoms persist."
    SymptomReport.objects.create(symptoms=q, possible_conditions=", ".join(conds) or "Unknown", advice=advice)
    return JsonResponse({
        "symptoms": q,
        "possible_conditions": conds or ["Unknown"],
        "risk_level": risk,
        "advice": advice
    })

# ---------- Guidance (simple rule-based) ----------
def guidance_api(request):
    msg = request.GET.get("message", "")
    low = msg.lower()
    allowed_keywords = ["climate", "weather", "rain", "mvua", "chafya", "heat", "joto",
                        "flood", "mafuriko", "cholera", "malaria", "air quality", "quality",
                        "drought", "ukame", "storm", "uv", "temperatur", "joto", "mosquito"]
    if not any(k in low for k in allowed_keywords):
        resp = ("I only answer questions about climate and public health. "
                "For example: heat, rain, floods, malaria, cholera, air quality, drought.")
    else:
        resp = ("Stay safe: avoid flood water, boil drinking water, use bed nets, "
                "hydrate during heat, and check local alerts.")
    GuidanceQuery.objects.create(message=msg, response=resp)
    return JsonResponse({"response": resp})

# ---------- Clinics ----------
def clinics_list(request):
    # If no clinics, seed a few demo points
    if Clinic.objects.count() == 0:
        Clinic.objects.create(name="Muhimbili National Hospital", district="Ilala",
                              type="Hospital", phone="+255 22 2151591",
                              latitude=-6.804, longitude=39.271)
        Clinic.objects.create(name="Amana Regional Hospital", district="Ilala",
                              type="Hospital", phone="+255 22 2115157",
                              latitude=-6.823, longitude=39.274)

    data = list(Clinic.objects.all().values("name", "district", "type", "phone", "latitude", "longitude"))
    return JsonResponse(data, safe=False)

# ---------- Education ----------
def education_list(request):
    data = [
        {"title": "Preventing Cholera After Floods",
         "description": "Boil water, use chlorine tablets, wash hands, and keep latrines safe.",
         "link": "https://www.who.int"},
        {"title": "Heatwave First Aid",
         "description": "Move to shade, cool body with wet cloth, sip water slowly.",
         "link": "https://www.cdc.gov"}
    ]
    return JsonResponse(data, safe=False)

# ---------- Youth ----------
def youth_list(request):
    data = [
        {"title": "School Climate Clubs",
         "description": "Start a climate-health club: clean-ups, awareness posters, water safety.",
         "link": "https://www.unicef.org"},
        {"title": "Community Mosquito Control",
         "description": "Eliminate standing water; teach neighbors; report mosquito breeding sites.",
         "link": "https://www.who.int"}
    ]
    return JsonResponse(data, safe=False)

# ---------- Subscribe ----------
def subscribe_api(request):
    name = request.GET.get("name", "").strip()
    district = request.GET.get("district", "").strip()
    channel = request.GET.get("channel", "").strip()  # sms | email | whatsapp
    contact = request.GET.get("contact", "").strip()

    # basic validation
    if not name or not district or channel not in ["sms", "email", "whatsapp"] or not contact:
        return JsonResponse({"ok": False, "error": "Invalid fields. Provide name, district, channel, contact."}, status=400)

    Subscription.objects.create(name=name, district=district, channel=channel, contact=contact)
    return JsonResponse({"ok": True, "message": f"Subscription saved for {name} via {channel} ({district})."})

# ---------- Admin Dashboard Quick Stats ----------
def admin_stats(request):
    data = {
        "lessons_count": 2,
        "users_count": Subscription.objects.count(),
        "reports": SymptomReport.objects.count(),
        "server_time": timezone.now().isoformat()
    }
    return JsonResponse(data)
