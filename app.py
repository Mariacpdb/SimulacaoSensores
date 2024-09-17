import paho.mqtt.client as mqtt
import random
import time

# Definir as configurações do broker
broker = 'localhost'  # ou use o IP do servidor se estiver em uma máquina remota
port = 1883
topic = "sensor/temperatura"

# Função para publicar dados
def publish_temperature():
    # Use a nova API de callback
    client = mqtt.Client(protocol=mqtt.MQTTv311)  # Especifica a versão do protocolo MQTT
    client.connect(broker, port)

    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)  # Simular valores entre 20 e 30°C
        print(f"Publicando temperatura: {temperature}°C no tópico {topic}")
        client.publish(topic, temperature)
        time.sleep(5)  # Publicar a cada 5 segundos

if __name__ == "__main__":
    publish_temperature()


