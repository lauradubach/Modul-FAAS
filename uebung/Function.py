import json
import urllib.request


def lambda_handler(event, context):
    # Extrahiere die IP und User-Agent aus dem Event
    headers = event.get('headers', {})
    ip = headers.get('X-Forwarded-For', 'IP not found')
    user_agent = headers.get('User-Agent', 'User-Agent not found')

    # Geo-Location API Aufruf (ip-api.com)
    geo_url = f"http://ip-api.com/json/{ip}"

    try:
        with urllib.request.urlopen(geo_url) as response:
            geo_data = json.load(response)
            country = geo_data.get('country', 'Unknown')
            city = geo_data.get('city', 'Unknown')
            lat = geo_data.get('lat', 'Unknown')
            lon = geo_data.get('lon', 'Unknown')
    except Exception as e:
        geo_data = {"error": str(e)}
        country, city, lat, lon = "Unknown", "Unknown", "Unknown", "Unknown"

    # Erstelle die Rückgabe als JSON
    body = {
        'ip': ip,
        'user_agent': user_agent,
        'geo_location': {
            'country': country,
            'city': city,
            'latitude': lat,
            'longitude': lon
        }
    }

    # Rückgabe des HTTP Responses
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body)
    }
