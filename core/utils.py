import random
from datetime import datetime

REGIONS = {
    "Dar es Salaam": {"lat": -6.8, "lon": 39.28},
    "Dodoma": {"lat": -6.17, "lon": 35.74},
    "Mwanza": {"lat": -2.52, "lon": 32.90},
    "Arusha": {"lat": -3.37, "lon": 36.68},
    "Zanzibar": {"lat": -6.17, "lon": 39.19},
    "Morogoro": {"lat": -6.82, "lon": 37.66},
}

def generate_weather_forecast(region):
    if region not in REGIONS:
        region = "Dar es Salaam"
    coords = REGIONS[region]
    return {
        "region": region,
        "lat": coords["lat"],
        "lon": coords["lon"],
        "forecast_date": datetime.now().strftime("%Y-%m-%d"),
        "temperature": random.randint(25, 38),
        "rainfall_mm": random.randint(0, 60),
        "humidity": random.randint(40, 90),
    }

def analyze_risk(weather):
    temp = weather["temperature"]
    rain = weather["rainfall_mm"]
    if rain >= 50:
        return {"risk": "High", "hazard": "Flood Risk", "disease": "Cholera"}
    elif rain >= 30:
        return {"risk": "Medium", "hazard": "Mosquito Breeding", "disease": "Malaria"}
    elif temp >= 37:
        return {"risk": "Medium", "hazard": "Heatwave", "disease": "Heat Stress"}
    else:
        return {"risk": "Low", "hazard": "Normal", "disease": "None"}

def detect_conditions(symptoms_text):
    text = symptoms_text.lower()
    conditions = []
    if "fever" in text or "chills" in text:
        conditions.append("Malaria")
    if "diarrhea" in text or "vomit" in text:
        conditions.append("Cholera")
    if "cough" in text or "breath" in text:
        conditions.append("Pneumonia")
    if "rash" in text:
        conditions.append("Measles")
    return conditions if conditions else ["Unknown"]

def get_guidance_response(message):
    text = message.lower()
    if "rain" in text or "flood" in text:
        return "Avoid stagnant water and use treated water sources."
    elif "heat" in text or "sun" in text:
        return "Stay hydrated and avoid long exposure to direct sunlight."
    elif "mosquito" in text or "malaria" in text:
        return "Use mosquito nets and repellents, and seek medical care if fever occurs."
    elif "climate" in text or "weather" in text:
        return "Climate change affects health; stay alert for updates on local risks."
    else:
        return "Sorry, I can only answer questions related to climate and public health."
