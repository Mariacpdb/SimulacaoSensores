import paho.mqtt.client as mqtt
import random
import time


broker = 'localhost'  
port = 1883
topic = "sensor/temperatura"


def publish_temperature():
    
    client = mqtt.Client(protocol=mqtt.MQTTv311) 
    client.connect(broker, port)

    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)  
        print(f"Publicando temperatura: {temperature}°C no tópico {topic}")
        client.publish(topic, temperature)
        time.sleep(5) 

if __name__ == "__main__":
    publish_temperature()


