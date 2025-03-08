import urllib.request
import json

def get_weather(city):
    """
    Získá aktuální teplotu pro dané město pomocí API.
    """
    url = f"https://api.weather.com/v1/weather/{city}"
    
    try:
        with urllib.request.urlopen(url) as response:
            if response.getcode() != 200:
                raise ValueError(f"Chyba při získávání dat: {response.getcode()}")
            
            data = json.loads(response.read().decode())
            
            if "temperature" not in data:
                raise KeyError("Teplota nebyla nalezena v odpovědi API")
            
            return data["temperature"]
    except urllib.error.URLError as e:
        raise ValueError(f"Chyba při připojení k API: {e}")
    except json.JSONDecodeError:
        raise ValueError("Chyba při parsování odpovědi API")