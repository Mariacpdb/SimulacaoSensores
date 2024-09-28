import requests
import random
import time


API_KEY = "M1B95IS41EVWUCMY"

def enviar_dados_thingspeak(dados):
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={dados}"
    response = requests.get(url)
    print(f"Enviando dados: {dados} para ThingSpeak, Resposta: {response.status_code}")

if __name__ == "__main__":
    while True:
        dados = gerardaddos()  
        enviar_dados_thingspeak(dados)
        time.sleep(15) 
