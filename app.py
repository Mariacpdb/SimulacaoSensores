import paho.mqtt.client as mqtt
import random
import time
import json  
broker = 'localhost'  
port = 1883
topic = "sensor/energiasolar"

def gerardados():
    dados = {
        'irradiancia': random.uniform(500, 1000),
        'temperatura': random.uniform(20, 50),
        'corrente': random.uniform(4, 10),
        'voltagem': random.uniform(220, 250),
        'energia_gerada': random.uniform(1, 5)
    }

    return json.dumps(dados)  

def publish_dados():
    client = mqtt.Client(protocol=mqtt.MQTTv311)  
    client.connect(broker, port)  

    while True:
        dados = gerardados()  
        print(f"Publicando dados: {dados} no tópico {topic}")
        client.publish(topic, dados) 
        time.sleep(5)  

if __name__ == "__main__":
    publish_dados() 


