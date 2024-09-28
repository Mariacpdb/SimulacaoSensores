import requests
import random
import time
import json
import paho.mqtt.client as mqtt


API_KEY = "FELVHXOQDN8N7DSE"
broker = 'localhost'
port = 1883
topic = 'sensores/energiasolar'  # Corrigido para ser consistente

def enviar_dados_thingspeak(dados):
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={dados['irradiancia']}&field2={dados['temperatura']}&field3={dados['corrente']}&field4={dados['voltagem']}&field5={dados['energia_gerada']}"
    response = requests.get(url)
    print(f"Enviando dados: {dados} para ThingSpeak, Resposta: {response.status_code}")

def menssagem_ativada(client, userdata, message):
    dados = json.loads(message.payload.decode())
    print(f'Dados recebidos: {dados}')
    
    if dados['temperatura'] > 45:
        print("Alerta: Temperatura elevada!")
    enviar_dados_thingspeak(dados)

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.on_message = menssagem_ativada
client.connect(broker, port)
client.subscribe(topic)

client.loop_forever()
