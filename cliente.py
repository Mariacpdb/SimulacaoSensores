import paho.mqtt.client as mqtt

broker = 'localhost'
port = 1883
topic = "sensor/temperatura"


def on_message(client, userdata, message):
    print(f"Mensagem recebida no tópico {message.topic}: {message.payload.decode()}")


def subscribe():
  
    client = mqtt.Client(protocol=mqtt.MQTTv311)  
    client.on_message = on_message
    client.subscribe(topic)

    
    client.loop_forever()

if __name__ == "__main__":
    subscribe()
