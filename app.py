import requests
import os

API_KEY = os.getenv("API_KEY", "c9458f73-41fb-42fa-9ac4-e4cca1897563")
BASE_URL = "https://sandbox.vizionapi.com/v3/shipments"

params = {"booking_number": "HANFA4349300"}
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

print("Fetching shipment data...")

try:
    response = requests.get(BASE_URL, headers=headers, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()
    print("✅ SUCCESS! Shipment data:")
    print(data)
except requests.exceptions.RequestException as e:
    print("❌ Error occurred:")
    print(e)
