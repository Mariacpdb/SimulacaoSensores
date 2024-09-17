import paho.mqtt.client as mqtt

broker = 'localhost'
port = 1883
topic = "sensor/temperatura"

# Função que é chamada quando uma mensagem é recebida
def on_message(client, userdata, message):
    print(f"Mensagem recebida no tópico {message.topic}: {message.payload.decode()}")

# Função para subscrever ao tópico
def subscribe():
    # Use a nova API de callback especificando a versão mais recente do protocolo MQTT
    client = mqtt.Client(protocol=mqtt.MQTTv311)  # Atualiza a API
    client.connect(broker, port)
    client.on_message = on_message
    client.subscribe(topic)

    # Ficar ouvindo o tópico
    client.loop_forever()

if __name__ == "__main__":
    subscribe()
