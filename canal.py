import requests
import random
import time


API_KEY = "M1B95IS41EVWUCMY"

def send_temperature_to_thingspeak(temperature):
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={temperature}"
    response = requests.get(url)
    print(f"Enviando temperatura: {temperature}°C para ThingSpeak, Resposta: {response.status_code}")

if __name__ == "__main__":
    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)  
        send_temperature_to_thingspeak(temperature)
        time.sleep(15)  # Enviar a cada 15 segundos
